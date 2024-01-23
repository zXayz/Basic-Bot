# 🤖 Basic Bot 
[![Basic Bot](https://img.shields.io/badge/Basic-Bot-purple)](https://github.com/zXayz/basic-bot.git)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-brightgreen)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)


## Overview

Basic Bot is a simple Discord bot built using the discord.py library. It provides essential functionalities and serves as a starting point for further customization and development.

## Features

- **Prefix Command**: Change the bot's command prefix easily.
- **Basic Command**: Includes a sample command (`!hello`) for testing.
- **Customizable**: Easy to extend and add more commands.

## Requirements

- Python 3.6 or higher
- discord.py library (`pip install discord.py`)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/zXayz/basic-bot.git
   cd basic-bot
   ```
2. **Install Dependencies:**
   ```bash
   pip install requirements.txt
   ```
3. **Create a Bot on Discord Developer Portal:**
    - Go to Discord **[Developer Portal](https://discord.com/developers/applications)**.
    - Create a new application.
    - Navigate to the "Bot" tab and click "Add Bot."
    - Copy the token for later use.
4. **Configure the Bot:**
    - Create a **`.env`** file in the project root.
    - Add your bot token to the .env file:
    ```python
    TOKEN = "your_bot_token_here"
    DEFAULT_PREFIX = "!"
    ENVIRONMENT = "development" # or "production" if it is.
    ```
    - Replace your_bot_token_here with the actual token from the Discord **[Developer Portal](https://discord.com/developers/applications)**.
5. **Run the Bot:**
    ```bash
    python bot.py | python3 bot.py
    ```
6. **Invite the Bot to Your Server:**
    - Go back to the Discord **[Developer Portal](https://discord.com/developers/applications)**.
    - In the "OAuth2" tab, under "OAuth2 URL Generator," select the bot and applications.commands scopes.
    - Copy the generated URL and open it in your browser.Authorize the bot to join your server.
## Usage
> Once the bot is invited to your server and running, use the specified command prefix (default is !) to interact with the bot.

- Try the sample command:
    ```bash
    !hello
    ```
## Contributing
Contributions are welcome! If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.
## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.


