FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y tesseract-ocr
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]