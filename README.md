# Discord SelfBot-ADVANCED

![Discord SelfBot](https://media.discordapp.net/attachments/1104256423669530745/1114104824426942564/image.png?width=1200&height=494)

This is a powerful Discord SelfBot implemented using the Discord.py library. The bot offers a wide range of features and commands to enhance your Discord experience.

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
- **Dataset**: Edits the `data.json` file with new guild and channel IDs and restarts the bot.
- **Delete**: Deletes a specified number of it's own messages from the current channel.
- **Stat**: Changes the bot's status to the specified status.

## Prerequisites

Before running the Discord SelfBot-ADVANCED, ensure you have the following prerequisites installed:

- Python 3.9 or higher
- Discord.py library
- pytz library
- psutil library

## Setup

To set up the Discord SelfBot-ADVANCED, follow these steps:

1. Clone the repository or download the code files.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Get your discord account token.
4. Set the bot token as an environment variable named `token`. (See instructions below on how to obtain your Discord token)
5. Optionally, modify the code to customize the bot's behavior and commands.
6. If you want to host the bot 24/7 on Replit, follow these additional steps:
   - Create a new Replit project and import the code files.
   - Create a `.env` file and set the `token` environment variable with your bot token.
   - Create a new file named `keep_alive.py` and copy the code from the provided `keep_alive.py` file into it.
   - Run the `keep_alive.py` file to start a web server that keeps the bot online.
   - Copy the Replit URL of your project and use it to configure a monitor in UptimeRobot to ping the URL and keep the bot running 24/7 for free.

## Usage

- Use the command prefix `!` to trigger the bot commands in your Discord server.
- Refer to the command descriptions in the code or use the bot's help command for detailed information on each command's functionality.
- If you have set up the voice channel connection feature, the bot will automatically join the specified voice channel upon startup.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Contact

For command requests or additional assistance, you can contact me on Discord: ALT#0540

## License

This project is licensed under the [MIT License](LICENSE).

## How to Obtain Your Discord Token

To obtain your Discord token, you can follow these steps:

1. Open Discord in your web browser and log into your account.
2. Right-click anywhere on the Discord web page and select "Inspect" or "Inspect Element" from the context menu. This will open the browser's Developer Tools.
3. In the Developer Tools window, locate the "Network" tab.
4. Refresh the Discord web page to capture the network requests.
5. Look for a request with the name "science" or "gateway" in the "Name" column. Click on it.
6. In the "Headers" section of the selected request, find the "Authorization" header.
7. The value next to the "Authorization" header is your Discord account token. Keep this token private and do not share it with anyone, as it provides full access to your Discord account.
