import discord
import asyncio

from utils.logger import log

subscribe_set = set(["Tryhard"])

async def toggle_user(client, message, choice):
    if not subscribe_set & set([x.name for x in message.server.roles]):
        desc = "I'm sorry but none of the following roles are available on your server: {}".format(", ".join(list(subscribe_set)))
        embed = discord.Embed(description=desc, color=discord.Colour(0xff0000))
        await client.send_message(message.channel, embed=embed)
        return

    rolemap = {x.name: x for x in message.server.roles}

    for role in subscribe_set:
        if role in rolemap.keys():
            if choice == "unsubscribe":
                await client.remove_roles(message.author, rolemap[role])
            else:
                await client.add_roles(message.author, rolemap[role])

            embed = discord.Embed(description="Your roles got updated.", color=discord.Colour(0x00ff00))
            await client.send_message(message.channel, embed=embed)

            return

