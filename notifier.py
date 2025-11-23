import requests
import time

BOT_TOKEN = "8396010863:AAGMs2uhN-5cBPjb2ME66fPQDHHSGAGZuU"
CHAT_ID = 8438499114
USERNAME = "nba"

API_URL = f"https://api.tiktokv.com/aweme/v1/aweme/post/?user_id={USERNAME}&count=1"

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

last_video = None

while True:
    try:
        r = requests.get(API_URL, timeout=10).json()
        video = r["aweme_list"][0]["aweme_id"]

        if last_video is None:
            last_video = video
        
        elif video != last_video:
            last_video = video
            link = f"https://www.tiktok.com/@{USERNAME}/video/{video}"
            send(f"New TikTok posted!\n{link}")

    except Exception as e:
        print("Error:", e)

    time.sleep(20)
