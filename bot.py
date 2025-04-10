import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from code_analysis import roast_code_file
from valorant_stats import roast_val_stats
from utils.roles import get_role_roast

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"ValRoaster is live and judging.")

@bot.command()
async def roast(ctx, role=None):
    if role:
        await ctx.send(get_role_roast(role))
    else:
        await ctx.send(get_random_insult())
        
@bot.command()
async def analyze_code(ctx):
    await ctx.send("Upload your code file. Let’s see how broken it is.")
    def check(m):
        return m.author == ctx.author and m.attachments
    msg = await bot.wait_for('message', timeout=30.0, check=check)
    file = msg.attachments[0]
    content = await file.read()
    result = roast_code_file(content.decode('utf-8'))
    await ctx.send(result)

@bot.command()
async def valorant(ctx, *, riot_id):
    await ctx.send(await roast_val_stats(riot_id))

bot.run(TOKEN)
