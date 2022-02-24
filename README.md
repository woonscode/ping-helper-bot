# ping-helper-bot
## Background
A simple Telegram bot to ping a URL to check whether it is up.

### Features
* Repeatedly pings a specific URL at fixed intervals
* If response status code is anything other than 200 (website is down), send a Telegram message to relevant personnel
* Deployed through Heroku
    * Environment variable of Telegram Bot Token must be set in config