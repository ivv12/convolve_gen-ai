from utils.ocr import pdf_to_images

images = pdf_to_images("sample.pdf")

print("Number of pages:", len(images))
print("Shape of first image:", images[0].shape)
