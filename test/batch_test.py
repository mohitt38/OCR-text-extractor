import os
import json
import cv2

from src.barcode_decoder import decode_barcode
from src.preprocessing import preprocess_image
from src.ocr_engine import run_ocr
from src.text_extraction import extract_barcode_text

IMAGE_DIR = "Sample_img/ReverseWay Bill"
results = []

for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    path = os.path.join(IMAGE_DIR, file)

    # 1️⃣ Read image ONCE
    image = cv2.imread(path)
    if image is None:
        continue

    # 2️⃣ Try barcode decode on original image
    text = decode_barcode(path)
    conf = 1.0 if text else None

    # 3️⃣ OCR fallback
    if text is None:
        processed = preprocess_image(image)
        ocr_results = run_ocr(processed)
        text, conf = extract_barcode_text(ocr_results)

    results.append({
        "image": file,
        "extracted_text": text,
        "confidence": conf
    })

# Save results
os.makedirs("results", exist_ok=True)
with open("results/batch_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Batch processing completed.")
