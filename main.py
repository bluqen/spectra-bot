from flask import Flask
from WPP_Whatsapp import Create
from flask import Flask
import threading

# Initialize session
session_name = "tagall_bot"
creator = Create(session=session_name)
client = creator.start()


if creator.state != 'CONNECTED':
    raise Exception(f"Failed to connect: {creator.state}")

def on_message(message):
    if message.get("isGroupMsg") and message.get("body", "").strip().lower() == "!tag":
        group_id = message.get("from")  

        # ✅ Get members safely
        ids = client.getGroupMembersIds(group_id) or []
        print("RAW IDS:", ids)

        mentions_text = "📣 Tagging everyone:\n"
        mentions = []

        for member in ids:
            if not member:
                continue

            # Each member is a dict like {'server': 'lid', 'user': '...', '_serialized': '...@lid'}
            user_id = member.get("_serialized")
            if not user_id:
                continue

            # Display just the number (remove server part)
            display_name = user_id.split("@")[0]

            mentions_text += f"@{display_name} "
            mentions.append(user_id)

        # ✅ Send mentions
        client.sendMentioned(group_id, mentions_text.strip(), mentions)



# Listen for incoming messages
creator.client.onMessage(on_message)


# Flask server for Render uptime
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# Run Flask in background thread
threading.Thread(target=run_flask).start()