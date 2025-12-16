
import re

def decode_barcode(image_path):
    try:
        from pyzbar.pyzbar import decode
        import cv2
        image = cv2.imread(image_path)
        if image is None:
            return None

        decoded_objects = decode(image)
        if not decoded_objects:
            return None

        texts = []

        for obj in decoded_objects:
            text = obj.data.decode("utf-8", errors="ignore").strip()
            if text:
                texts.append(text)
    
        for t in texts:
            if "_1_" or "_1" or "1_" in t:
                return t


        for t in texts:
            if re.search(r"\d+", t):   # contains any number
                return t
            
            
        return texts[0] if texts else None
    
    except ImportError:
        print("pyzbar library is not installed. Barcode decoding is unavailable.")
        return None
