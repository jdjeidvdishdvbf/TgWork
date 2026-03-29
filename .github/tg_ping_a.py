import time
import os
import requests

TOKEN = "7361353728:AAHbzfLNjuG8zxatvkCrhVGKWi3MrcTOg-g"
CHAT_ID = "1047092792"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

IP = os.popen("tailscale ip -4 | head -n1").read().strip()
send_message(f"SSH Runner A запущено! SSH: runner@{IP}")

while True:
    ping = os.popen("ping -c 1 google.com").read()
    send_message(f"Ping:\n{ping}")
    time.sleep(30)
