# -*- coding: utf-8 -*-
# grammar name PredefinedQuestions
# grammar tier Easy
import re
import datetime
import Behavior
behavior = Behavior.Behavior()
data = [\
    {\
        'pattern':re.compile(r'what are the colours of the Japanese flag', re.IGNORECASE),\
        'text':'Japanese flag is a red circle centred over white',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'when was invented the B programming language', re.IGNORECASE),\
        'text':'B was developed circa 1969 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'What city is the capital of the Japan', re.IGNORECASE),\
        'text':'Tokyo',\
        'callback':behavior.Talk,\
    },
    {\
        'pattern':re.compile(r'When was invented the C programming language', re.IGNORECASE),\
        'text':'C was developed after B in 1972 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Open Platform League', re.IGNORECASE),\
        'text':'There is no standard defined for OPL',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r"What's the name of your team", re.IGNORECASE),\
        'text':'Team name is KIT Happy Robot',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Who invented the C programming language', re.IGNORECASE),\
        'text':'Ken Thompson and Dennis Ritchie',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Do you have dreams', re.IGNORECASE),\
        'text':'I dream of Electric Sheep',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Domestic Standard Platform League', re.IGNORECASE),\
        'text':'The Toyota Human Support Robot',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'How many people live in the Japan', re.IGNORECASE),\
        'text':'A little over 80 million',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'What is a Sakura', re.IGNORECASE),\
        'text':'Sakura is the Japanese term for ornamental cherry blossom and its tree',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Social Standard Platform League', re.IGNORECASE),\
        'text':'The SoftBank Robotics Pepper',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Who is the emperor of Japan', re.IGNORECASE),\
        'text':'His Majesty Akihito sama is the emperor in Japan since January 7, 1989',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'What is the highest point in Japan', re.IGNORECASE),\
        'text':'The highest point in Japan is Mount Fuji, which reaches 3776m above sea level',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Where does the term computer bug come from', re.IGNORECASE),\
        'text':'From a moth trapped in a relay',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r"In which city will next year's RoboCup be hosted", re.IGNORECASE),\
        'text':"It hasn't been announced yet",\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'Who invented the first compiler', re.IGNORECASE),\
        'text':'Grace Brewster Murray Hopper invented it',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':re.compile(r'What time is it', re.IGNORECASE),\
        'callback':behavior.TalkTime,\
    },\
    {\
        'pattern':re.compile(r'What day is today', re.IGNORECASE),\
        'callback':behavior.TalkToday,\
    },\
]
