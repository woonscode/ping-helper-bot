import os
from time import sleep
import requests
from telegram import Bot

TOKEN = os.getenv("TOKEN")
# Set receivers with Telegram Chat ID
CHAT_ID = 0


bot = Bot(TOKEN)
alive = False

while(True):
    try:
        # Set url to ping
        response = requests.head("")
        if response.status_code == 200:
            alive = True
        else:
            alive = False
    except:
        alive = False
    
    if not(alive):
        message = "WEBSITE DOWN!!!"
        bot.send_message(CHAT_ID, message)

    # Customise how long to ping in seconds
    sleep(30)