from .ai_engine import OCRResponse


def decide_document(ocr_response: OCRResponse) -> str:
    normalized = ocr_response.text.lower()
    if 'approved' in normalized or 'valid' in normalized:
        return 'Accepted'
    if 'reject' in normalized or 'invalid' in normalized:
        return 'Rejected'
    return 'Needs manual review'
