# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY math_ops.py . /app
COPY test_math_ops.py . /app

# Set the command to run the unit tests
CMD [ "pytest" ,  "test_math_ops.py"]