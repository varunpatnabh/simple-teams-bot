from flask import Flask, request, Response
import asyncio

from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity

app = Flask(__name__)

# =========================
# 🔐 HARDCODED CREDENTIALS
# =========================
APP_ID = "78caff69-dfc9-4d13-9d42-1a1ac010cca8"
APP_PASSWORD = "Mvi8Q~hthqiSvZrmqI41cOmCJzZPaWjkKJdm_a1x"

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)


# =========================
# 🤖 BOT LOGIC
# =========================
async def handle_message(turn_context: TurnContext):
    await turn_context.send_activity("Hello from Teams bot 👋")


# =========================
# 📩 BOT ENDPOINT
# =========================
@app.route("/api/messages", methods=["POST"])
def messages():
    try:
        body = request.json
        activity = Activity().deserialize(body)
        auth_header = request.headers.get("Authorization", "")

        async def aux_func(turn_context):
            await handle_message(turn_context)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            adapter.process_activity(activity, auth_header, aux_func)
        )
        loop.close()

        return Response(status=201)

    except Exception as e:
        print("ERROR:", str(e))
        return Response("Error", status=500)


# =========================
# 🏠 HEALTH CHECK
# =========================
@app.route("/")
def home():
    return "Bot running 🚀"
