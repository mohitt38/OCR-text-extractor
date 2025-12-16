import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def run_ocr(image):
    results = reader.readtext(image)
    ocr_results = []

    for bbox, text, conf in results:
        ocr_results.append((bbox, text, conf))

    return ocr_results
