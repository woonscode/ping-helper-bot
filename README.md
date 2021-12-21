# ping-helper-bot
## Background
A simple Telegram bot made as a helper in a school project.

### Features
* Repeatedly pings a specific website at fixed intervals
* If response status code is anything other than 200 (website is down), send a Telegram message to relevant personnel
* Deployed through AWS Elastic Beanstalk
    * Environment variable of Telegram Bot Token must be set in config