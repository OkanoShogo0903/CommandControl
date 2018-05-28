# -*- coding: utf-8 -*-
'''
; grammar name ArenaQuestions
; grammar tier High

$Main   = $arenaq
$arenaq = Where is the {placement} located?
$arenaq = Where is the {beacon} located?
$arenaq = In which room is the {placement}?
$arenaq = In which room is the {beacon}?
$arenaq = How many doors does the {room} have?
$arenaq = How many ({placement} | {beacon}) are in the {room}?
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
        # $arenaq = Where is the {placement} located?
        #'pattern':re.compile(r'Where is the %s locate'% xml_data.placement_pattern, re.IGNORECASE),\
        'pattern':re.compile(r'Where is the (?P<placement>\w+) locate', re.IGNORECASE),\
        'pattern_variable':{'placement':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # $arenaq = Where is the {beacon} located?
        'pattern':re.compile(r'Where is the (?P<beacon>\w+) locate', re.IGNORECASE),\
        'pattern_variable':{'beacon':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # $arenaq = In which room is the {placement}?
        #'pattern':re.compile(r'In which room is the %s'% xml_data.placement_pattern, re.IGNORECASE),\
        'pattern':re.compile(r'In which room is the (?P<placement>\w+)', re.IGNORECASE),\
        'pattern_variable':{'placement':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # $arenaq = In which room is the {beacon}?
        #'pattern':re.compile(r'In which room is the %s'% xml_data.beacon_pattern, re.IGNORECASE),\
        'pattern':re.compile(r'In which room is the (?P<beacon>\w+)', re.IGNORECASE),\
        'pattern_variable':{'beacon':'room'},\
        'text':'it in $room',\
        'callback':behavior.customTalk,\
    },\
    {\
        # $arenaq = How many doors does the {room} have?
        'pattern':re.compile(r'How many doors does the (?P<beacon>\w+) have', re.IGNORECASE),\
        #'pattern_variable':{'beacon':'room'},\
        'text':'it have $random',\
        'callback':behavior.HowManyObjInTheRoom,\
    },\
    {\
        # $arenaq = How many ({placement} | {beacon}) are in the {room}?
        'pattern':re.compile(r'How many ((?P<placement>\w+)|(?P<beacon>\w+)) are in the (?P<room>\w+)', re.IGNORECASE),\
        'text':'',\
        'callback':behavior.HowManyObjInTheRoom,\
    },\
]
