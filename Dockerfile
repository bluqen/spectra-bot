FROM python:3.11-slim

# Install chromium
RUN apt-get update && apt-get install -y chromium chromium-driver

# Set chromium path for WPP_Whatsapp
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# Install python deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY . .

CMD ["python", "main.py"]
