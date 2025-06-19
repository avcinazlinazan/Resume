import textract
from PIL import Image
import pytesseract

def extract_text_from_file(file_path: str) -> str:
    if file_path.endswith(('.pdf', '.docx', '.txt')):
        text = textract.process(file_path).decode('utf-8')
    elif file_path.endswith(('.jpg', '.jpeg', '.png')):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
    else:
        raise ValueError("Desteklenmeyen dosya türü")
    return text