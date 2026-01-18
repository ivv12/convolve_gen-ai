def build_document_ocr(images, run_ocr_fn):
    """
    Runs OCR on all pages and builds a unified document representation.

    Args:
        images (List[np.ndarray]): Images from pdf_to_images
        run_ocr_fn (function): OCR function (run_ocr)

    Returns:
        List[dict]: Unified list of OCR blocks for the whole document
    """
    document_ocr = []

    for page_index, image in enumerate(images):
        page_ocr = run_ocr_fn(image)

        # Optionally store page index (useful later)
        for block in page_ocr:
            block["page"] = page_index
            document_ocr.append(block)

    return document_ocr
