import json


with open("config.json", mode="r", encoding="utf-8") as cfg:
    data = json.loads(cfg.read())

    TOKEN = data.get("bot_token")
    ADMINS = data.get("admins_id")
    LOGGING_LEVEL = data.get("logging_level")
    DB_CONF = data.get("database")

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
