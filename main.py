import discord
import datetime
from discord.ext import commands
from topics import topic_selector, concept_selector
from practice import question_answer, question_len

TOKEN = 'MTA4ODA4MjUzMzAxMjQ3NjAxNQ.G7idng.2vJ0OmHgYjxp_RyjIWE3v4ZR8mEoZEAUPmcGIM'
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.',intents=intents)
subject=''
topic_selected = ''
ptype = ''

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

class practice_type(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="MCQs", style=discord.ButtonStyle.blurple)
    async def bio_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global ptype
        ptype='Mcq'
        await interaction.response.send_message(f"To begin `{topic_selected} {ptype}`, type `.start`")

    @discord.ui.button(label="Fill In Blanks", style=discord.ButtonStyle.blurple)
    async def chem_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global ptype
        ptype='Fill_in_blank'
        await interaction.response.send_message(f"To begin `{topic_selected} {ptype}`, type `.start`")
    
    @discord.ui.button(label="Flashcards", style=discord.ButtonStyle.blurple)
    async def his_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global ptype
        ptype = "Flashcards"
        await interaction.response.send_message(f"To begin `{topic_selected} {ptype}`, type `.start`")

class subjectSelector(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Biology", style=discord.ButtonStyle.grey)
    async def bio_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global subject
        subject='Biology'
        await interaction.response.send_message(f"{subject} was choosen for practice, type `.topics`")

    @discord.ui.button(label="Chemistry", style=discord.ButtonStyle.grey)
    async def chem_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global subject
        subject='Chemistry'
        await interaction.response.send_message(f"{subject} was choosen for practice, type `.topics`")
    
    @discord.ui.button(label="History", style=discord.ButtonStyle.grey)
    async def his_btn(self,interaction: discord.Interaction, button: discord.ui.Button ):
        global subject
        subject = "History"
        await interaction.response.send_message(f"{subject} was choosen for practice, type `.topics`")
        
@client.command()
async def practice(ctx):
    view = subjectSelector()
    embedVar = discord.Embed(title="Practice", description="Select your practice type", color=0x4287f5)
    await ctx.channel.send(embed=embedVar, view=view)
    
@client.command()
async def topics(ctx):
    index=0
    for topic in topic_selector(subject):
        index+=1
        await ctx.channel.send(f"**{str(index)})** {topic}")
        
    await ctx.channel.send("Select topics listed above, type `.select_topic (topic no.)`")

@client.command()
async def select_topic(ctx, topic_number):
    global topic_selected
    topic_selected=concept_selector(subject, int(topic_number))
    await ctx.channel.send(f"You have selected `{str(topic_selected)}`, type `.ptype` to view options.")
    
@client.command()
async def ptype(ctx):
    view = practice_type()
    embedVar = discord.Embed(title=topic_selected, description="Choose Practice Type", color=0x4287f5)
    await ctx.channel.send(embed=embedVar, view=view)

question_number = 1

@client.command()
async def start(ctx):
    if ptype == "Mcq":
        for i in range(1, question_len(subject,topic_selected,ptype)+1):
            question_number=i
            question_ans=question_answer(subject,topic_selected,ptype,question_number)
            question=question_ans[0]
            
            await ctx.channel.send(f"**{question}**")
            
            for option in range(1,5):
                await ctx.channel.send(question_ans[option])
            
client.run(TOKEN)