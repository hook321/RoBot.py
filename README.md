# RoBot.py
The FRC Discord Bot, now with 100% more snakes

## Invite
https://discordapp.com/oauth2/authorize?client_id={client_id}&scope=bot&permissions=402779143 (need to find client id)

## Development Setup
1. *Recommended*: [create your own application](https://discordapp.com/developers/applications/me/) with bot account for testing
1. Install dependencies: `sudo apt-get install libxml2 libxslt-dev python3-lxml && sudo pip3 install discord.py requests aiohttp bs4`
1. Create authentication file (`auth.txt`): first line is token, second line is owner account ID
1. Run: `python3 bot.py`
