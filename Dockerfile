FROM python:3.10-slim

# 1. Install system dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip
RUN pip install --upgrade pip

# 3. Set workdir
WORKDIR /app

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy rest of the app
COPY . .

# 6. Set default command (optional)
CMD ["python", "app.py"]
