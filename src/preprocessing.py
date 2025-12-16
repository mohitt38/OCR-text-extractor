import cv2

def preprocess_image(image):
    """
    image: numpy array (BGR)
    Crops bottom region and prepares for OCR / barcode
    """

    if image is None:
        return None

    h, w = image.shape[:2]

    # Crop bottom 50% (receiver barcode region)
    y_start = int(h * 0.50)
    cropped = image[y_start:h, :]

    # Convert to grayscale
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Threshold
    _, thresh = cv2.threshold(
        enhanced, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresh
