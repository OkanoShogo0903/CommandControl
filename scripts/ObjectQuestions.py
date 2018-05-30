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
        # call one's own function
        #$objq = How many {category} are there?
        'pattern':[re.compile(r'How many (?P<category>\w+) are there', re.IGNORECASE)],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.HowManyObjAreThere,\
    },\
    {\
        # TODO color
        # call one's own function
        #$objq = What's the color of the {kname}?
        'pattern':[re.compile(r"(?:What's)|(?:What is) the color of the (?P<name>\w+)", re.IGNORECASE)],\
        'pattern_variable':{'name':'color'},\
        'text':'color is $color',\
        'callback':behavior.customTalk,\
    },\
    {\
        # TODO some tag
        # call one's own function
        #$objq = How many ({category} | names) are in the {placement}?
        'pattern':[re.compile(r'How many (?P<category>\w+) are in the (?P<name>\w+)', re.IGNORECASE)],\
        #'pattern':re.compile(r'How many (?P<name>\w+) are in the (?P<placement>\w+)', re.IGNORECASE),\
        #'pattern':re.compile(r'How many (?P<category>\w+)|(?P<name>\w+) are in the (?P<placement>\w+)', re.IGNORECASE),\
        #'pattern_variable':{'category':'name'},\
        'text':'',\
        'callback':behavior.HowManyObjAreThere,\
    },\
    {\
        # call one's own function
        #$objq = What names are stored in the {placement}?
        'pattern':[re.compile(r'What names are stored in the (?P<name>\w+)', re.IGNORECASE)],\
        'pattern_variable':{'name':'name'},\
        'text':'it in $name',\
        'callback':behavior.customTalk,\
    },\
    {\
        # TODO multi value
        # * -> defaultLocation
        #$objq = Where can I find the ({name} | {category})?
        #'pattern':[re.compile(r'Where can I find the (?P<name>\w+)|(?P<category>\w+)', re.IGNORECASE)],\
        'pattern':  [re.compile(r'Where can I find the (?P<name>\w+)', re.IGNORECASE),\
                     re.compile(r'Where can I find the (?P<category>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.customTalk,\
    },\
    {\
        # name -> category
        #$objq = What is the category of the {name}?
        'pattern':[re.compile(r'What is the (?P<category>\w+) of the (?P<name>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'category':''},\
        'text':'it in $hoge',\
        'callback':behavior.customTalk,\
    },\
    {\
        # TODO
        # call one's own function (Yes No question)
        #$objq = Do the {name 1} and {name 2} belong to the same category?
        'pattern':[re.compile(r'Do the (?P<name1>\w+) are (?P<name2>\w+) belong to the same category', re.IGNORECASE)],\
        'pattern_variable':{'beacon':'defaultLocation'},\
        'text':'it in $defaultLocation',\
        'callback':behavior.customTalk,\
    },\
    {\
        # call one's own function (Yes No question)
        #$objq = Which is the $adja ({category} | name)?
        #$adja = heaviest | smallest | biggest | lightest
        #'pattern':re.compile(r'Which is the (?:heaviest)|(?:smallest)|(?:biggest)|(?:lightest) (?P<category>\w+)|(?P<name>\w+)', re.IGNORECASE),\
        'pattern':[re.compile(r'Which is the (?P<adja>\w+) (?P<category>\w+)', re.IGNORECASE),\
                    re.compile(r'Which is the (?P<adja>\w+) (?P<name>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        'callback':behavior.PassComparedResult,\
        #'callback':behavior.TwoObjectComparison,\
    },\
    {\
        # call one's own function (Yes No question)
        #$objq = Between the {name 1} and {name 2}, which one is $adjr?
        #$adjr = heavier | smaller | bigger | lighter
        # TODO name1.2 will block by isSimilarRegexpBlock
        'pattern':[re.compile(r'Between the (?P<name1>\w+) and (?P<name2>\w+), which one is (?P<adjr>\w+)', re.IGNORECASE)],\
        #'pattern_variable':{'beacon':'defaultLocation'},\
        #'callback':behavior.TwoObjectComparison,\
        'callback':behavior.PassComparedResult,\
    },\
]
