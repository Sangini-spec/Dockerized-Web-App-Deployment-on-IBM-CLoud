# 1. Use official Python image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory in container
WORKDIR /app

# 4. Copy app code to the container
COPY . /app

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Expose port
EXPOSE 8080

# 7. Run the Flask app
CMD ["python", "app.py"]
