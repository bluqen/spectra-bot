from flask import Flask
from WPP_Whatsapp import Create

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
    ]
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
    
send("+2349135000629", "YOoooooooo")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
