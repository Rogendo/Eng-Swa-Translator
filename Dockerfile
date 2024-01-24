# Use a lightweight Python base image
FROM python:3.10.12

# Set a working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set the environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]