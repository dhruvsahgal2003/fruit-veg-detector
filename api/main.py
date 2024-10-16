from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.detect import detect_and_count

app = FastAPI()

@app.post("/detect")
async def detect_fruits_vegetables(file: UploadFile = File(...)):
    # Read and save the uploaded image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_path = "temp_image.jpg"
    image.save(image_path)

    # Perform detection and counting
    results = detect_and_count(image_path)

    # Remove the temporary image
    os.remove(image_path)

    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)