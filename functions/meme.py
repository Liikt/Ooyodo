import discord
import asyncio

from random import randint


"""
maint_meme is a function that when called, sends the zion maintanence meme to the channel of the invoker message

It takes the client object and a message object as arguments

returns nothing
"""
async def maint_meme(client, message):
    embed = discord.Embed(color=discord.Colour(randint(0x0, 0xffffff)))
    embed.set_image(
        url="https://media.discordapp.net/attachments/242858060224135168/466827108396564482/No_5dc4dc9fcee3ff1d1d28a64b0793eb8a.png"
    )

    await client.send_message(message.channel, embed=embed)