# -*- coding: utf-8 -*-
# grammar name PredefinedQuestions
# grammar tier Easy
import re
import datetime
import Behavior
behavior = Behavior.Behavior()
data = [\
    {\
# Which was the first computer with a hard disk drive?    The IBM 305 RAMAC.
        'textbook_sentence':"Which was the first computer with a hard disk drive",\
        'pattern':[\
            re.compile(r"Which was the first computer", re.IGNORECASE),\
        ],\
        'text':"The I B M 305 R A M A C",\
        'callback':behavior.Talk,\
    },\
    {\
# Which program do Jedi use to open PDF files?    Adobe Wan Kenobi
        'textbook_sentence':"Which program do Jedi use to open PDF files",\
        'pattern':[\
            re.compile(r"which program", re.IGNORECASE),\
            re.compile(r"program do", re.IGNORECASE),\
            re.compile(r"Jedi", re.IGNORECASE),\
            re.compile(r"PDF", re.IGNORECASE),\
        ],\
        'text':'Adobe Wan Kenobi',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Who's the most handsome person in Canada? I know that Justin Trudeau is very handsome
    {\
        'textbook_sentence':"Who's the most handsome person in Canada",\
        'pattern':[\
            re.compile(r"handsome", re.IGNORECASE),\
            re.compile(r"person in", re.IGNORECASE),\
        ],\
        'text':'I know that Justin Trudeau is very handsome',\
        'callback':behavior.Talk,\
    },\
    {\
# Who coined the term Beatlemania? Sandy Gardiner, a journalist of the Ottawa Journal
        'textbook_sentence':"Who coined the term Beatlemania",\
        'pattern':[\
            re.compile(r"coined", re.IGNORECASE),\
            re.compile(r"Beatlemania", re.IGNORECASE),\
        ],\
        'text':'Sandy Gardiner, a journalist of the Ottawa Journal',\
        'callback':behavior.Talk,\
    },\
    {\
# Who invented the compiler?  Grace Hoper. She wrote it in her spare time.
        'textbook_sentence':"Who invented the compiler",\
        'pattern':[\
            re.compile(r"invented", re.IGNORECASE),\
        ],\
        'text':'Grace Hoper. She wrote it in her spare time',\
        'callback':behavior.Talk,\
    },\
    {\
# Who created the C Programming Language?     C was invented by Dennis MacAlistair Ritchie.
        'textbook_sentence':"Who created the C Programming Language",\
        'pattern':[\
            re.compile(r"C Programming Language", re.IGNORECASE),\
        ],\
        'text':'C was invented by Dennis MacAlistair Ritchie',\
        'callback':behavior.Talk,\
    },\
    {\
# Who created the Python Programming Language?    Python was invented by Guido van Rossum.
        'textbook_sentence':"Who created the Python Programming Language",\
        'pattern':[\
            re.compile(r"Python", re.IGNORECASE),\
        ],\
        'text':'Python was invented by Guido van Rossum',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is the inventor of the Apple I microcomputer?   My lord and master Steve Wozniak.
        'textbook_sentence':"Who is the inventor of the Apple I microcomputer",\
        'pattern':[\
            re.compile(r"inventor", re.IGNORECASE),\
            re.compile(r"microcomputer", re.IGNORECASE),\
        ],\
        'text':'My lord and master Steve Wozniak',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is considered to be the first computer programmer?  Ada Lovelace.
        'textbook_sentence':"Who is considered to be the first computer programmer",\
        'pattern':[\
            re.compile(r"considered", re.IGNORECASE),\
            re.compile(r"to be the", re.IGNORECASE),\
            re.compile(r"first computer programmer", re.IGNORECASE),\
        ],\
        'text':'Ada Lovelace',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is the world's first android?   Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.
        'textbook_sentence':"Who is the world's first android",\
        'pattern':[\
            re.compile(r"Who is the", re.IGNORECASE),\
            re.compile(r"android", re.IGNORECASE),\
        ],\
        'text':'Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# What's the longest street in the world?     Yonge Street in Ontario is the longest street in the world.
    {\
        'textbook_sentence':"What's the longest street in the world",\
        'pattern':[\
            re.compile(r"longest street", re.IGNORECASE),\
            re.compile(r"What's the longest street in the world", re.IGNORECASE),\
        ],\
        'text':'Yonge Street in Ontario is the longest street in the world',\
        'callback':behavior.Talk,\
    },\
    {\
# What's the name of the bear cub exported from Canada to the London Zoo in 1915?     The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh.
        'textbook_sentence':"What's the name of the bear cub exported from Canada to the London Zoo in 1915",\
        'pattern':[\
            re.compile(r"bear", re.IGNORECASE),\
            re.compile(r"cub", re.IGNORECASE),\
            re.compile(r"exported", re.IGNORECASE),\
            re.compile(r"London", re.IGNORECASE),\
            re.compile(r"Zoo", re.IGNORECASE),\
            re.compile(r"1915", re.IGNORECASE),\
        ],\
        'text':'The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh',\
        'callback':behavior.Talk,\
    },\
    {\
# What's the origin of the Comic Sans font?   Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books.
        'textbook_sentence':"What's the origin of the Comic Sans font",\
        'pattern':[\
            re.compile(r"origin", re.IGNORECASE),\
            re.compile(r"Comic", re.IGNORECASE),\
            re.compile(r"Sans", re.IGNORECASE),\
            re.compile(r"font", re.IGNORECASE),\
        ],\
        'text':"Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books",\
        'callback':behavior.Talk,\
    },\
    {\
# What is the world's largest coin?   The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.
        'textbook_sentence':"What is the world's largest coin",\
        'pattern':[\
            re.compile(r"largest coin", re.IGNORECASE),\
        ],\
        'text':'The Big Nickel in Sudbury, Ontario. It is nine meters in diameter',\
        'callback':behavior.Talk,\
    },\
    {\
# What is a nanobot?  The smallest robot possible is called a nanobot.
        'textbook_sentence':"What is a nanobot",\
        'pattern':[\
            re.compile(r"is a nanobot", re.IGNORECASE),\
        ],\
        'text':'The smallest robot possible is called a nanobot',\
        'callback':behavior.Talk,\
    },\
    {\
# What is a Mechanical Knight?    A robot sketch made by Leonardo DaVinci.
        'textbook_sentence':"What is a Mechanical Knight",\
        'pattern':[\
            re.compile(r"Mechanical", re.IGNORECASE),\
            re.compile(r"Knight", re.IGNORECASE),\
            re.compile(r"night", re.IGNORECASE),\
        ],\
        'text':'A robot sketch made by Leonardo DaVinci',\
        'callback':behavior.Talk,\
    },\
    {\
# What is the AI knowledge engineering bottleneck?    It is when you need to load an AI with enough knowledge to start learning.
        'textbook_sentence':"What is the AI knowledge engineering bottleneck",\
        'pattern':[\
            re.compile(r"knowledge", re.IGNORECASE),\
            re.compile(r"engineering", re.IGNORECASE),\
            re.compile(r"bottleneck", re.IGNORECASE),\
        ],\
        'text':'It is when you need to load an AI with enough knowledge to start learning',\
        'callback':behavior.Talk,\
    },\
    {\
# What is a chatbot?  A chatbot is an A.I. you put in customer service to avoid paying salaries.
        'textbook_sentence':"What is a chatbot",\
        'pattern':[\
            re.compile(r"chat", re.IGNORECASE),\
        ],\
        'text':'A chatbot is an A.I. you put in customer service to avoid paying salaries',\
        'callback':behavior.Talk,\
    },\
    {\
# What was the first computer bug?    The first actual computer bug was a dead moth stuck in a Harvard Mark II.
        'textbook_sentence':"What was the first computer bug",\
        'pattern':[\
            re.compile(r"first computer bug", re.IGNORECASE),\
            re.compile(r"first computer bank", re.IGNORECASE),\
        ],\
        'text':'The first actual computer bug was a dead moth stuck in a Harvard Mark two',\
        'callback':behavior.Talk,\
    },\
    {\
# What was the first computer to pass the Turing test?    some people think it was ibm watson, but it was eugene, a computer designed at england's university of reading.
        'textbook_sentence':"What was the first computer to pass the Turing test",\
        'pattern':[\
            re.compile(r"the Turing test", re.IGNORECASE),\
            re.compile(r"first computer to", re.IGNORECASE),\
        ],\
        'text':"some people think it was ibm watson, but it was eugene, a computer designed at england's university of reading",\
        'callback':behavior.Talk,\
    },\
    {\
# What does CAPTCHA stands for?   CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart.
        'textbook_sentence':"What does CAPTCHA stands for",\
        'pattern':[\
            re.compile(r"What does c", re.IGNORECASE),\
            re.compile(r"stands for", re.IGNORECASE),\
            re.compile(r"stand for", re.IGNORECASE),\
        ],\
        'text':'CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart',\
        'callback':behavior.Talk,\
    },\
    {\
# What does Moravec's paradox state?  Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.
        'textbook_sentence':"What does Moravec's paradox state",\
        'pattern':[\
            re.compile(r"What does m", re.IGNORECASE),\
            re.compile(r"paradox", re.IGNORECASE),\
            re.compile(r"state", re.IGNORECASE),\
        ],\
        'text':"Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills",\
        'callback':behavior.Talk,\
    },\
# In what year was Canada invaded by the USA for the first time?  The first time that the USA invaded Canada was in 1775
    {\
        'textbook_sentence':"In what year was Canada invaded by the USA for the first time",\
        'pattern':[\
            re.compile(r"In what year", re.IGNORECASE),\
            re.compile(r"for the first time", re.IGNORECASE),\
        ],\
        'text':"The first time that the USA invaded Canada was in 1775",\
        'callback':behavior.Talk,\
    },\
    {\
# What year was Canada invaded by the USA for the second time?    The USA invaded Canada a second time in 1812.
        'textbook_sentence':"What year was Canada invaded by the USA for the second time",\
        'pattern':[\
            re.compile(r"the second time", re.IGNORECASE),\
        ],\
        'text':'The USA invaded Canada a second time in 1812',\
        'callback':behavior.Talk,\
    },\
    {\
# What country holds the record for the most gold medals at the Winter Olympics?  Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.
        'textbook_sentence':"What country holds the record for the most gold medals at the Winter Olympics",\
        'pattern':[\
            re.compile(r"holds", re.IGNORECASE),\
            re.compile(r"country", re.IGNORECASE),\
            re.compile(r"gold medals", re.IGNORECASE),\
            re.compile(r"Winter Olympics", re.IGNORECASE),\
        ],\
        'text':"Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics",\
        'callback':behavior.Talk,\
    },\
    {\
# What else is Montreal called?   Montreal is often called the City of Saints or the City of a Hundred Bell Towers.
        'textbook_sentence':"What else is Montreal called",\
        'pattern':[\
            re.compile(r"What else", re.IGNORECASE),\
            re.compile(r"Montreal call", re.IGNORECASE),\
        ],\
        'text':'Montreal is often called the City of Saints or the City of a Hundred Bell Towers',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# When
    {\
# When was The Mounted Police formed?     The Mounted Police was formed in 1873.
        'textbook_sentence':"When was The Mounted Police formed",\
        'pattern':[\
            re.compile(r"The Mounted Police formed", re.IGNORECASE),\
            re.compile(r"When was The M", re.IGNORECASE),\
        ],\
        'text':"The Mounted Police was formed in 1873",\
        'callback':behavior.Talk,\
    },\
    {\
# When was the first computer with a hard disk drive launched?    The IBM 305 RAMAC was launched in 1956.
        'textbook_sentence':"When was the first computer with a hard disk drive launched",\
        'pattern':[\
            re.compile(r"When was the first", re.IGNORECASE),\
            re.compile(r"disk drive launched", re.IGNORECASE),\
        ],\
        'text':"The IBM 305 RAMAC was launched in 1956",\
        'callback':behavior.Talk,\
    },\
    {\
# When was The Royal Canadian Mounted Police formed?  In 1920, when The Mounted Police merged with the Dominion Police.
        'textbook_sentence':"When was The Royal Canadian Mounted Police formed",\
        'pattern':[\
            re.compile(r"When was The R", re.IGNORECASE),\
            re.compile(r"royal", re.IGNORECASE),\
            re.compile(r"Canadian Mounted", re.IGNORECASE),\
        ],\
        'text':"In 1920, when The Mounted Police merged with the Dominion Police",\
        'callback':behavior.Talk,\
    },\

#--------------------------------------------------->
# Why
    {\
# Why is Canada named Canada?     French explorers misunderstood the local native word "Kanata", which means village.
        'textbook_sentence':"Why is Canada named Canada",\
        'pattern':[\
            re.compile(r"Why is Canada", re.IGNORECASE),\
            re.compile(r"Canada named Canada", re.IGNORECASE),\
            re.compile(r"named Canada", re.IGNORECASE),\
        ],\
        'text':"French explorers misunderstood the local native word 'Kanata', which means village",\
        'callback':behavior.Talk,\
    },\
    {\
# Why wasn't Tron nominated for an award by The Motion Picture Academy?   The Academy thought that Tron cheated by using computers.
        'textbook_sentence':"Why wasn't Tron nominated for an award by The Motion Picture Academy",\
        'pattern':[\
            re.compile(r"Why was", re.IGNORECASE),\
            re.compile(r"Tron nominated", re.IGNORECASE),\
            re.compile(r"Motion Picture", re.IGNORECASE),\
            re.compile(r"Academy", re.IGNORECASE),\
        ],\
        'text':"The Academy thought that Tron cheated by using computers",\
        'callback':behavior.Talk,\
    },\
    {\
# Why is Elon Musk worried about AI's impact on humanity?     I don't know. He should worry more about the people's impact on humanity.
        'textbook_sentence':"Why is Elon Musk worried about AI's impact on humanity",\
        'pattern':[\
            re.compile(r"Elon", re.IGNORECASE),\
            re.compile(r"Musk", re.IGNORECASE),\
            re.compile(r"impact", re.IGNORECASE),\
        ],\
        'text':"I don't know. He should worry more about the people's impact on humanity",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Where
    {\
# Where was the Blackberry Smartphone developed?  It was developed in Ontario, at Research In Motion's Waterloo offices.
        'textbook_sentence':"Where was the Blackberry Smartphone developed",\
        'pattern':[\
            re.compile(r"Blackberry", re.IGNORECASE),\
            re.compile(r"Smartphone", re.IGNORECASE),\
        ],\
        'text':"It was developed in Ontario, at Research In Motion's Waterloo offices",\
        'callback':behavior.Talk,\
    },\
    {\
# Where is The Hotel de Glace located?    The Hotel de Glace is in Quebec.
        'textbook_sentence':"Where is The Hotel de Glace located",\
        'pattern':[\
            re.compile(r"Where is The Hotel", re.IGNORECASE),\
            re.compile(r"why is The Hotel", re.IGNORECASE),\
            re.compile(r"Glace locate", re.IGNORECASE),\
        ],\
        'text':"The Hotel de Glace is in Quebec",\
        'callback':behavior.Talk,\
    },\
    {\
# Where is Canada's only desert?  Canada's only desert is British Columbia.
        'textbook_sentence':"Where is Canada's only desert",\
        'pattern':[\
            re.compile(r"Where is Canada", re.IGNORECASE),\
        ],\
        'text':"Canada's only desert is British Columbia",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# How
    {\
# How many time zones are there in Canada?    Canada spans almost 10 million square km and comprises 6 time zones
        'textbook_sentence':"How many time zones are there in Canada",\
        'pattern':[\
            re.compile(r"How many time zones are there in Canada", re.IGNORECASE),\
            re.compile(r"time zones", re.IGNORECASE),\
        ],\
        'text':"Canada spans almost 10 million square km and comprises 6 time zones",\
        'callback':behavior.Talk,\
    },\
    {\
# How long is Yonge Street in Ontario?    Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border.
        'textbook_sentence':"How long is Yonge Street in Ontario",\
        'pattern':[\
            re.compile(r"How long", re.IGNORECASE),\
        ],\
        'text':"Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border",\
        'callback':behavior.Talk,\
    },\
    {\
# How big is the RCMP?    Today, the RCMP has close to 30,000 members.
        'textbook_sentence':"How big is the R C M P",\
        'pattern':[\
            re.compile(r"How big is the", re.IGNORECASE),\
            re.compile(r"How big was the", re.IGNORECASE),\
            re.compile(r"RCMP", re.IGNORECASE),\
        ],\
        'text':"Today, the RCMP has close to 30,000 members",\
        'callback':behavior.Talk,\
    },\
# How many tons of ice are required to build The Hotel de Glace?  The Hotel de Glace requires about 400 tons of ice.
    {\
        'textbook_sentence':"How many tons of ice are required to build The Hotel de Glace",\
        'pattern':[\
            re.compile(r"How many tons of ice", re.IGNORECASE),\
            re.compile(r"ice are required to build The Hotel de Glace", re.IGNORECASE),\
        ],\
        'text':"The Hotel de Glace requires about 400 tons of ice",\
        'callback':behavior.Talk,\
    },\
# How many tons of snow are required to build The Hotel de Glace?     Every year, 12000 tons of snow are used for The Hotel de Glace.
    {\
        'textbook_sentence':"How many tons of snow are required to build The Hotel de Glace",\
        'pattern':[\
            re.compile(r"How many tons of snow", re.IGNORECASE),\
            re.compile(r"snow are required to build The Hotel de Glace", re.IGNORECASE),\
        ],\
        'text':"Every year, 12000 tons of snow are used for The Hotel de Glace",\
        'callback':behavior.Talk,\
    },\
# How big is Canada's only desert?    The British Columbia desert is only 15 miles long.
    {\
        'textbook_sentence':"How big is Canada's only desert",\
        'pattern':[\
            re.compile(r"How big is Canada", re.IGNORECASE),\
            re.compile(r"Canada's only", re.IGNORECASE),\
        ],\
        'text':"The British Columbia desert is only 15 miles long",\
        'callback':behavior.Talk,\
    },\
# How small can a nanobot be?     A nanobot can be less than one-thousandth of a millimeter.
    {\
        'textbook_sentence':"How small can a nanobot be",\
        'pattern':[\
            re.compile(r"How small", re.IGNORECASE),\
            re.compile(r"nanobot be", re.IGNORECASE),\
        ],\
        'text':"A nanobot can be less than one-thousandth of a millimeter",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Other
    {\
# Can I visit the Hotel de Glace in summer?   No. Every summer it melts away, only to be rebuilt the following winter.
        'textbook_sentence':"Can I visit the Hotel de Glace in summer",\
        'pattern':[\
            re.compile(r"Can I visit", re.IGNORECASE),\
            re.compile(r"visit the", re.IGNORECASE),\
        ],\
        'text':"No. Every summer it melts away, only to be rebuilt the following winter",\
        'callback':behavior.Talk,\
    },\
# Name 3 famous male Canadians.   leonard cohen, keanu reeves, and jim carrey.
    {\
        'textbook_sentence':"Name 3 famous male Canadians",\
        'pattern':[\
            re.compile(r"Name 3 famous male Canadian", re.IGNORECASE),\
            re.compile(r" male Canadian", re.IGNORECASE),\
        ],\
        'text':"Name 3 famous male Canadians",\
        'callback':behavior.Talk,\
    },\
    {\
# Name 3 famous female Canadians.     Celine Dion, Pamela Anderson, and Avril Lavigne.
        'textbook_sentence':"Name 3 famous female Canadians",\
        'pattern':[\
            re.compile(r"Name 3 famous female", re.IGNORECASE),\
            re.compile(r"female Canadian", re.IGNORECASE),\
        ],\
        'text':"Celine Dion, Pamela Anderson, and Avril Lavigne",\
        'callback':behavior.Talk,\
    },\
    {\
# Are self-driving cars safe?     yes. car accidents are product of human misconduct.
        'textbook_sentence':"Are self-driving cars safe",\
        'pattern':[\
            re.compile(r"Are self", re.IGNORECASE),\
            re.compile(r"driving", re.IGNORECASE),\
            re.compile(r"cars safe", re.IGNORECASE),\
            re.compile(r"car safe", re.IGNORECASE),\
        ],\
        'text':"yes. car accidents are product of human misconduct.",\
        'callback':behavior.Talk,\
    },\
    {\
# Is Mark Zuckerberg a robot?     sure. i've never seen him drink water.
        'textbook_sentence':"Is Mark Zuckerberg a robot",\
        'pattern':[\
            re.compile(r"Is Mark", re.IGNORECASE),\
            re.compile(r"Zuckerberg", re.IGNORECASE),\
        ],\
        'text':"sure. i've never seen him drink water",\
        'callback':behavior.Talk,\
    },\
    {\
# Name all of the robots on Mars.     There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.
        'textbook_sentence':"Name all of the robots on Mars",\
        'pattern':[\
            re.compile(r"Name all of", re.IGNORECASE),\
            re.compile(r"on Mars", re.IGNORECASE),\
        ],\
        'text':"There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing",\
        'callback':behavior.Talk,\
    },\
    {\
# Do you think robots are a threat to humanity?   No. Humans are the real threat to humanity.
        'textbook_sentence':"Do you think robots are a threat to humanity",\
        'pattern':[\
            re.compile(r"Do you think", re.IGNORECASE),\
            re.compile(r"threat to", re.IGNORECASE),\
        ],\
        'text':"No. Humans are the real threat to humanity",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
    {\
        # (?:What's)|(?:What is) the name of your team
        'textbook_sentence':"What is the name of your team",\
        'pattern':[\
            re.compile(r"the name of your team", re.IGNORECASE),\
            re.compile(r"team", re.IGNORECASE),\
        ],\
        'text':'My team name is K I T happy robot',\
        'callback':behavior.Talk,\
    },\
    {\
        # What time is it
        'textbook_sentence':"What time is it",\
        'pattern':[\
            re.compile(r'time is it', re.IGNORECASE),\
            re.compile(r'What time', re.IGNORECASE),\
        ],\
        'callback':behavior.TalkTime,\
    },\
    {\
        # What day is today
        'textbook_sentence':"What day is today",\
        'pattern':[\
            re.compile(r'What day', re.IGNORECASE),
            re.compile(r'today', re.IGNORECASE),
        ],\
        'callback':behavior.TalkToday,\
    },\
#--------------------------------------------------->
]
