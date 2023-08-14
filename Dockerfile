FROM python:3.8

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential cmake && \
    apt-get install -y libopenblas-dev libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libatlas-base-dev gfortran

# Copy your app files
COPY . /app

# Set the environment variable
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Install Python dependencies
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "FaceRecognition-One-shot.py"]
