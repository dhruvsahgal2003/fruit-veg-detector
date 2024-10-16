# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the API when the container launches
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]