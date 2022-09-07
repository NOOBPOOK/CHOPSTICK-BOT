import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio
import asyncpraw
import youtube_dl

intents=nextcord.Intents(messages = True, message_content=True, guilds = True, voice_states = True, members=True)
client = commands.Bot(command_prefix="&", help_command=None, intents=intents)
m9 = 0
m2 = 0
n9 = 0
n2 = 0
time = 0
gameover = True

@client.command()
async def ctest(ctx, po:nextcord.Member, pk:nextcord.Member):
    global gameover
    if gameover and po != await client.fetch_user(981550864479178872) and pk != await client.fetch_user(981550864479178872):
        global m9
        global m2    
        global n9  
        global n2
        global p9_but
        global p2_but
        global p9_memb
        global p2_memb
        global p9
        global p2
        global time
        gameover = False
        p9 = po
        p2 = pk
        m9 = 1
        m2 = 1
        n9 = 1
        n2 = 1
        time = 0
        await ctx.reply(f"Chopstick game between {p9.mention} and {p2.mention}!")
        await player1(ctx)
        p9_embed = nextcord.Embed(title = f"**{p9}**", description="Let's use your brains and ruin someone's friendship!", color = 0xffff00)
        p9_embed.set_thumbnail(url = f"{p9.display_avatar}")
        p9_embed.add_field(name="Detailed Values of all the Hands of bot the players!", value = f"**Your Left Hand:{m9}\nYour Right Hand:{m2}\nPlayer2 Left Hand:{n9}\nPlayer2 Right Hand:{n2}**")
        p9_memb = await ctx.send(embed=p9_embed)
        p2_but = await ctx.send("**Waiting for Player2 Turn!!**")
        p2_embed = nextcord.Embed(title = f"**{p2}**", description="Let's use your brains and ruin someone's friendship!", color = 0xffff00)
        p2_embed.set_thumbnail(url = f"{p2.display_avatar}")
        p2_embed.add_field(name="Detailed Values of all the Hands of bot the players!", value = f"**Your Left Hand:{n9}\nYour Right Hand:{n2}\nPlayer1 Left Hand:{m9}\nPlayer1 Right Hand:{m2}**")
        p2_memb = await ctx.send(embed=p2_embed)
        
        while True:
            if gameover == False:
                await asyncio.sleep(1)
                time+=1
            else:
                break
    else:
        await ctx.reply(f"A Game is already being played between {p9.mention} and {p2.mention}!")
  
async def player1(ctx): #Chose the hand to attack Player1
    global m9
    global m2
    global p9_but
    button1 = Button(label="Left Hand", style=nextcord.ButtonStyle.blurple, emoji="👈")  
    button2 = Button(label="Right Hand", style=nextcord.ButtonStyle.blurple, emoji="👉")
    view = View(timeout = 100)
    if m9<5:
        view.add_item(button1)
    if m2<5:
        view.add_item(button2)
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            await player101()
    button1.callback = button_callback
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            await player102()
    button2.callback = button_callback
    p9_but = await ctx.send("For Player 1!", view = view)
    
async def player11(): #Chose the hand to attack Player1
    global m9
    global m2
    global p9_but
    button1 = Button(label="Left Hand", style=nextcord.ButtonStyle.blurple, emoji="👈")  
    button2 = Button(label="Right Hand", style=nextcord.ButtonStyle.blurple, emoji="👉")
    view = View(timeout = 100)
    if m9<5:
        view.add_item(button1)
    if m2<5:
        view.add_item(button2)
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            await player101()
    button1.callback = button_callback
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            await player102()
    button2.callback = button_callback
    await p9_but.edit("For Player 1!", view = view)
        
async def player101():#Left Hand attack with Player1
    global m9
    global m2
    global n9
    global n2
    global p9_but
    global button1
    global button2
    global button3
    global view
    
    button1 = Button(label = "Left Hand", style=nextcord.ButtonStyle.danger, emoji="👈")
    button2 = Button(label = "Right Hand", style=nextcord.ButtonStyle.danger, emoji="👉")
    button3 = Button(label = "Your Second Hand", style=nextcord.ButtonStyle.green, emoji="👋")
    view = View(timeout = 100)
    if n9<5:
        view.add_item(button1)
    if n2<5:
        view.add_item(button2)
    if m2<5:
        view.add_item(button3)
    
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global n9
            global m9
            global button1
            global button2
            global button3
            global view
            n9+=m9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button1.callback = button_callback
                  
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global n2
            global m9
            global button1
            global button2
            global button3
            global view
            n2+=m9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button2.callback = button_callback
    
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global m2
            global m9
            global button1
            global button2
            global button3
            global view
            m2+=m9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button3.callback = button_callback
        
    await p9_but.edit("**Left hand** What do you choose?", view = view)
        
