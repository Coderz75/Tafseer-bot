import discord
import os
import random
import requests
from keep_alive import keep_alive




client = discord.Client()

greetings = ["Hi", "hi", "hello", "Hello", "Hola", "Welcome", 'A wild', 'just slid into the server', 'Good to see you','Yay you made it', 'just showed up!', "Glad you're here,"]

#seerah

sq = ["Which muslim convert changed the course of muslim history.", "What was the first actual battle that the muslims participated in", 'What was the first surah revealed in the quran', 'Is anything hidden from Allah (3:5)', 'Is there any diety except Allah (swt) (3:6)', "Do disbeleivers seek interpretations of Allah's (swt) devine book that is incorrect and suitable only to themselves (3:7)"]

sa = ["umar", "badr", 'alaq', 'no', 'no', 'no' ]

#transalation

tq = ['وَظَلَّلْنَا', 'عَلَيْكُمُ', 'الْغَمَامَ', 'وَأَنزَلْنَا', ' الْمَنَّ', 'وَالسَّلْوَىٰ', ' كُلُوا', 'مِن', 'طَيِّبَاتِ', 'مَا', 'رَزَقْنَاكُمْ', 'ظَلَمُونَا ', 'وَلَٰكِن', 'كَانُوا', 'أَنفُسَهُمْ', 'يَظْلِمُونَ']

ta = ['and we shaded', 'upon you', 'the clouds', 'and we sent down', 'manna', 'and quails', 'eat', 'from', 'good things','what/not', 'we have provided you', 'they wronged us', 'but', 'they were', 'themselves', 'doing wrong']

qn = 0
q = ''
a = ''
qexists = 0
req = 0
username = ''
lines = ''
al= 0
users = []
points = []
startingValue= '0'
Qtype = ''

def getPoints(username, change):
    global users
    global points
    global startingValue
    try:
         f = open("users.txt",'r',encoding = 'utf-8')
         users = f.readlines()
    finally:
        f.close
    try:
         f = open("points.txt",'r',encoding = 'utf-8')
         points = f.readlines()
    finally:
        f.close
    username = username + '\n'

    if username in users:
        index = users.index(username)
        upoints = int(points[index]) + change
        points[index] = str(upoints) + '\n'
        updateFiles()

    else:
        print('new user')
        users.append(username)
        points.append('0\n')
        updateFiles()

        index = users.index(username)
        upoints = int(points[index].split('/')[0]) + change
        points[index] = str(upoints) + '\n'
        updateFiles()  

    print(users)
    print(points)
    return upoints

def updateFiles():
    global points
    global users
    try:
        f = open("points.txt",'w',encoding = 'utf-8')
        for element in points:
            f.write(str(element))
    finally:
        f.close
    try:
        f = open("users.txt",'w',encoding = 'utf-8')
        for element in users:
            f.write(str(element))
    finally:
        f.close


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    print("Tafseer bot: Ready for action")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global qn
    global q
    global a
    global qexists
    global req
    global username
    global al
    global Qtype

    username = message.author.name
    msg = message.content
    
    if any(word in msg for word in greetings):
        await message.channel.send("Hello! I am tafseer bot. i am this server's bot. Type .help in #bot-commands to learn more about me")

    if msg.startswith(".q"):
        await message.channel.send('fetching question...')
        if msg == '.q seerah':
            qn = random.randint(0, len(sq)-1)
            q = sq[qn]
            a = sa[qn]
            qexists = 1
            Qtype= 'seerah'
        elif msg == '.q trans':
            al = 0
            qn = random.randint(0, len(tq)-1)
            q = 'What does ' + tq[qn] + ' mean'
            a = ta[qn]
            if '/' in a:
                a= a.split('/')
                al= 1
            qexists = 1
            Qtype = 'trans'
        else:
            await message.channel.send('Invalid subject. please type .q [subject]')
            q = ''
        await message.channel.send(q+'? Please type your answer in lowercase (to simplify the work i have to do)')
    if msg.startswith('.a'):
        if qexists == 1:
            if al != 1:
                if msg == '.a ' + a:
                    await message.add_reaction("\N{Brain}")
                    if Qtype == 'seerah':
                        points = getPoints(username, 1)
                    else:
                        points = getPoints(username, 2)
                    await message.channel.send('Correct! Nice job. You have now ' + str(points) + ' points.' )
                else:
                    await message.add_reaction("\N{Slightly Frowning Face}")
                    await message.channel.send('Incorrect, the correct answer was: ' + str(a))
                
            else:
                msg = msg.split('.a ')[1]
                if msg in a:
                    await message.add_reaction("\N{Brain}")
                    points = getPoints(username, 2)
                    await message.channel.send('Correct! Nice job. You have now ' + str(points) + ' points.' )  
                else:
                    await message.add_reaction("\N{Slightly Frowning Face}")
                    await message.channel.send('Incorrect, the correct answer was: ' + str(a))
                al = 0
            qexists = 0
        else:
            await message.channel.send('There is no current question. call it by typing .q [topic]. Type in .help for more help')

    if message.content.strip() ==".help":
        helptxt = """
**Tafseer bot**
Hello! I am Tafseer bot. I help in keeping your brain fresh by askingg you questions! How plesent, right?

**My Current topics:**
:book:: .q seerah
Arabic :arrow_forward: English: .q trans (transalation)

to answer, just type .a [answer]

To see how many points you have, type .points

I should stay online 24/7, but if I don't, message my creator (in the about me section)

**About me:**
I am a bot built by Nuaym #5039 on nsyed_nha. My source code could be found here: <https://github.com/Coderz75/Tafseer-bot/> (The variable TOKEM is not defined on github) My license can be found here: https://github.com/Coderz75/Tafseer-bot/blob/main/LICENSE.
Did you know my point storge system in universal? SO that means you can use me here, and on the server!. Just type in .q [topic] to get started!
        """
        await message.add_reaction("\N{Thumbs Up Sign}")
        await message.author.send(helptxt)
    
    req = requests.get("https://discord.com/api/path/to/the/endpoint")
    print(req)
    
    if 'Ur Mom' in msg or "ur mom" in msg or "Ur mom" in msg:
        await message.channel.send('Tu muy estupido')   

    if '.points' in msg:
        points = getPoints(username,0) 
        await message.channel.send('You have: ' + str(points) + ' points')


keep_alive()
client.run(os.getenv("TOKEN"))
