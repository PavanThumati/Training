FROM python:3.9

WORKDIR /app
COPY . /app/
COPY Kubernetes/flask-ci-cd/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
