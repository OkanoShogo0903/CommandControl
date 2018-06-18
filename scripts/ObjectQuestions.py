# -*- coding: utf-8 -*-
'''
; grammar name ObjectQuestions
; grammar tier High

No1
$Main = $objq
# object -> defaultLocation
$objq = Where can I find the {object}?

No2
# call one's own function
$objq = How many {category} are there?

No3
# call one's own function
$objq = What's the color of the {kobject}?

No4
# call one's own function
$objq = How many ({category} | objects) are in the {placement}?

No5
# call one's own function
$objq = What objects are stored in the {placement}?

No6
# * -> defaultLocation
$objq = Where can I find the ({object} | {category})?

No7
# object -> category
$objq = What is the category of the {object}?

No8
# call one's own function (Yes No question)
$objq = Do the {object 1} and {object 2} belong to the same category?

No9
# call one's own function (Yes No question)
$objq = Which is the $adja ({category} | object)?
$adja = heaviest | smallest | biggest | lightest

No10
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
        #No1 & 6
        #$objq = Where can I find the ({name} | {category})?
        'pattern':  [\
            re.compile(r'find the (?P<name>.+)', re.IGNORECASE),\
            re.compile(r'find the (?P<category>.+)', re.IGNORECASE),\
        ],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'you can find in $defaultLocation',\
        'callback':behavior.customTalk,\
    },\
    {\
        # No2
        #[warning] SPRの部屋にあるカテゴリーをすべて読み上げるようにしている
        #$objq = How many {category} are there?
        'pattern':[\
            re.compile(r'many (?P<category>.+) are there', re.IGNORECASE),\
        ],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'$defaultLocation object are there',\
        'callback':behavior.howManyCategoryAreThere,\
    },\
    {\
        # No3
        #$objq = What's the color of the {kname}?
        'pattern':[\
            re.compile(r"color of the (?P<name>.+)", re.IGNORECASE),\
            re.compile(r"color of the (?P<name>\w+)", re.IGNORECASE),\
        ],\
        'pattern_variable':{'name':'color'},\
        'text':"Object's color is $color",\
        'callback':behavior.customTalk,\
    },\
    {\
        #No4
        #$objq = How many ({category} | names) are in the {placement}?
        'pattern':[\
            re.compile(r'many (?P<category>.+) are in the (?P<name>.+)', re.IGNORECASE),\
            re.compile(r'many (?P<category>.+) are in the (?P<name>\w+)', re.IGNORECASE),\
            re.compile(r'many (?P<name1>.+) are in the (?P<name2>.+)', re.IGNORECASE),\
            re.compile(r'many (?P<name1>.+) are in the (?P<name2>\w+)', re.IGNORECASE),\
            ],\
            #re.compile(r'How many (?P<name>(?:\w+ ){1,256})are in the (?P<room>(?:\w+(?: |$)){1,256})', re.IGNORECASE)] # same to $arenaq = How many ({name} | {name}) are in the {room}?
        'text':'',\
        'callback':behavior.howManyObjInThePlacement,\
    },\
    {\
        #No5
        #$objq = What names are stored in the {placement}?
        #$objq = What objects are stored in the {placement}?
        'pattern':[\
                re.compile(r'store in the (?P<name>.+)', re.IGNORECASE),\
                re.compile(r'store in the (?P<name>\w+)', re.IGNORECASE),\
                re.compile(r'stored in the (?P<name>.+)', re.IGNORECASE),\
                re.compile(r'stored in the (?P<name>\w+)', re.IGNORECASE),\
            ],\
        #'pattern_variable':{'room':'name'},\
        'text':'it in $name',\
        'callback':behavior.whatNames,\
    },\
    # No1 equal No6
    {\
        #No7
        # name -> category
        #$objq = What is the category of the {name}?
        'pattern':[\
            re.compile(r'category of the (?P<name>.+)', re.IGNORECASE),\
            re.compile(r'category of the (?P<name>\w+)', re.IGNORECASE),\
        ],\
        #'pattern_variable':{'category':''},\
        'text':'category is $category',\
        'callback':behavior.customTalk,\
    },\
    {\
        #No8
        # call one's own function (Yes No question)
        #$objq = Do the {name 1} and {name 2} belong to the same category?
        'pattern':[\
            re.compile(r'the (?P<name1>.+) and (?P<name2>.+) b', re.IGNORECASE),\
        ],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.belongToSameCategory,\
    },\
    {\
        #No9-1
        #$objq = Which is the $adja ({category} | name)?
        #$adja = heaviest | smallest | biggest | lightest
        'pattern':[\
            re.compile(r'the (?P<adja>\w+) (?P<category>.+)', re.IGNORECASE),\
        ],\
        'callback':behavior.whichIsTheCompare,\
        #'callback':behavior.TwoObjectComparison,\
    },\
    {\
        #No9-2
        #$objq = Which is the $adja ({category} | name)?
        #$adja = heaviest | smallest | biggest | lightest
        'pattern':[re.compile(r'the (?P<adja>\w+) o', re.IGNORECASE)],\
        'callback':behavior.whichIsTheMost,\
        #'callback':behavior.TwoObjectComparison,\
    },\
    {\
        #No10
        # call one's own function (Yes No question)
        #$objq = Between the {name 1} and {name 2}, which one is $adjr?
        #$adjr = heavier | smaller | bigger | lighter
        # I give priority to speed. ;)
        'pattern':[\
                re.compile(r'the (?P<name1>.+) and (?P<name2>.+), which one is (?P<adjr>\w+)', re.IGNORECASE),\
                re.compile(r'the (?P<name1>.+) and (?P<name2>.+) which one is (?P<adjr>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'callback':behavior.twoObjectComparison,\
    },\
]
