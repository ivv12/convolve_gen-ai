from utils.ocr import pdf_to_images, run_ocr
from utils.document import build_document_ocr

images = pdf_to_images("sample.pdf")
doc_ocr = build_document_ocr(images, run_ocr)

print("Total OCR blocks in document:", len(doc_ocr))

# Print first 10 blocks
for block in doc_ocr[:10]:
    print(block)
