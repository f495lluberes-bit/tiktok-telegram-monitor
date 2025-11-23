import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"    # MUST BE STRING
USERNAME = "nba"

# STEP 1 — Convert username → user_id
USER_LOOKUP_URL = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/profile/other/?unique_id={USERNAME}"

try:
    user_data = requests.get(USER_LOOKUP_URL, timeout=10).json()
    USER_ID = user_data["user_info"]["uid"]
except Exception as e:
    raise SystemExit(f"Could not get user_id for {USERNAME}: {e}")

API_URL = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/aweme/post/?user_id={USER_ID}&count=1"

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
        send(f"Error: {e}")

    time.sleep(20)

