# -*- coding: utf-8 -*-
'''
; grammar name CrowdQuestions
; grammar tier High

$Main   = $crowdq
# call one's own function
$crowdq = How many $people are in the crowd?

# ???
$crowdq = How many people in the crowd are ($posppl | {gesture})?

# call one's own function
# equal "How many $people are in the crowd?"
$crowdq = Tell me the number of $people in the crowd

# call one's own function
$crowdq = Was the person $posprs a $gprsng?

# ???
$crowdq = Tell me if the person ($posprs | {gesture}) was a $gprsn?

# ???
$crowdq = Tell me how many people were wearing $color


$people = $appl | $gppl
$appl   = children | adults | elders
$gppl   = males | females | men | women | boys | girls

$posppl = $posprs
$posppl = standing or sitting
$posppl = standing or lying down
$posppl = sitting or lying down
$posprs = standing | sitting | lying down

$gprsn  = male | female | man | woman | boy | girl
$gprsng = male or female | man or woman | boy or girl

$color  = red | blue | white | black | green | yellow
'''
import Behavior
import sys,os
import re
import XmlPerser as xml_data

behavior = Behavior.Behavior()
data = [\
    {\
        # $crowdq = How many $people are in the crowd?
        # call one's own function
        'pattern':[\
            re.compile(r'many (?P<people>.+) are in the crowd', re.IGNORECASE),\
            re.compile(r'how many (?P<people>.+) are', re.IGNORECASE),\
        ],\
        'callback':behavior.UnimplementedCountReply,\
        # $people = $appl | $gppl
        # $appl   = children | adults | elders
        # $gppl   = males | females | men | women | boys | girls
    },\
    {\
        # ???
        # $crowdq = How many people in the crowd are ($posppl | {gesture})?
        'pattern':[\
                re.compile(r'crowd (?:\w+) (?P<posppl>.+)', re.IGNORECASE),\
                re.compile(r'crowd (?:\w+) (?P<posprs>\w+)', re.IGNORECASE),\
                re.compile(r'crowd (?:\w+) (?P<gesture>.+)', re.IGNORECASE)],\
        'callback':behavior.UnimplementedCountReply,\
    },\
    {\
        # call one's own function
        # $crowdq = Tell me the number of $people in the crowd
        'pattern':[\
            re.compile(r'of (?P<people>.+) in the crowd', re.IGNORECASE),\
            re.compile(r'number of (?P<people>.+) in', re.IGNORECASE),\
        ],\
        'callback':behavior.UnimplementedCountReply,\
        # $people = $appl | $gppl
        # $appl   = children | adults | elders
        # $gppl   = males | females | men | women | boys | girls
    },\
    {\
        # call one's own function
        # $crowdq = Was the person $posprs a $gprsng?
        'pattern':[\
            re.compile(r'person (?P<posprs>\w+) a (?P<gprsng>.+)', re.IGNORECASE),\
        ],\
        'callback':behavior.UnimplementedGprsngReply,\
        # $posprs = standing | sitting | lying down
        # $gprsng = male or female | man or woman | boy or girl
    },\
    {\
        # ???
        # $crowdq = Tell me if the person ($posprs | {gesture}) was a $gprsn?
        'pattern':[\
            re.compile(r'person (?P<posprs>\w+) was a (?P<gprsn>.+)', re.IGNORECASE),\
            re.compile(r'person (?P<gesture>.+) was a (?P<gprsn>.+)', re.IGNORECASE)\
        ],\
        'callback':behavior.UnimplementedGprsnReply,\
        # $posprs = standing | sitting | lying down
        # $gprsn  = male | female | man | woman | boy | girl
    },\
    {\
        # ???
        # $crowdq = Tell me how many people were wearing $color
        'pattern':[\
            re.compile(r'wear (?P<color>\w+)', re.IGNORECASE),\
            re.compile(r'wears (?P<color>\w+)', re.IGNORECASE),\
            re.compile(r'wearing (?P<color>\w+)', re.IGNORECASE),\
            re.compile(r'wore (?P<color>\w+)', re.IGNORECASE),\
            re.compile(r'worn (?P<color>\w+)', re.IGNORECASE),\
        ],\
        'callback':behavior.UnimplementedCountReply,\
        # $color  = red | blue | white | black | green | yellow
    },\
]
