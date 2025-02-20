from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# If using Windows, set the Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        image = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(image, lang="eng")
        os.remove(file_path)  # Clean up the image after processing
        return jsonify({"text": extracted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
