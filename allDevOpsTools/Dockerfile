# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the app folder first (this helps with caching dependencies)
COPY allDevOpsTools/requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the application port
EXPOSE 5000

# Run the app when the container starts
#CMD ["python", "flaskApp.py"]
CMD sleep 60 && python flaskApp.py
