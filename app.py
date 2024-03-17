from fastapi import FastAPI, File, UploadFile
from typing import List
from models_utils import classify_image 
from PIL import Image
import io
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
@app.post("/upload-image/")
async def create_upload_file(image: UploadFile = File(...)):
    # Чтение содержимого изображения
    image_contents = await image.read()
    # Преобразование в объект BytesIO
    img = Image.open(io.BytesIO(image_contents))
    report = classify_image(img)
    
    return {"filename": image.filename,"result":report}