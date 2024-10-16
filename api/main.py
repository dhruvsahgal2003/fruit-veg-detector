from fastapi import FastAPI, File, UploadFile, HTTPException
from src.detect import detect_and_count
import io
from PIL import Image
import os

app = FastAPI()

@app.post("/detect")
async def detect_fruits_vegetables(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        image_path = "temp_image.jpg"
        image.save(image_path)

        results = detect_and_count(image_path)

        os.remove(image_path)

        if "error" in results:
            raise HTTPException(status_code=500, detail=results["error"])

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Detection was run successully, check the results on postman"}
