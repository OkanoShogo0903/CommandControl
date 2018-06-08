# -*- coding: utf-8 -*-
# grammar name PredefinedQuestions
# grammar tier Easy
import re
import datetime
import Behavior
behavior = Behavior.Behavior()
data = [\
    {\
        'pattern':[re.compile(r"(What's)|(What is) the name of your team", re.IGNORECASE)],\
        'text':'My team name is K I T happy robot',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'What time is it', re.IGNORECASE)],\
        'callback':behavior.TalkTime,\
    },\
    {\
        'pattern':[re.compile(r'What day is today', re.IGNORECASE)],\
        'callback':behavior.TalkToday,\
    },\
#--------------------------------------------------->
    {\
        'pattern':[re.compile(r'Who invented the C programming language', re.IGNORECASE)],\
        'text':'Ken Thompson and Dennis Ritchie',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'When was the C programming language invented', re.IGNORECASE)],\
        'text':'C was developed after B in 1972 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'When was the B programming language invented', re.IGNORECASE)],\
        'text':'B was developed circa 1969 at Bell Labs',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Where does the term computer bug come from', re.IGNORECASE)],\
        'text':'From a moth trapped in a relay',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Who invented the first compiler', re.IGNORECASE)],\
        'text':'Grace Brewster Murray Hopper invented it',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Which robot is used in the Open Platform League', re.IGNORECASE)],\
        'text':'There is no standard defined for OPL',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Which robot is used in the Domestic Standard Platform League', re.IGNORECASE)],\
        'text':'The Toyota Human Support Robot',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Which robot is used in the Social Standard Platform League', re.IGNORECASE)],\
        'text':'The SoftBank Robotics Pepper',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'Do you have dreams', re.IGNORECASE)],\
        'text':'I dream of Electric Sheep',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r"In which city will next year's RoboCup be hosted", re.IGNORECASE)],\
        'text':"It hasn't been announced yet",\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'What is the origin of the name Canada', re.IGNORECASE)],\
        'text':'The name Canada comes from the Iroquois word Kanata, meaning village or settlement',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'What is the capital of Canada', re.IGNORECASE)],\
        'text':'The capital of Canada is Ottawa',\
        'callback':behavior.Talk,\
    },\
    {\
        'pattern':[re.compile(r'What is the national anthem of Canada', re.IGNORECASE)],\
        'text':'O Canada',\
        'callback':behavior.Talk,\
    },\
]
