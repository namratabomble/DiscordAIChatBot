# DiscordAIChatBot
NamsGPT is a Discord chatbot developed using Python and Discord.py, leveraging OpenAI's GPT-3.5 model for natural language understanding and generative AI responses. 
This bot handles real-time message interactions and enhances user engagement through advanced conversational automation.

# Features

Real-time message handling
Intelligent AI responses
Easy integration and setup

# Tech Stack
Programming Language: Python
Libraries:
discord.py for Discord API interaction
openai for integrating OpenAI's GPT-3.5 model
python-dotenv for managing environment variables

# APIs:
OpenAI API for AI-generated responses
Deployment: Can be deployed on cloud platforms like Heroku, AWS, or Repl.it

# Setup and Installation

Prerequisites

Python 3.7+
Discord account and server
OpenAI API key

## Installation
Clone the repository:

git clone https://github.com/yourusername/namsgpt.git
cd namsgpt

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Set up environment variables:
Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_discord_bot_token

# Usage

Run the bot:
python bot.py

Interact with the bot:
Mention the bot in any message on your Discord server to get a response, e.g.,

On Discord server:

@NamsGPT Hello! How are you?
