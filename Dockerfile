FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make sure your model file is copied into the container
COPY yolov8n.pt .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV OPENCV_IO_ENABLE_JASPER=true
ENV QT_QPA_PLATFORM=offscreen

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
