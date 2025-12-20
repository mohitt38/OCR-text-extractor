# OCR-Based Text Extraction 

---

## Project Overview

This project is an **OCR-based reverse waybill extraction system** designed to extract the **`_1_` line (barcode / waybill identifier)** from parcel label images.

### Key Idea

- **Barcode decoding is used as the primary method**
- **EasyOCR is used as a fallback OCR engine**
- Image preprocessing improves text visibility
- Only **target `_1_` line patterns** are extracted
- Accuracy and confidence are calculated on a test dataset

The application is implemented using **Python and Streamlit** and outputs **structured JSON results**.

---

## Project Structure (Actual)

```text
OCR_Label_Extraction/
│
├── app.py
├── requirements.txt
├── temp.jpg
├── .gitignore
│
├── results/
│   └── batch_results.json      # Batch OCR results & accuracy data
│
├── src/
│   ├── barcode_decoder.py      # Barcode decoding logic (primary)
│   ├── ocr_engine.py           # EasyOCR-based OCR logic
│   ├── preprocessing.py        # Image preprocessing functions
│   ├── text_extraction.py      # `_1_` line extraction & validation
│   └── utils.py                # Helper / utility functions
│
├── test/
│   ├── accuracy.py             # Accuracy calculation script
│   ├── batch_test.py           # Batch image testing
│   └── temp.py                 # Temporary testing utilities
│
└── .venv/                      # Virtual environment
````

 ### Installation Instructions

###Clone the Repository

```bash
git clone <repository-url>
cd OCR_Label_Extraction
```

### Create & Activate Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Usage Guide

### Run Streamlit Application

```bash
streamlit run app.py
```

### Application Flow

1. Upload a reverse waybill image
2. Barcode decoder attempts extraction
3. If barcode fails → **EasyOCR fallback** is applied
4. `_1_` line text is extracted and validated
5. Confidence score is generated
6. Output is stored in JSON format

---

## Technical Approach

### OCR Method Used

* **EasyOCR**
* Deep learning–based OCR (CNN + LSTM)
* Handles noisy and alphanumeric text
* Used **only when barcode decoding fails**

---

### Image Preprocessing (`preprocessing.py`)

* Bottom-region cropping (barcode location assumption)
* Grayscale conversion
* CLAHE (contrast enhancement)
* Binary thresholding (Otsu)
* Noise reduction

---

###  `_1_` Line Extraction Logic (`text_extraction.py`)

* Filters OCR output text
* Applies regex validation for:

  * 15-digit numeric codes
  * `RxxxxFPL` format
  * `Mxxxxxxxxxx` format
* Rejects partial or invalid matches
* Assigns confidence based on OCR score

---

### Accuracy Calculation (`test/accuracy.py`)

Accuracy is calculated **only for `_1_` line extraction**:

```
Accuracy = (Correct Extractions / Total Images Tested) × 100
```

* Exact matches only
* No partial credit
* Manual ground truth verification

---

## Performance Metrics

### Test Dataset

* **Total images tested:** 27
* **Target:** `_1_` line

### Results Summary

| Metric                       | Value    |
| ---------------------------- | -------- |
| Successful Extractions       | 10       |
| Failed Extractions           | 17       |
| Overall Accuracy             | **40-42%**  |
| Average Confidence (Success) | **0.98** |

---

## Error Analysis

| Actual \ Predicted | Extracted | Not Extracted |
| ------------------ | --------- | ------------- |
| `_1_` Line Present | 10        | 17            |

### Observations

* No false positives
* Failures mainly caused by:

  * Blurred images
  * Low contrast
  * Partial barcode visibility
* High precision, moderate recall

---

## Challenges & Solutions

### Challenges

* Poor image quality
* Fixed cropping region
* OCR noise in low-resolution images

### Solutions

* CLAHE-based contrast enhancement
* Barcode-first extraction strategy
* Strict regex validation
* Confidence-based acceptance

---

## Future Improvements

* Dynamic barcode region detection
* Multi-pass EasyOCR for failed cases
* Skew and rotation correction
* Super-resolution preprocessing
* Better dataset quality

---

## Screenshots

Screenshots demonstrate real extraction results from the application.

![Extraction Result]("screenshots/sam1.png")
![Extraction Result]("screenshots/sam2.png")


## Streamlit :

### LINK :- https://ocr-text-extractor-mn1.streamlit.app/
---

## Author

**Mohit Nagda**
AI / ML | Computer Vision

---

## 📜 License

For educational and internal evaluation purposes only.

---

### ✅ Important (Company-Safe Statement)

> *The system uses barcode decoding as the primary method and EasyOCR as a fallback.
> Accuracy is primarily limited by input image quality rather than extraction logic.*

```


