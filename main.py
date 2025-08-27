from flask import Flask
from WPP_Whatsapp import Create

import asyncio
from playwright.__main__ import main as playwright_main

# Ensure chromium is installed (downloads to /.cache/ms-playwright)
asyncio.get_event_loop().run_until_complete(asyncio.create_subprocess_exec("playwright", "install", "chromium"))


app = Flask(__name__)

# Create WhatsApp client
session = Create(
    session="mybot",
    browser_args=[
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--disable-accelerated-2d-canvas",
        "--no-first-run",
        "--no-zygote",
        "--single-process"
    ],
    executablePath="/opt/render/project/.cache/ms-playwright/chromium/chrome-linux/chrome"
)

client = session.start()

@app.route("/")
def home():
    return "WPP_Whatsapp bot running on Render!"

@app.route("/send/<number>/<message>")
def send(number, message):
    try:
        client.sendText(f"{number}@c.us", message)
        return f"Sent to {number}"
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
