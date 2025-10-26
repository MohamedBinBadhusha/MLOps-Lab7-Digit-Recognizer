# 1. Base Image
FROM python:3.9-slim

# 2. Working Directory inside the container
WORKDIR /app

# 3. Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all your app files
COPY . .

# 5. Expose port 5000 for Flask
EXPOSE 5000

# 6. Command to run the Flask app
CMD ["python", "app.py"]
