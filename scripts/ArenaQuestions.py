# -*- coding: utf-8 -*-
'''
; grammar name ArenaQuestions
; grammar tier High

$Main   = $arenaq
$arenaq = Where is the {name} located?
$arenaq = Where is the {name} located?
$arenaq = In which room is the {name}?
$arenaq = In which room is the {name}?
$arenaq = How many doors does the {room} have?
$arenaq = How many ({name} | {name}) are in the {room}?
'''
import sys,os
#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
#print(sys.path.append(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import Behavior

import re
#import os, sys
#print(os.getcwd())
import XmlPerser as xml_data
behavior = Behavior.Behavior()
data = [\
    {\
        # $arenaq = Where is the {name} located?
        #'pattern':re.compile(r'Where is the %s locate'% xml_data.name_pattern, re.IGNORECASE),\
        'pattern':[re.compile(r'Where is the (?P<name>.+) locate', re.IGNORECASE)],\
        'pattern_variable':{'name':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # $arenaq = In which room is the {name}?
        #'pattern':re.compile(r'In which room is the %s'% xml_data.name_pattern, re.IGNORECASE),\
        'pattern':[re.compile(r'In which room is the (?P<name>.+)', re.IGNORECASE)],\
        'pattern_variable':{'name':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # TODO add door number
        # $arenaq = How many doors does the {room} have?
        'pattern':[re.compile(r'How many doors does the (?P<room>.+) have', re.IGNORECASE)],\
        #'pattern_variable':{'name':'room'},\
        'text':'it have $random',\
        'callback':behavior.howManyDoors,\
    },\
    {\
        # $arenaq = How many ({name} | {name}) are in the {room}?
        'pattern':[re.compile(r'How many (?P<name>.+) are in the (?P<room>.+)', re.IGNORECASE)],\
        'text':'',\
        'callback':behavior.howManyObjInTheRoom,\
    },\
]
