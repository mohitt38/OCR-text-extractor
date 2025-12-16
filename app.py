import streamlit as st
import numpy as np
import cv2

from src.barcode_decoder import decode_barcode
from src.ocr_engine import run_ocr
from src.text_extraction import extract_barcode_text
from src.preprocessing import preprocess_image

st.title("OCR Text Extractor")

uploaded_file = st.file_uploader(
    "Upload a label image", type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # ✅ Show ONLY uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save temp image
    temp_path = "temp.jpg"
    cv2.imwrite(temp_path, image)

    # Barcode decode (authoritative)
    barcode_text = decode_barcode(temp_path)

    # Preprocess image (used internally ONLY)
    processed = preprocess_image(image)

    if barcode_text:
        st.success("Barcode decoded successfully")
        st.write("**Extracted Text:**", barcode_text)

    else:
        st.warning("Trying OCR fallback...")

        # OCR
        ocr_results = run_ocr(processed)

        # Strict regex extraction
        text, conf = extract_barcode_text(ocr_results)

        if text and conf >= 0.6:
            st.success("OCR extraction successful")
            st.write("**Extracted Text:**", text)
            st.write("**Confidence:**", f"{conf:.2f}")
        else:
            st.error("Extraction failed. No valid text found.")
