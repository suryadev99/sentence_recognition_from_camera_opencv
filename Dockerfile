# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    v4l-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first
COPY requirements.txt /app/

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]
