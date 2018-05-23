import discord
import asyncio
from time import sleep
from random import randint

async def debug(client, message):
    desc = ":exclamation: You have a month left on your quarterly quests. I hope you weren't lazying around Admiral."
    embed = discord.Embed(description=desc, color=discord.Colour(randint(0, 0xffffff)))
    await client.send_message(message.channel, embed=embed)

    sleep(0.5)

    async for m in client.logs_from(message.channel, limit=1):
        print(m.embeds[0])
        print(" ".join(desc.split()[1:]) in m.embeds[0]["description"])