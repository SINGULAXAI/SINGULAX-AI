# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app/main.py"]
