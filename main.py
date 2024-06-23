import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_history = ""

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return 

        self.chat_history += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')

        if self.user in message.mentions:
            try:
                response = await openai.ChatCompletion.acreate(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": self.chat_history + "\nNamsGPT: "}
                    ],
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                message_to_send = response['choices'][0]['message']['content']
                await message.channel.send(message_to_send)
            except openai.error.OpenAIError as e:
                print(f"OpenAI error: {e}")
                self.chat_history = "" 

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
