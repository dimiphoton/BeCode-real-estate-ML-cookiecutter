# Use the official Python image as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory into the working directory
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the Flask app to listen on port 5000
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
