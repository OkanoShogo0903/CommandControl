# -*- coding: utf-8 -*-
'''

; grammar name Category I
; grammar tier Easy
; import common.txt

$Main     = $deliver
$Main     = $fndppl
$Main     = $fndobj
'''

##############################################################################
#
# Production Rules required by common.txt
#
##############################################################################
; Define an object type
$object   = {kobject}

; Rule for finding a specific (named) person
$findp    = $vbfind ( {name} | a person | someone )

; A named or described person in the given place
$whowhere = {name} at the {beacon 1}

##############################################################################
#
# Manipulation
#
##############################################################################
$deliver  = $vbbring (me | to $whowhere) the {kobject} from the {placement}
$deliver  = $takefrom and ($delivme | $delivat)
$deliver  = $takefrom and $place


##############################################################################
#
# Find people
#
##############################################################################
$fndppl   = Tell me the name of the person at the {beacon}
$fndppl   = Tell me the name of the person in the {room}

##############################################################################
#
# Find objects
#
##############################################################################
$fndobj   = $vbfind the {kobject?} in the {room}



##############################################################################
#
# Rules
#
##############################################################################

import sys,os
import Behavior

import re
import XmlPerser as xml_data
behavior = Behavior.Behavior()
data = [\
    {\
        # $fndobj   = $vbfind the {kobject?} in the {room}
        # $arenaq = Where is the {name} located?
        'pattern':[\
            re.compile(r'find the (?P<name>.+) in the (?P<room>.+)', re.IGNORECASE),\
        ],\
        'pattern_variable':{'name':'room'},\
        'text':'it is in $room',\
        'callback':behavior.customTalk,\
    },\