async def player102():#Right hand attack with Player1
    global m9
    global m2
    global n9
    global n2
    global p9_but
    global button1
    global button2
    global button3
    global view
    button1 = Button(label = "Left Hand", style=nextcord.ButtonStyle.danger, emoji="👈")
    button2 = Button(label = "Right Hand", style=nextcord.ButtonStyle.danger, emoji="👉")
    button3 = Button(label = "Your Second Hand", style=nextcord.ButtonStyle.green, emoji="👋")
    view = View(timeout=100)
    if n9<5:
        view.add_item(button1)
    if n2<5:
        view.add_item(button2)
    if m9<5:
        view.add_item(button3)
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global n9
            global m2
            global view
            global button1
            global button2
            global button3
            n9+=m2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button1.callback = button_callback
    
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global n2
            global m2
            global view
            global button1
            global button2
            global button3
            n2+=m2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button2.callback = button_callback
    
    async def button_callback(interaction):
        global p9
        if interaction.user == p9:
            global m9
            global m2
            global view
            global button1
            global button2
            global button3
            m9+=m2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p9_emb()
            await p2_emb()
            await gameplay1()
    button3.callback = button_callback
    
    await p9_but.edit("**Right Hand** Whom do you want to choose?", view = view)
        
async def player2():#chose the hand to attack player2
    global n9
    global n2
    global p2_but
    button1 = Button(label="Left Hand", style=nextcord.ButtonStyle.blurple, emoji="👈")
    button2 = Button(label="Right Hand", style=nextcord.ButtonStyle.blurple, emoji="👉")
    view = View(timeout=100)
    if n9<5:
        view.add_item(button1)
    if n2<5:
        view.add_item(button2)
        
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            await player201()
    button1.callback = button_callback 
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            await player202()
    button2.callback = button_callback
    
    await p2_but.edit("For Player 2!", view = view)

async def player201():#left hand attack with player2
    global m9
    global m2
    global n9
    global n2
    global p2_but
    global button1
    global button2
    global button3
    global view
    
    button1 = Button(label = "Left Hand", style=nextcord.ButtonStyle.danger, emoji="👈")
    button2 = Button(label = "Right Hand", style=nextcord.ButtonStyle.danger, emoji="👉")
    button3 = Button(label = "Your Second Hand", style=nextcord.ButtonStyle.green, emoji="👋")
    view = View()
    if m9<5:
        view.add_item(button1)
    if m2<5:
        view.add_item(button2)
    if n2<5:
        view.add_item(button3)
    
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n9
            global m9
            global button1
            global button2
            global button3
            global view
            m9+=n9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button1.callback = button_callback
    
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n9
            global m2
            global button1
            global button2
            global button3
            global view
            m2+=n9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button2.callback = button_callback

    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n2
            global n9
            global button1
            global button2
            global button3
            global view
            n2+=n9
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button3.callback = button_callback
    
    await p2_but.edit("**Left Hand** Whom do choose to give?", view = view)
        
async def player202():#right hand attack with player2
    global m9
    global m2
    global n9
    global n2
    global p2_but
    global button1
    global button2
    global button3
    global view
    
    button1 = Button(label = "Left Hand", style=nextcord.ButtonStyle.danger, emoji="👈")
    button2 = Button(label = "Right Hand", style=nextcord.ButtonStyle.danger, emoji="👉")
    button3 = Button(label = "Your Second Hand", style=nextcord.ButtonStyle.green, emoji="👋")
    view = View(timeout=100)
    if m9<5:
        view.add_item(button1)
    if m2<5:
        view.add_item(button2)
    if n9<5:
        view.add_item(button3)
    
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n2
            global m9
            global button1
            global button2
            global button3
            global view
            m9+=n2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button1.callback = button_callback    
    
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n2
            global m2
            global button1
            global button2
            global button3
            global view
            m2+=n2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button2.callback = button_callback
    
    async def button_callback(interaction):
        global p2
        if interaction.user == p2:
            global n2
            global n9
            global button1
            global button2
            global button3
            global view
            n9+=n2
            button1.disabled = True
            button2.disabled = True
            button3.disabled = True
            await interaction.response.edit_message(view = view)
            await p2_emb()
            await p9_emb()
            await gameplay2()
    button3.callback = button_callback
    await p2_but.edit("**Right Hand** Whom do you want to choose?", view = view)
        
