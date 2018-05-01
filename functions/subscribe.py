import discord
import asyncio

from utils.logger import log

subscribe_set = set(["Tryhard"])


"""
toggle_user updates the role of the user invoking it to what he wanted by removing or adding the role

It takes
    the client object of the bot
    the message object, conataining the auther and the actual message
    the choice of the user (this is more convinience really)

It returns nothing
"""
async def toggle_user(client, message, choice):
    # Check if the intersection of the subscribe set and the sevrer roles is not empty, meaning the server contains at least one of the subscriber role
    # If not send the list of currently accepted roles
    if not subscribe_set & set([x.name for x in message.server.roles]):
        desc = "I'm sorry but none of the following roles are available on your server: {}".format(", ".join(list(subscribe_set)))
        embed = discord.Embed(description=desc, color=discord.Colour(0xff0000))
        await client.send_message(message.channel, embed=embed)
        return

    # Create a map of name -> role for convinience
    rolemap = {x.name: x for x in message.server.roles}

    # Find the appropriate role for the server
    for role in subscribe_set:
        if role in rolemap.keys():
            # If choice was "unsubscribe" than remove the role
            if choice == "unsubscribe":
                await client.remove_roles(message.author, rolemap[role])
            # Otherwise add it
            else:
                await client.add_roles(message.author, rolemap[role])

            embed = discord.Embed(description="Your roles got updated.", color=discord.Colour(0x00ff00))
            await client.send_message(message.channel, embed=embed)

            return

