# Fruit and Vegetable Detector

This project provides an API for detecting and counting fruits and vegetables in images using YOLOv8.

## Building the Docker image

To build the Docker image, run the following command in the project root:

```
docker build -t fruit-veg-detector .
```

## Running the container

To run the container, use:

```
docker run -p 8000:8000 fruit-veg-detector
```

The API will be available at `http://localhost:8000`.

## Using the API

To detect fruits and vegetables in an image, send a POST request to the `/detect` endpoint:

```
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8000/detect
```

The API will return a JSON response with the detected fruits and vegetables and their counts.

## API Documentation

Endpoint: POST /detect
Input: multipart/form-data with a "file" field containing the image
Output: JSON object with detected classes and their counts

Example output:
```json
{
  "apple": 2,
  "orange": 3,
  "banana": 1
}
```