import streamlit as st
import easyocr

@st.cache_resource
def load_reader():
    # Lazy-load and cache the OCR model
    return easyocr.Reader(['en'], gpu=True)

def run_ocr(image):
    reader = load_reader()
    results = reader.readtext(image)

    ocr_results = []
    for bbox, text, conf in results:
        ocr_results.append((bbox, text, conf))

    return ocr_results
