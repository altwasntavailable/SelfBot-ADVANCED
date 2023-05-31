# Discord SelfBot

This is a Discord bot implemented using the discord.py library. The bot has various commands and events to perform actions in a Discord server.

## Prerequisites

- Python 3.8 or higher
- discord.py library (`pip install discord.py`)
- pytz library (`pip install pytz`)

## Setup

1. Clone this repository or download the code files.

2. Install the required libraries using the command:
pip install -r requirements.txt

3. Create a file named `.env` in the project directory and add the following line to it:
token=YOUR_DISCORD_BOT_TOKEN

Replace `token` with your Discord bot token. If you don't have a bot token, you can create a bot and obtain the token from the Discord Developer Portal.

## Usage

1. Open the command prompt or terminal and navigate to the project directory.

2. Start the bot using the command:
python bot.py

3. The bot should now be online and ready to respond to commands in the Discord server.

## Commands

- `!uptime`: Shows the uptime of the bot.

- `!whois [mention]`: Shows information about a mentioned user. If no user is mentioned, it shows information about the command invoker.

- `!restart`: Restarts the bot.

- `!stop`: Stops the bot.

- `!date`: Shows the current date and time in the GMT+1 timezone.

- `!ping`: Measures the latency of the bot.

- `!seta [activity_type] [activity_name]`: Sets the bot's activity. Valid activity types are "playing" and "listening".

## Events

- `on_ready`: Triggered when the bot is logged in and ready to use. It sets the bot's activity and connects to a voice channel if the data is available.

- `on_message`: Triggered when a message is sent. It checks if the bot is mentioned and replies accordingly if enough time has passed since the last mention.

## Miscellaneous

- `keep_alive.py`: A separate file that keeps the bot alive by running a web server. It's used to prevent the bot from sleeping due to inactivity on free hosting platforms.

- `data.json`: A JSON file used to store the guild and channel IDs for voice channel connection. Update this file with the desired guild and channel IDs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
