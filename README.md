<<<<<<< HEAD
# Procurement Document Verifier

A Flask-based OCR verification prototype with Gemini OCR stub, rule engine, and bounding-box visualization.

## Project structure

- `.env` - Gemini API key. (Do not commit)
- `requirements.txt` - Python dependencies
- `app.py` - Flask entrypoint
- `services/` - core modules
  - `ai_engine.py` - Gemini OCR client + data models
  - `rules_engine.py` - Accept/Reject/Review logic
  - `vision_engine.py` - Pillow overlay drawing
- `static/processed_images/` - output images
- `templates/index.html` - upload frontend

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` or edit `.env`:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

## Run

```bash
python app.py
```

Navigate to `http://localhost:5000`.

## Gemini OCR integration (TODO)

In `services/ai_engine.py`, replace the `run_ocr` dummy block with the actual Gemini OCR endpoint. Example:

- `url = 'https://api.gemini.example/vision/ocr'`
- Authorization header: `Bearer <api_key>`
- JSON payload includes image bytes or base64
- parse response into `OCRResponse` and `OCRBox`

## Notes

- `rules_engine.py` currently uses text matching for decisions.
- `vision_engine.py` draws reds bounding boxes and text labels.
- `static/processed_images` is excluded from git under `.gitignore`.
=======
# AIDOCFY
AI document verifier
>>>>>>> 11ba17a5b6ecb38987695a945310f702ea8e0a71
