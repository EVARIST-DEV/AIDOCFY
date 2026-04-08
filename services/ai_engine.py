import google.generativeai as genai
import os
import PIL.Image
from pydantic import BaseModel
from typing import List, Optional

# (Insert the BoundingBox, ExtractedField, TrustSignal, and DocumentExtraction classes here)

def extract_document_data(image_path: str) -> 'DocumentExtraction':
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    img = PIL.Image.open(image_path)
    prompt = """
    Analyze this procurement document. 
    1. Extract fields: 'lpo_reference' and 'total_amount'.
    2. Visually scan for official stamps or seals.
    CRITICAL: Provide bounding box coordinates as normalized percentages (0.0 to 1.0).
    """
    
    response = model.generate_content(
        [prompt, img],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema=DocumentExtraction,
            temperature=0.1,
        )
    )
    return DocumentExtraction.model_validate_json(response.text)