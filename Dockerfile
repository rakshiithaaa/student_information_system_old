# Dockerfile
FROM python:3.10-slim

# 1) Install only pip and update it
RUN pip install --upgrade pip

WORKDIR /app

# 2) Copy and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy the rest of your app
COPY . .

EXPOSE 5000
ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
