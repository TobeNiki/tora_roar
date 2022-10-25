import discord
import config

bot = discord.Bot()

@bot.slash_command()
async def hello (ctx, name:str = None):
    name = name or ctx.author.name
    await ctx.respond(f"heelo {name}!")


@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run(config.load_token())