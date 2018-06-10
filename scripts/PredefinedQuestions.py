# -*- coding: utf-8 -*-
# grammar name PredefinedQuestions
# grammar tier Easy
import re
import datetime
import Behavior
behavior = Behavior.Behavior()
data = [\
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
