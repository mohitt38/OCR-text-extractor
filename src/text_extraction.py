import re

def extract_barcode_text(ocr_results, strict=True):
    best_text = None
    best_conf = 0.0

    for _, text, conf in ocr_results:
        clean = text.replace(" ", "").strip()

        if strict:
            if "_1_" in clean and conf >= 0.75:
                return clean, conf

        else:
            # numeric fallback ONLY
            if clean.isdigit() and len(clean) >= 10 and conf >= 0.75:
                if conf > best_conf:
                    best_text = clean
                    best_conf = conf

    return best_text, best_conf
