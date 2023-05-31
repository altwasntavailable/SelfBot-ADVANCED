# Discord SelfBot-ADVANCED

This is a Discord bot implemented using the Discord.py library. The bot performs various functions and commands in a Discord server.

## Features

- **Uptime**: Displays the bot's uptime.
- **Whois**: Shows information about a user.
- **Restart**: Restarts the bot.
- **Stop**: Stops the bot.
- **Date**: Displays the current date and time in a specific timezone.
- **Ping**: Displays the bot's latency.
- **Set Activity**: Changes the bot's activity.
- **Record**: Records CPU and memory usage for a specified duration.
- **Voice Channel Connection**: Automatically connects to a specified voice channel on startup if the guild ID and channel ID are provided in the `data.json` file.

## Prerequisites

- Python 3.9 or higher
- Discord.py library
- pytz library
- psutil library

## Setup

1. Clone the repository or download the code files.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a Discord bot and obtain the bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
4. Set the bot token as an environment variable named `token`.
5. Optionally, modify the code to customize the bot's behavior and commands.
6. If you want the bot to automatically connect to a voice channel on startup:
   - Update the `data.json` file with the desired guild ID and channel ID.
7. If you want to host the bot 24/7 on Replit:
   - Create a new Replit project and import the code files.
   - Create a `.env` file and set the `token` environment variable with your bot token.
   - Create a new file named `keep_alive.py` and copy the code from the provided `keep_alive.py` file into it.
   - Run the `keep_alive.py` file to start a web server that keeps the bot online.
   - Copy the Replit URL of your project and use it to configure a monitor in UptimeRobot to ping the URL and keep the bot running 24/7 for free.

## Usage

- Use the command prefix `!` to trigger the bot commands in the server.
- Refer to the command descriptions in the code or bot help command for details on each command's functionality.
- If you have set up the voice channel connection feature, the bot will automatically join the specified voice channel upon startup.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Contact

For command requests or additional assistance, you can contact me on Discord: ALT#0540

## License

This project is licensed under the [MIT License](LICENSE).
