FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY Kubernetes/flask-ci-cd/requirements.txt /app/

# Upgrade pip
#RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Set the command to run your application
CMD ["python", "app.py"]
