import re
data = [\
    {\
        'pattern':re.compile(r'what are the colours of the Japanese flag', re.IGNORECASE),\
        'print':'Japanese flag is a red circle centred over white',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'when was invented the B programming language', re.IGNORECASE),\
        'print':'B was developed circa 1969 at Bell Labs',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'What city is the capital of the Japan', re.IGNORECASE),\
        'print':'Tokyo',\
        'date':False,\
        'time':False,\
    },    {\
        'pattern':re.compile(r'When was invented the C programming language', re.IGNORECASE),\
        'print':'C was developed after B in 1972 at Bell Labs',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Open Platform League', re.IGNORECASE),\
        'print':'There is no standard defined for OPL',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r"What's the name of your team", re.IGNORECASE),\
        'print':'Team name is KIT Happy Robot',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Who invented the C programming language', re.IGNORECASE),\
        'print':'Ken Thompson and Dennis Ritchie',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Do you have dreams', re.IGNORECASE),\
        'print':'I dream of Electric Sheep',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Domestic Standard Platform League', re.IGNORECASE),\
        'print':'The Toyota Human Support Robot',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'How many people live in the Japan', re.IGNORECASE),\
        'print':'A little over 80 million',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'What is a Sakura', re.IGNORECASE),\
        'print':'Sakura is the Japanese term for ornamental cherry blossom and its tree',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'What time is it', re.IGNORECASE),\
        'print':'',\
        'date':False,\
        'time':True,\
    },\
    {\
        'pattern':re.compile(r'Which robot is used in the Social Standard Platform League', re.IGNORECASE),\
        'print':'The SoftBank Robotics Pepper',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'What day is today', re.IGNORECASE),\
        'print':'',\
        'date':True,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Who is the emperor of Japan', re.IGNORECASE),\
        'print':'His Majesty Akihito sama is the emperor in Japan since January 7, 1989',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'What is the highest point in Japan', re.IGNORECASE),\
        'print':'The highest point in Japan is Mount Fuji, which reaches 3776m above sea level',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Where does the term computer bug come from', re.IGNORECASE),\
        'print':'From a moth trapped in a relay',\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r"In which city will next year's RoboCup be hosted", re.IGNORECASE),\
        'print':"It hasn't been announced yet",\
        'date':False,\
        'time':False,\
    },\
    {\
        'pattern':re.compile(r'Who invented the first compiler', re.IGNORECASE),\
        'print':'Grace Brewster Murray Hopper invented it',\
        'date':False,\
        'time':False,\
    },\
]
