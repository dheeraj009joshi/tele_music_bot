import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5204962985:AAFLF35MA6OGWwzj7eghvIzq5sJ6mkwDaKE")
API_ID = int(os.environ.get("API_ID", "5367498"))
API_HASH = os.environ.get("API_HASH", "142d57032467ed5def14ddcf498dcca3")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1757043164"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1816945609 , 2122833329").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://denver:denver@cluster0.bfkmd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
