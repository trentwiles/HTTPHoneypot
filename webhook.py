import requests
import json

def webhook(message):
    requests.post("https://ntfy.sh/" + json.loads(open("config.json").read()["webhook_path"]), data=message)