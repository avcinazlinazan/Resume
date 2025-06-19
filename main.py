from fastapi import FastAPI, File, UploadFile, HTTPException
from extractor import extract_text_from_file
from openai_structurer import get_structured_resume
from models import ResumeStructured
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import shutil

app = FastAPI()

@app.post("/parse_resume", response_model=ResumeStructured)
async def parse_resume(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        text = extract_text_from_file(temp_path)
        result = get_structured_resume(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        os.remove(temp_path)



# Statik dosyaları sun
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ana sayfa olarak index.html sun
@app.get("/", response_class=FileResponse)
def root():
    return "static/index.html"