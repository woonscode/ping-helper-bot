import os
from time import sleep
import requests
from telegram import Bot

TOKEN = os.getenv("TOKEN")
# Set receivers with Telegram Chat ID
# My ID
CHAT_ID_1 = 145382580
# Other ID
# CHAT_ID_2 = 171328604


bot = Bot(TOKEN)
alive = False

while(True):
    try:
        # Set url to ping
        response = requests.head("http://ec2-54-179-230-30.ap-southeast-1.compute.amazonaws.com/")
        if response.status_code == 200:
            alive = True
        else:
            alive = False
    except:
        alive = False
    
    if not(alive):
        message = "WEBSITE DOWN!!!"
        bot.send_message(CHAT_ID_1, message)
    else:
        message = "website up yo"
        bot.send_message(CHAT_ID_1, message)

    # Customise how long to ping in seconds
    sleep(30)