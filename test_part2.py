import utils.ocr
print("OCR FILE PATH:", utils.ocr.__file__)

from utils.ocr import pdf_to_images, run_ocr

images = pdf_to_images("sample.pdf")
ocr_lines = run_ocr(images[0])

print("Total OCR lines:", len(ocr_lines))
