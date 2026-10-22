# OCR Text Extractor

Barcode-first **parcel label OCR** that pulls the waybill / `_1_` identifier from real-world label images. EasyOCR is used as a fallback when barcode decoding is not enough.

**Portfolio:** [mohit-nagda.vercel.app](https://mohit-nagda.vercel.app/#projects) · **Author:** [Mohit Nagda](https://github.com/mohitt38)

---

## Problem

Parcel labels are noisy photos. Full-page OCR is slow and error-prone when you only need the barcode / waybill line.

## What I built

- Barcode decoding as the primary extraction path
- EasyOCR fallback with image preprocessing
- Target-pattern extraction for `_1_` waybill lines
- Confidence / accuracy evaluation on a test set
- Streamlit app with structured JSON output

## Tech stack

`Python` · `EasyOCR` · `Computer Vision` · `Streamlit`

## Run locally

```bash
git clone https://github.com/mohitt38/OCR-text-extractor.git
cd OCR-text-extractor
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Screenshots

Add a demo screenshot of the Streamlit UI with a sample label + extracted JSON.

## Related

- Portfolio: https://mohit-nagda.vercel.app/#projects
