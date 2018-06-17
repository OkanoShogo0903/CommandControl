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
        'pattern':[\
            re.compile(r"Which was the first computer with a hard disk drive", re.IGNORECASE),\
        ],\
        'text':"The IBM 305 RAMAC",\
        'callback':behavior.Talk,\
    },\
    {\
# Which program do Jedi use to open PDF files?    Adobe Wan Kenobi
        'pattern':[\
            re.compile(r"Which program do Jedi use to open PDF files", re.IGNORECASE),\
        ],\
        'text':'Adobe Wan Kenobi',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Who's the most handsome person in Canada? I know that Justin Trudeau is very handsome
    {\
        'pattern':[\
            re.compile(r"Who's the most handsome person in Canada", re.IGNORECASE),\
        ],\
        'text':'I know that Justin Trudeau is very handsome',\
        'callback':behavior.Talk,\
    },\
    {\
# Who coined the term Beatlemania? Sandy Gardiner, a journalist of the Ottawa Journal
        'pattern':[\
            re.compile(r"Who coined the term Beatlemania", re.IGNORECASE),\
        ],\
        'text':'Sandy Gardiner, a journalist of the Ottawa Journal',\
        'callback':behavior.Talk,\
    },\
    {\
# Who invented the compiler?  Grace Hoper. She wrote it in her spare time.
        'pattern':[\
            re.compile(r"Who invented the compiler", re.IGNORECASE),\
        ],\
        'text':'Grace Hoper. She wrote it in her spare time',\
        'callback':behavior.Talk,\
    },\
    {\
# Who created the C Programming Language?     C was invented by Dennis MacAlistair Ritchie.
        'pattern':[\
            re.compile(r"Who created the C Programming Language", re.IGNORECASE),\
        ],\
        'text':'C was invented by Dennis MacAlistair Ritchie',\
        'callback':behavior.Talk,\
    },\
    {\
# Who created the Python Programming Language?    Python was invented by Guido van Rossum.
        'pattern':[\
            re.compile(r"Who created the Python Programming Language", re.IGNORECASE),\
        ],\
        'text':'Python was invented by Guido van Rossum',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is the inventor of the Apple I microcomputer?   My lord and master Steve Wozniak.
        'pattern':[\
            re.compile(r"Who is the inventor of the Apple I microcomputer", re.IGNORECASE),\
        ],\
        'text':'My lord and master Steve Wozniak',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is considered to be the first computer programmer?  Ada Lovelace.
        'pattern':[\
            re.compile(r"Who is considered to be the first computer programmer", re.IGNORECASE),\
        ],\
        'text':'Ada Lovelace',\
        'callback':behavior.Talk,\
    },\
    {\
# Who is the world's first android?   Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.
        'pattern':[\
            re.compile(r"Who is the world's first android", re.IGNORECASE),\
        ],\
        'text':'Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
#What's the longest street in the world?     Yonge Street in Ontario is the longest street in the world.
    {\
        'pattern':[\
            re.compile(r"What's the longest street in the world", re.IGNORECASE),\
        ],\
        'text':'Yonge Street in Ontario is the longest street in the world',\
        'callback':behavior.Talk,\
    },\
    {\
#What's the name of the bear cub exported from Canada to the London Zoo in 1915?     The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh.
        'pattern':[\
            re.compile(r"What's the name of the bear cub exported from Canada to the London Zoo in 1915", re.IGNORECASE),\
        ],\
        'text':'The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh',\
        'callback':behavior.Talk,\
    },\
    {\
#What's the origin of the Comic Sans font?   Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books.
        'pattern':[\
            re.compile(r"What's the origin of the Comic Sans font", re.IGNORECASE),\
        ],\
        'text':"Comic Sans is based on Dave Gibbons' lettering in the Watchmen comic books",\
        'callback':behavior.Talk,\
    },\
    {\
#What is the world's largest coin?   The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.
        'pattern':[\
            re.compile(r"What is the world's largest coin", re.IGNORECASE),\
        ],\
        'text':'The Big Nickel in Sudbury, Ontario. It is nine meters in diameter',\
        'callback':behavior.Talk,\
    },\
    {\
#What is a nanobot?  The smallest robot possible is called a nanobot.
        'pattern':[\
            re.compile(r"What is a nanobot", re.IGNORECASE),\
        ],\
        'text':'The smallest robot possible is called a nanobot',\
        'callback':behavior.Talk,\
    },\
    {\
# What is a Mechanical Knight?    A robot sketch made by Leonardo DaVinci.
        'pattern':[\
            re.compile(r"What is a Mechanical Knight", re.IGNORECASE),\
        ],\
        'text':'A robot sketch made by Leonardo DaVinci',\
        'callback':behavior.Talk,\
    },\
    {\
#What is the AI knowledge engineering bottleneck?    It is when you need to load an AI with enough knowledge to start learning.
        'pattern':[\
            re.compile(r"What is the AI knowledge engineering bottleneck", re.IGNORECASE),\
        ],\
        'text':'It is when you need to load an AI with enough knowledge to start learning',\
        'callback':behavior.Talk,\
    },\
    {\
#What is a chatbot?  A chatbot is an A.I. you put in customer service to avoid paying salaries.
        'pattern':[\
            re.compile(r"What is a chatbot", re.IGNORECASE),\
        ],\
        'text':'you put in customer service to avoid paying salaries',\
        'callback':behavior.Talk,\
    },\
    {\
#What was the first computer bug?    The first actual computer bug was a dead moth stuck in a Harvard Mark II.
        'pattern':[\
            re.compile(r"What was the first computer bug", re.IGNORECASE),\
        ],\
        'text':'The first actual computer bug was a dead moth stuck in a Harvard Mark two',\
        'callback':behavior.Talk,\
    },\
    {\
#What was the first computer to pass the Turing test?    some people think it was ibm watson, but it was eugene, a computer designed at england's university of reading.
        'pattern':[\
            re.compile(r"What was the first computer to pass the Turing test", re.IGNORECASE),\
        ],\
        'text':"some people think it was ibm watson, but it was eugene, a computer designed at england's university of reading",\
        'callback':behavior.Talk,\
    },\
    {\
#What does CAPTCHA stands for?   CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart.
        'pattern':[\
            re.compile(r"What does CAPTCHA stands for", re.IGNORECASE),\
        ],\
        'text':'CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart',\
        'callback':behavior.Talk,\
    },\
    {\
#What does Moravec's paradox state?  Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.
        'pattern':[\
            re.compile(r"What does Moravec's paradox state", re.IGNORECASE),\
        ],\
        'text':"Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills",\
        'callback':behavior.Talk,\
    },\
    {\
# What year was Canada invaded by the USA for the second time?    The USA invaded Canada a second time in 1812.
        'pattern':[\
            re.compile(r"What year was Canada invaded by the USA for the second time", re.IGNORECASE),\
        ],\
        'text':'The USA invaded Canada a second time in 1812',\
        'callback':behavior.Talk,\
    },\
    {\
# What country holds the record for the most gold medals at the Winter Olympics?  Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.
        'pattern':[\
            re.compile(r"What country holds the record for the most gold medals at the Winter Olympics", re.IGNORECASE),\
        ],\
        'text':"Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics",\
        'callback':behavior.Talk,\
    },\
    {\
# What else is Montreal called?   Montreal is often called the City of Saints or the City of a Hundred Bell Towers.
        'pattern':[\
            re.compile(r"What else is Montreal called", re.IGNORECASE),\
        ],\
        'text':'Montreal is often called the City of Saints or the City of a Hundred Bell Towers',\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# When
    {\
#When was The Mounted Police formed?     The Mounted Police was formed in 1873.
        'pattern':[\
            re.compile(r"When was The Mounted Police formed", re.IGNORECASE),\
        ],\
        'text':"",\
        'callback':behavior.Talk,\
    },\
    {\
#When was the first computer with a hard disk drive launched?    The IBM 305 RAMAC was launched in 1956.
        'pattern':[\
            re.compile(r"When was the first computer with a hard disk drive launched", re.IGNORECASE),\
        ],\
        'text':"The IBM 305 RAMAC was launched in 1956",\
        'callback':behavior.Talk,\
    },\
    {\
#When was The Royal Canadian Mounted Police formed?  In 1920, when The Mounted Police merged with the Dominion Police.
        'pattern':[\
            re.compile(r"When was The Royal Canadian Mounted Police formed", re.IGNORECASE),\
        ],\
        'text':"In 1920, when The Mounted Police merged with the Dominion Police",\
        'callback':behavior.Talk,\
    },\

#--------------------------------------------------->
# Why
    {\
# Why is Canada named Canada?     French explorers misunderstood the local native word "Kanata", which means village.
        'pattern':[\
            re.compile(r"Why is Canada named Canada", re.IGNORECASE),\
        ],\
        'text':"French explorers misunderstood the local native word 'Kanata', which means village",\
        'callback':behavior.Talk,\
    },\
    {\
# Why wasn't Tron nominated for an award by The Motion Picture Academy?   The Academy thought that Tron cheated by using computers.
        'pattern':[\
            re.compile(r"Why wasn't Tron nominated for an award by The Motion Picture Academy", re.IGNORECASE),\
        ],\
        'text':"The Academy thought that Tron cheated by using computers",\
        'callback':behavior.Talk,\
    },\
    {\
# Why is Elon Musk worried about AI's impact on humanity?     I don't know. He should worry more about the people's impact on humanity.
        'pattern':[\
            re.compile(r"Why is Elon Musk worried about AI's impact on humanity", re.IGNORECASE),\
        ],\
        'text':"I don't know. He should worry more about the people's impact on humanity",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Where
    {\
        'pattern':[\
# Where was the Blackberry Smartphone developed?  It was developed in Ontario, at Research In Motion's Waterloo offices.
            re.compile(r"Where was the Blackberry Smartphone developed", re.IGNORECASE),\
        ],\
        'text':"It was developed in Ontario, at Research In Motion's Waterloo offices",\
        'callback':behavior.Talk,\
    },\
    {\
# Where is The Hotel de Glace located?    The Hotel de Glace is in Quebec.
        'pattern':[\
            re.compile(r"Where is The Hotel de Glace located", re.IGNORECASE),\
        ],\
        'text':"The Hotel de Glace is in Quebec",\
        'callback':behavior.Talk,\
    },\
    {\
# Where is Canada's only desert?  Canada's only desert is British Columbia.
        'pattern':[\
            re.compile(r"Where is Canada's only desert", re.IGNORECASE),\
        ],\
        'text':"Canada's only desert is British Columbia",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# How
    {\
# How many time zones are there in Canada?    Canada spans almost 10 million square km and comprises 6 time zones
        'pattern':[\
            re.compile(r"How many time zones are there in Canada", re.IGNORECASE),\
        ],\
        'text':"Canada spans almost 10 million square km and comprises 6 time zones",\
        'callback':behavior.Talk,\
    },\
    {\
# How long is Yonge Street in Ontario?    Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border.
        'pattern':[\
            re.compile(r"How long is Yonge Street in Ontario", re.IGNORECASE),\
        ],\
        'text':"Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border",\
        'callback':behavior.Talk,\
    },\
    {\
# How big is the RCMP?    Today, the RCMP has close to 30,000 members.
        'pattern':[\
            re.compile(r"How big is the RCMP", re.IGNORECASE),\
        ],\
        'text':"Today, the RCMP has close to 30,000 members",\
        'callback':behavior.Talk,\
    },\
# How many tons of ice are required to build The Hotel de Glace?  The Hotel de Glace requires about 400 tons of ice.
    {\
        'pattern':[\
            re.compile(r"How many tons of ice are required to build The Hotel de Glace", re.IGNORECASE),\
        ],\
        'text':"The Hotel de Glace requires about 400 tons of ice",\
        'callback':behavior.Talk,\
    },\
# How many tons of snow are required to build The Hotel de Glace?     Every year, 12000 tons of snow are used for The Hotel de Glace.
    {\
        'pattern':[\
            re.compile(r"How many tons of snow are required to build The Hotel de Glace", re.IGNORECASE),\
        ],\
        'text':"Every year, 12000 tons of snow are used for The Hotel de Glace",\
        'callback':behavior.Talk,\
    },\
# How big is Canada's only desert?    The British Columbia desert is only 15 miles long.
    {\
        'pattern':[\
            re.compile(r"How big is Canada's only desert", re.IGNORECASE),\
        ],\
        'text':"The British Columbia desert is only 15 miles long",\
        'callback':behavior.Talk,\
    },\
# How small can a nanobot be?     A nanobot can be less than one-thousandth of a millimeter.
    {\
        'pattern':[\
            re.compile(r"How small can a nanobot be", re.IGNORECASE),\
        ],\
        'text':"A nanobot can be less than one-thousandth of a millimeter",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
# Other
    {\
# Can I visit the Hotel de Glace in summer?   No. Every summer it melts away, only to be rebuilt the following winter.
        'pattern':[\
            re.compile(r"Can I visit the Hotel de Glace in summer", re.IGNORECASE),\
        ],\
        'text':"No. Every summer it melts away, only to be rebuilt the following winter",\
        'callback':behavior.Talk,\
    },\
# In what year was Canada invaded by the USA for the first time?  The first time that the USA invaded Canada was in 1775
    {\
        'pattern':[\
            re.compile(r"In what year was Canada invaded by the USA for the first time", re.IGNORECASE),\
        ],\
        'text':"The first time that the USA invaded Canada was in 1775",\
        'callback':behavior.Talk,\
    },\
# Name 3 famous male Canadians.   leonard cohen, keanu reeves, and jim carrey.
    {\
        'pattern':[\
            re.compile(r"Name 3 famous male Canadians", re.IGNORECASE),\
        ],\
        'text':"Name 3 famous male Canadians",\
        'callback':behavior.Talk,\
    },\
    {\
# Name 3 famous female Canadians.     Celine Dion, Pamela Anderson, and Avril Lavigne.
        'pattern':[\
            re.compile(r"Name 3 famous female Canadians", re.IGNORECASE),\
        ],\
        'text':"Celine Dion, Pamela Anderson, and Avril Lavigne",\
        'callback':behavior.Talk,\
    },\
    {\
# Are self-driving cars safe?     yes. car accidents are product of human misconduct.
        'pattern':[\
            re.compile(r"Are self-driving cars safe", re.IGNORECASE),\
        ],\
        'text':"Are self-driving cars safe",\
        'callback':behavior.Talk,\
    },\
    {\
# Is Mark Zuckerberg a robot?     sure. i've never seen him drink water.
        'pattern':[\
            re.compile(r"Is Mark Zuckerberg a robot", re.IGNORECASE),\
        ],\
        'text':"sure. i've never seen him drink water",\
        'callback':behavior.Talk,\
    },\
    {\
# Name all of the robots on Mars.     There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.
        'pattern':[\
            re.compile(r"Name all of the robots on Mars", re.IGNORECASE),\
        ],\
        'text':"There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing",\
        'callback':behavior.Talk,\
    },\
    {\
# Do you think robots are a threat to humanity?   No. Humans are the real threat to humanity.
        'pattern':[\
            re.compile(r"Do you think robots are a threat to humanity", re.IGNORECASE),\
        ],\
        'text':"No. Humans are the real threat to humanity",\
        'callback':behavior.Talk,\
    },\
#--------------------------------------------------->
    {\
        # (?:What's)|(?:What is) the name of your team
        'pattern':[\
            re.compile(r"the name of your team", re.IGNORECASE),\
            re.compile(r"team", re.IGNORECASE),\
        ],\
        'text':'My team name is K I T happy robot',\
        'callback':behavior.Talk,\
    },\
    {\
        # What time is it
        'pattern':[\
            re.compile(r'time is it', re.IGNORECASE),\
            re.compile(r'What time', re.IGNORECASE),\
        ],\
        'callback':behavior.TalkTime,\
    },\
    {\
        # What day is today
        'pattern':[\
            re.compile(r'What day', re.IGNORECASE),
            re.compile(r'today', re.IGNORECASE),
        ],\
        'callback':behavior.TalkToday,\
    },\
#--------------------------------------------------->
    {\
        # Who invented the C programming language
        'pattern':[\
            re.compile(r'Who invented the C', re.IGNORECASE),\
            re.compile(r'invented the C ', re.IGNORECASE),\
        ],\
        'text':'Ken Thompson and Dennis Ritchie',\
        'callback':behavior.Talk,\
    },\
    {\
        # When was the C programming language invented
        'pattern':[\
            re.compile(r'When was the C', re.IGNORECASE),\
            re.compile(r'C programming language invented', re.IGNORECASE),\
        ],\
        'text':'C was developed after B in 1972 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        # When was the B programming language invented
        'pattern':[\
            re.compile(r'When was the B', re.IGNORECASE),\
            re.compile(r'B programming', re.IGNORECASE),\
        ],\
        'text':'B was developed circa 1969 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        # Where does the term computer bug come from
        'pattern':[\
            re.compile(r'Where does the term', re.IGNORECASE),\
            re.compile(r'computer bug come from', re.IGNORECASE),\
        ],\
        'text':'From a moth trapped in a relay',\
        'callback':behavior.Talk,\
    },\
    {\
        # Who invented the first compiler
        'pattern':[\
            re.compile(r'Who invented the first', re.IGNORECASE),\
            re.compile(r'the first', re.IGNORECASE),\
        ],\
        'text':'Grace Brewster Murray Hopper invented it',\
        'callback':behavior.Talk,\
    },\
    {\
        # Which robot is used in the Open Platform League
        'pattern':[\
            re.compile(r'Open', re.IGNORECASE),\
        ],\
        'text':'There is no standard defined for OPL',\
        'callback':behavior.Talk,\
    },\
    {\
        # Which robot is used in the Domestic Standard Platform League
        'pattern':[\
            re.compile(r'Domestic', re.IGNORECASE),\
        ],\
        'text':'The Toyota Human Support Robot',\
        'callback':behavior.Talk,\
    },\
    {\
        # Which robot is used in the Social Standard Platform League
        'pattern':[\
            re.compile(r'Social', re.IGNORECASE),\
            re.compile(r'Standard', re.IGNORECASE),\
        ],\
        'text':'The SoftBank Robotics Pepper',\
        'callback':behavior.Talk,\
    },\
    {\
        # Do you have dreams
        'pattern':[\
            re.compile(r'you have', re.IGNORECASE),\
            re.compile(r'dream', re.IGNORECASE),\
        ],\
        'text':'I dream of Electric Sheep',\
        'callback':behavior.Talk,\
    },\
    {\
        # In which city will next year's RoboCup be hosted
        'pattern':[\
            re.compile(r"city", re.IGNORECASE),\
            re.compile(r"next year", re.IGNORECASE),\
            re.compile(r"RoboCup be host", re.IGNORECASE),\
        ],\
        'text':"It hasn't been announced yet",\
        'callback':behavior.Talk,\
    },\
    {\
        # What is the origin of the name Canada
        'pattern':[\
            re.compile(r'What is the origin', re.IGNORECASE),\
            re.compile(r'name Canada', re.IGNORECASE),\
        ],\
        'text':'The name Canada comes from the Iroquois word Kanata, meaning village or settlement',\
        'callback':behavior.Talk,\
    },\
    {\
        # What is the capital of Canada
        'pattern':[\
            re.compile(r'capital', re.IGNORECASE),\
        ],\
        'text':'The capital of Canada is Ottawa',\
        'callback':behavior.Talk,\
    },\
    {\
        # What is the national anthem of Canada
        'pattern':[\
            re.compile(r'anthem of Canada', re.IGNORECASE),\
            re.compile(r'national', re.IGNORECASE),\
        ],\
        'text':'O Canada',\
        'callback':behavior.Talk,\
    },\
]
