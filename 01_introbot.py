# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


# Even though you can be pretty confident at this point in the tutorial that your bot is only connected
# to a single guild (so client.guilds[0] would be simpler), it’s important to realize that a bot user can
# be connected to many guilds. Therefore, a more robust solution is to loop through client.guilds to find
# the one you’re looking for.


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)