FROM python:3.10-slim

WORKDIR /app

# Required system dependencies for pycairo + ffmpeg
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    pkg-config \
    libcairo2-dev \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash", "start.sh"]