async def p9_emb():
    global m9
    global m2    
    global n9  
    global n2
    global p9
    global p2
    global p9_embed
    p9_embed = nextcord.Embed(title = f"**{p9}**", description="Let's use your brains and ruin someone's friendship!", color = 0xffff00)
    p9_embed.set_thumbnail(url = f"{p9.display_avatar}")
    p9_embed.add_field(name="Detailed Values of all the Hands of bot the players!", value = f"**Your Left Hand:{m9}\nYour Right Hand:{m2}\nPlayer2 Left Hand:{n9}\nPlayer2 Right Hand:{n2}**")
    await p9_memb.edit(embed=p9_embed)
    
async def p2_emb():
    global m9
    global m2    
    global n9  
    global n2
    global p9
    global p2
    global p2_memb
    p2_embed = nextcord.Embed(title = f"**{p2}**", description="Let's use your brains and ruin someone's friendship!", color = 0xffff00)
    p2_embed.set_thumbnail(url = f"{p2.display_avatar}")
    p2_embed.add_field(name="Detailed Values of all the Hands of bot the players!", value = f"**Your Left Hand:{n9}\nYour Right Hand:{n2}\nPlayer1 Left Hand:{m9}\nPlayer1 Right Hand:{m2}**")
    await p2_memb.edit(embed=p2_embed)
    
async def gameplay1():
    global m9
    global m2
    global n2
    global n9
    global gameover
    if m9>=5 and m2>=5:
        gameover = True
        await win_p2()
    elif n2>=5 and n9>=5:
        gameover = True
        await win_p9()
    else:
        await player2()
    
async def gameplay2():
    global m9
    global m2
    global n2
    global n9
    global gameover
    if m9>=5 and m2>=5:
        gameover = True
        await win_p2()
    elif n2>=5 and n9>=5:
        gameover = True
        await win_p9()
    else:
        await player11()
    
async def win_p9():
    global p9_memb
    global p2_memb
    global p2_but
    global p9_but
    global time
    win_emebd = nextcord.Embed(title="**CHOPSTICKS🥢**", description=f"{p9.mention} Wins the Game!🎊🎉", color = 0xffff00)
    win_emebd.set_thumbnail(url = f"{p9.display_avatar}")
    win_emebd.set_footer(text = f"Time taken in seconds: {time}")
    await p9_memb.edit(embed = win_emebd)
    await p2_but.delete()
    loss_emebd = nextcord.Embed(title="**CHOPSTICKS🥢**", description=f"{p2.mention} Losses the Game!💩💩", color = 0xffff00)
    loss_emebd.set_thumbnail(url = f"{p2.display_avatar}")
    loss_emebd.set_footer(text = f"Time taken in seconds: {time}")
    await p2_memb.edit(embed = loss_emebd)
    await p9_but.delete()

async def win_p2():
    global p9_memb
    global p2_memb
    global p2_but
    global p9_but
    global time
    win_emebd = nextcord.Embed(title="**CHOPSTICKS🥢**", description=f"{p2.mention} Wins the Game!🎊🎉", color = 0xffff00)
    win_emebd.set_thumbnail(url = f"{p2.display_avatar}")
    win_emebd.set_footer(text = f"Time taken in seconds: {time}")
    await p2_memb.edit(embed = win_emebd)
    await p2_but.delete()
    loss_emebd = nextcord.Embed(title="**CHOPSTICKS🥢**", description=f"{p9.mention} Losses the Game!💩💩", color = 0xffff00)
    loss_emebd.set_thumbnail(url = f"{p9.display_avatar}")
    loss_emebd.set_footer(text = f"Time taken in seconds: {time}")
    await p9_memb.edit(embed = loss_emebd)
    await p9_but.delete()
        
@client.command()
async def endgame(ctx):
    global gameover
    global p9
    global p2
    if ctx.author == p2 or ctx.author == p9:
        gameover = True
        num = random.randint(1,2)
        if num == 1:
            await win_p9()
        elif num == 2:
            await win_p2()
    else:
        ctx.reply("You can't end the game if you haven't started one!")
        
@client.command()
async def help(ctx):
    help_emb = nextcord.Embed(title = "**CHOPSTICKS🥢**", description = "Here are the cmds to play the game!!" , color =  0xe91e63)
    help_emb.add_field(name = "**🤖COMMANDS🤖**", value = "1.")
    
client.run("*******BOT-TOKEN*******")
