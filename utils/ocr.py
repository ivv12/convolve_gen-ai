import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path


def pdf_to_images(pdf_path):
    """
    Converts a PDF into a list of images (one per page).
    """
    pages = convert_from_path(pdf_path, dpi=300)

    images = []
    for page in pages:
        img = np.array(page)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        images.append(img)

    return images


def run_ocr(image):
    """
    Runs OCR using Tesseract.
    Returns a list of {text, conf, bbox}.
    """
    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    results = []
    n = len(data["text"])

    for i in range(n):
        text = data["text"][i].strip()
        if text == "":
            continue

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        conf_raw = data["conf"][i]
        conf = float(conf_raw) / 100 if conf_raw != "-1" else 0.0

        results.append({
            "text": text,
            "conf": conf,
            "bbox": [x, y, x + w, y + h]
        })

    return results
