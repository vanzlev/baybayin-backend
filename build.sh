#!/bin/bash

# Update package list and install Tesseract OCR
apt-get update && apt-get install -y tesseract-ocr

# Run the Flask app
python app.py
