from flask import Flask, render_template, request, jsonify
import re

from menu_compression import display_menu
from availability import check_availability
from reservation_handler import reserve_table

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    # 1️⃣ Menu
    if "menu" in user_msg:
        reply = display_menu()

    # 2️⃣ Availability keyword
    elif "availability" in user_msg:
        reply = "📅 Please provide date and time (YYYY-MM-DD HH:MM)"

    # 3️⃣ Reserve keyword
    elif "reserve" in user_msg:
        try:
            parts = user_msg.split()
            date = parts[-2]
            time = parts[-1]

            slots = check_availability(date, time)

            if slots is None:
                reply = "❌ Invalid date or time format."

            elif slots > 0:
                reserve_table(date, time)
                reply = f"✅ Table reserved on {date} at {time}"

            else:
                reply = "❌ Slot full. Try another time."

        except:
            reply = "⚠️ Use format: reserve YYYY-MM-DD HH:MM"

    # 4️⃣ ONLY date & time entered (SMART FIX ✅)
    elif re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", user_msg):
        reply = "❓ Do you want to check availability or reserve?"

    # 5️⃣ Default fallback
    else:
        reply = "🤖 Ask for menu, availability, or reserve a table."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
