<<<<<<< HEAD
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application using uvicorn
=======
# First stage to build the application
FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

# Second stage to run the application
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

EXPOSE 8000

>>>>>>> f0ae657d6e8455067a87cef92b8ffd1a79880ab7
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
