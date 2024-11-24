# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 10000

# Command to start the ASGI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
