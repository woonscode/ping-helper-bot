import os
from time import sleep
import requests
from telegram import Bot

TOKEN = os.getenv("TOKEN")
# CHAT_ID = os.getenv("chat_id")

CHAT_ID = 145382580

bot = Bot(TOKEN)
alive = False

while(True):
    try:
        # Set url to ping
        response = requests.head("http://cyclink-env.eba-pvekmnpz.ap-southeast-1.elasticbeanstalk.com/")
        if response.status_code == 200:
            alive = True
        else:
            alive = False
    except:
        alive = False
    
    if not(alive):
        message = "WEBSITE DOWN!!!"
        bot.send_message(CHAT_ID, message)

    # Customise how long to ping
    sleep(30)