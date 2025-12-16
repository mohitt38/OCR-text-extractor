from src.barcode_decoder import decode_barcode
from src.preprocessing import load_image
from src.ocr_engine import run_ocr
from src.text_extraction import extract_barcode_text

image_path = r"Sample_img/ReverseWay Bill/reverseWaybill-163138358833942080_1.jpg"

# STEP 1: Try barcode decoding (PRIMARY)
barcode_text = decode_barcode(image_path)

conf = None

# STEP 2: OCR fallback
if barcode_text is None:
    image = load_image(image_path)

    if image is None:
        print("Image could not be loaded. Check file path.")
    else:
        ocr_results = run_ocr(image)
        barcode_text, conf = extract_barcode_text(ocr_results)
else:
    conf = 1.0  # barcode decoding is exact

print("\nFINAL RESULT:")
print("Extracted Text:", barcode_text)
print("Confidence:", conf if conf else "N/A")
