# Base Python image
FROM python:3.10-slim

# Install Chromium and dependencies
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set environment so WPP_Whatsapp knows where Chrome is
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMIUM_FLAGS="--no-sandbox --disable-dev-shm-usage"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

# Start bot
CMD ["python", "main.py"]
