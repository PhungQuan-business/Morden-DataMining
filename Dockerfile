# FROM python:3.9
# WORKDIR /app
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY ./best.pt .
# COPY ./api.py .
# COPY ./predict.py .
# EXPOSE 5000
# CMD ["python", "api.py"]

# FROM python:3.9

# # Install necessary packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     python3-pip     \
#     libgl1-mesa-glx \
#     libsm6          \
#     libxext6        \
#     libxrender-dev  \
#     libglib2.0-0    \
#     git             \
#     python3-dev     \
#     python3-wheel

# RUN pip3 install --upgrade pip \
#     && pip3 install   \
#     gradio        \
#     opencv-python \
#     supervision   \
#     mmengine      \
#     setuptools    \
#     openmim       \
#     && mim install mmcv==2.0.0 \
#     && pip3 install --no-cache-dir --index-url https://download.pytorch.org/whl/cu118 \
#     wheel         \
#     torch         \
#     torchvision   
# # Set the working directory
# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# # Expose the port the app runs on
# EXPOSE 5000

# # Run the application
# CMD ["python", "api.py"]


# Dockerfile
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install opencv dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txtiterm

# Copy application code
COPY . .

# Expose the port
EXPOSE 5000

# Command to run the app
CMD ["python", "api.py"]
