# AntiBadSubs
![AntiBadSubs logo](https://i.vgy.me/c1SzTV.png)

Discord bot for removing bad subs sent by users.

This bot will try to read every message sent into the server that the bot is present in and then delete a message if it contains a link that either matches or its embed matches the AntiBadSubs blacklist.

---

## Note

The bot is still in early stages, so the code isn't that clean or optimized. I'm also not that great at Python. If you would like to help out, feel free to fork the project, make pull requests, and all that good stuff! I'm also actively looking out for contributors who can help.

## Invite bot

>The bot server is currently undergoing testing, so invites are only available to servers that already have the bot present for now as well as those who ask. The production version is currently hosted on a garbage Google Cloud server. The bot also has a limit of 100 servers as imposed by Discord.

1. Invite to the server using the link.
2. Limit the bot only to channels that you would like by limiting the bot's view permissions using your server settings. Or let it read all the channels, your choice.

## Commands
The prefix is `abs!` for all commands.

- `help` - Get a list of all commands
- `about` - Get more info about the bot.
- `list` - Get the global spreadsheet of channels that are blacklisted.
- `invite` - Get the invite link of the bot to invite it to your server. Please note that the bot only has a limit of 100 servers and is undergoing testing phase.

## Build and run

1. Clone the repo to your server or local machine.
2. Run `installer.py`. This will install the prerequisites, create the database, and create your token file.
3. The installer will ask you for your token. Please use the Discord Developer Portal to get your bot token and insert it here.
4. After running the installer, you can run `main.py`. This is the main bot process.

## Prerequisites
The bot will require several of these Python packages:

- discord (Discord.py)
- python-dotenv (for environment vairables, token storage)
- pandas (because i'm too lazy to figure out csv reading)

The installer will install these packages for you.

## Permissions required

Scopes:

- bot

Bot permissions:

- Read Messages/View Channels
- Send Messages
- Send Messages in Threads
- Manage Messages
- Embed Links
- Attach Files
- Read Message History

## Known bugs
- There's currently a bug where the first video embed will not be detected by the bot. After sending the first video link, the bot will proceed to work as normal.

## Warranty

I cannot be held liable should the bot end up deleting the wrong messages or not properly deleting messages. You are granting the ability for the bot to read and delete messages, and you should be careful with this permission. If you encounter an issue with the bot, do not hesitate to contact me as soon as possible in order to resolve the issue.

## Credits

- Special thanks to [Ryu1845](https://github.com/Ryu1845) for their original `delete_otak` Python Discord bot that is part of the core code for this bot. The original repository for it can be found here: https://github.com/Ryu1845/delete_otak
- Thanks to my friends for helping test the bot in its various stages of development as well as giving advice throughout. Y'all know who you are.