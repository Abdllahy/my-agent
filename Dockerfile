FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Cloud Run uses
EXPOSE 8080

# Run the Flask app
CMD ["python", "main.py"]
