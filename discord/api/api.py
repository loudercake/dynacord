import json
import requests

from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

class API:
    def __init__(self) -> None:
        self._url = "https://discord.com/api/v10"
        self._headers = {
            "Authorization": f"Bot {token}"
        }

    def send_message(self, channel_id: str, msg: str):
        message = {
            'content': msg
        }
        print(requests.post(f"{self._url}/channels/{channel_id}/messages", json=message, headers=self._headers).content)

if __name__ == "__main__":
    api = API()
    api.send_message("1278151925946126360", "a")
