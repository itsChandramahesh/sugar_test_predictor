# Sugar-Test-Predictor
A Flask-based web application that predicts fasting and post-meal blood sugar levels by extracting data from uploaded sugar test reports using OCR (Optical Character Recognition). Users can also enter their sugar levels manually to receive instant health status feedback.
# Sugar Test Predictor — Blood Sugar Level Analyzer with OCR and Flask

A Flask-based web application that predicts fasting and post-meal blood sugar levels by extracting data from uploaded sugar test reports using OCR (Optical Character Recognition). Users can also manually input their sugar levels to receive instant health status feedback.

---

## Features

- Extract sugar values automatically from medical report images using Tesseract OCR  
- Manual input option for fasting and post-meal blood sugar levels  
- Categorizes sugar levels as **Normal**, **High**, or **Critical** based on thresholds  
- Responsive and user-friendly interface built with HTML, CSS, and JavaScript  
- Backend powered by Python, Flask, and OpenCV for image preprocessing  

---

## Technologies Used

- Python  
- Flask  
- Tesseract OCR (`pytesseract`)  
- OpenCV (`opencv-python-headless`)  
- HTML, CSS, JavaScript  

---

## Getting Started

### Prerequisites

- Python 3.8+ installed  
- Tesseract OCR installed on your system (for local testing)  
  - [Installation Guide](https://github.com/tesseract-ocr/tesseract#installing-tesseract)  

### Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/sugar-test-predictor.git
   cd sugar-test-predictor
   
2.reate and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run the app locally:

python app.py

5.Open your browser at http://127.0.0.1:5000 to use the app.
