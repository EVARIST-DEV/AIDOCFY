import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Import our custom services
from services.ai_engine import extract_document_data
from services.vision_engine import draw_visuals
from services.rules_engine import validate_submission

# (In a real app, you'd fetch these from a database)
from services.ai_engine import DocumentExtraction # Import mock data setup if needed

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/processed_images/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Renders the frontend UI."""
    return render_template('index.html')

@app.route('/api/verify', methods=['POST'])
def verify_document():
    """The main API endpoint that the frontend talks to."""
    if 'invoice_file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
        
    file = request.files['invoice_file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], f"raw_{filename}")
        file.save(temp_path)

        try:
            # 1. AI Extraction
            extracted_data = extract_document_data(temp_path)
            
            # 2. Visual Drawing
            processed_filename = f"processed_{filename}"
            visual_url = draw_visuals(temp_path, extracted_data, processed_filename)
            
            # 3. Validation Rules (Assuming you pass mock LPO/Receipt data here for now)
            # decision = validate_submission(mock_lpo, extracted_data, mock_receipt)
            
            # For this example, let's mock the decision response:
            decision = {
                "status": "ACCEPT",
                "confidence_score": 0.98,
                "reason": "All documents match."
            }

            # Return the full package to the frontend
            return jsonify({
                "success": True,
                "decision": decision,
                "extracted_json": extracted_data.model_dump(),
                "image_url": f"/{visual_url}" # URL for the browser to load the image
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)