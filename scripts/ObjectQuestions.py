# -*- coding: utf-8 -*-
'''
; grammar name ObjectQuestions
; grammar tier High

$Main = $objq
# object -> defaultLocation
$objq = Where can I find the {object}?

# call one's own function
$objq = How many {category} are there?

# call one's own function
$objq = What's the color of the {kobject}?

# call one's own function
$objq = How many ({category} | objects) are in the {placement}?

# call one's own function
$objq = What objects are stored in the {placement}?

# * -> defaultLocation
$objq = Where can I find the ({object} | {category})?

# object -> category
$objq = What is the category of the {object}?

# call one's own function (Yes No question)
$objq = Do the {object 1} and {object 2} belong to the same category?

# call one's own function (Yes No question)
$objq = Which is the $adja ({category} | object)?
$adja = heaviest | smallest | biggest | lightest

# call one's own function (Yes No question)
$objq = Between the {object 1} and {object 2}, which one is $adjr?
$adjr = heavier | smaller | bigger | lighter
'''

import Behavior
import sys,os
import re
import XmlPerser as xml_data

behavior = Behavior.Behavior()
data = [\
    {\
        #[warning] SPRの部屋にあるカテゴリーをすべて読み上げるようにしている
        #$objq = How many {category} are there?
        'pattern':[re.compile(r'How many (?P<category>.+) are there', re.IGNORECASE)],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.howManyCategoryAreThere,\
    },\
    {\
        #$objq = What's the color of the {kname}?
        'pattern':[re.compile(r"(?:What's)|(?:What is) the color of the (?P<name>.+)", re.IGNORECASE)],\
        'pattern_variable':{'name':'color'},\
        'text':'color is $color',\
        'callback':behavior.customTalk,\
    },\
    {\
        #$objq = How many ({category} | names) are in the {placement}?
        'pattern':[\
            re.compile(r'How many (?P<category>.+) are in the (?P<name>.+)', re.IGNORECASE),\
            re.compile(r'How many (?P<name1>.+) are in the (?P<name2>.+)', re.IGNORECASE),\
            ],\
            #re.compile(r'How many (?P<name>(?:\w+ ){1,256})are in the (?P<room>(?:\w+(?: |$)){1,256})', re.IGNORECASE)] # same to $arenaq = How many ({name} | {name}) are in the {room}?
        'text':'',\
        'callback':behavior.howManyObjInThePlacement,\
    },\
    {\
        #$objq = What names are stored in the {placement}?
        'pattern':[\
                re.compile(r'What names are stored in the (?P<name>.+)', re.IGNORECASE)\
            ],\
        'pattern_variable':{'room':'name'},\
        'text':'it in $name',\
        'callback':behavior.whatNames,\
    },\
    {\
        #$objq = Where can I find the ({name} | {category})?
        'pattern':  [re.compile(r'Where can I find the (?P<name>.+)', re.IGNORECASE),\
                     re.compile(r'Where can I find the (?P<category>.+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.customTalk,\
    },\
    {\
        # name -> category
        #$objq = What is the category of the {name}?
        'pattern':[re.compile(r'What is the category of the (?P<name>.+)', re.IGNORECASE)],\
        #'pattern_variable':{'category':''},\
        'text':'it in $category',\
        'callback':behavior.customTalk,\
    },\
    {\
        # TODO
        # call one's own function (Yes No question)
        #$objq = Do the {name 1} and {name 2} belong to the same category?
        'pattern':[re.compile(r'Do the (?P<name1>.+) and (?P<name2>.+) belong to the same category', re.IGNORECASE)],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.belongToSameCategory,\
    },\
    {\
        # call one's own function (Yes No question)
        #$objq = Which is the $adja ({category} | name)?
        #$adja = heaviest | smallest | biggest | lightest
        'pattern':[re.compile(r'Which is the (?P<adja>\w+) (?P<category>.+)', re.IGNORECASE),\
                    re.compile(r'Which is the (?P<adja>\w+) (?P<name>.+)', re.IGNORECASE)],\
        'callback':behavior.whichIsTheCompare,\
        #'callback':behavior.TwoObjectComparison,\
    },\
    {\
        # call one's own function (Yes No question)
        #$objq = Between the {name 1} and {name 2}, which one is $adjr?
        #$adjr = heavier | smaller | bigger | lighter
        # I give priority to speed. ;)
        'pattern':[\
                re.compile(r'Between the (?P<name1>.+) and (?P<name2>.+), which one is (?P<adjr>\w+)', re.IGNORECASE),\
                re.compile(r'Between the (?P<name1>.+) and (?P<name2>.+) which one is (?P<adjr>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'callback':behavior.twoObjectComparison,\
    },\
]
