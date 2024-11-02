# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (including libpango for WeasyPrint)
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    build-essential \
    python3-dev \
    python3-pip \
    libpq-dev

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "resume.wsgi:application"]