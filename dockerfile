FROM python:3.11-slim

# Sistem bağımlılıkları
RUN apt-get update && \
    apt-get install -y tesseract-ocr poppler-utils libsm6 libxext6 libxrender-dev && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]