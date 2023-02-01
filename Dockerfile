# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the local code into the container at /app
COPY . /app

# Install the required packages
RUN pip install flask

# Set the environment variable to allow Flask to run
ENV FLASK_APP=app.py

# Set the environment variable for LOG_FILE_PATH as required by app.py
ENV LOG_FILE_PATH /app/access.log

# Expose port 5001 to allow connections to the Flask app
EXPOSE 5001

# Set the entrypoint to run the Flask app
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
