from WPP_Whatsapp import Create

session = Create(
    session="mybot",
    browser_args=[
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--disable-accelerated-2d-canvas",
        "--no-first-run",
        "--no-zygote",
        "--single-process",
        "--disable-gpu"
    ]
)

client = session.start()

def on_message(message):
    if message.get("body", "").lower() == "!ping":
        client.sendText(message["from"], "Pong 🏓")

client.onMessage(on_message)
