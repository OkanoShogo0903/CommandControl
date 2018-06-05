# -*- coding: utf-8 -*-
from functools import reduce
import xml.etree.ElementTree as ET
#import os
#print(os.getcwd()) # C:\Users\okano\Documents\CommandControl
#sum_xml_url = [
#    'scripts/CommonFiles/Locations.xml',\
#    'scripts/CommonFiles/Names.xml',\
#    'scripts/CommonFiles/Objects.xml'
#]
location_list = []
object_list = []
name_list = []
crowd_state_list = []
color_list = []
gestures_list = []
origins_sum_list = []
comparison_list = []

add_path = '' # To absorb the difference of the os

def absorbOsPathDifference():
    ''' To absorb the difference of the os '''
    import os
    global add_path
    #print("os",os.name)
    if os.name == 'nt': # windows
        add_path = 'scripts/'
    elif os.name == 'posix': # linux
        add_path = ''
    else:
        add_path = ''


def setReferredGlobalValue():
    global comparison_list
    comparison_list = [\
        {'adja':'heaviest'},\
        {'adja':'lightest'},\
        {'adja':'smallest'},\
        {'adja':'biggest'},\
        {'adjr':'heavier'},\
        {'adjr':'lighter'},\
        {'adjr':'smaller'},\
        {'adjr':'bigger'},\
    ]
    global origins_sum_list
    origins_sum_list = \
            location_list + object_list + name_list + \
            gestures_list + color_list + crowd_state_list + comparison_list


def getXmldata():
    ''' get (object|location|name) info from xml files '''
    with open(add_path + 'Locations.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            for grandson in child:
                _dict = {}
                _dict['room'] = child.attrib['name']
                _dict.update(grandson.attrib)
                location_list.append(_dict)

    with open(add_path + 'Names.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            _dict = {}
            _dict['name'] = child.text
            _dict.update(child.attrib)
            name_list.append(_dict)

    with open(add_path + 'Objects.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            for grandson in child:
                _dict = {}
                _dict.update(child.attrib)
                _dict.update(grandson.attrib) # overwrite 'name'
                _dict['category'] = child.attrib['name']
                object_list.append(_dict)

    with open(add_path + 'Crowd.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            _dict = {}
            _dict.update(child.attrib)
            crowd_state_list.append(_dict)

    with open(add_path + 'Color.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            _dict = {}
            _dict.update(child.attrib)
            color_list.append(_dict)


    with open(add_path + 'Gestures.xml', 'r') as xml_file:
        root = ET.fromstring(xml_file.read())
        for child in root: # reference to child node
            _dict = {}
            _dict.update(child.attrib)
            gestures_list.append(_dict)


def init():
    ''' call once '''
    # set file's path
    absorbOsPathDifference()

    # get xml data from CommonFiles
    getXmldata()

    #print("[locate list]",location_list)
    #print("[object list]",object_list)
    #print("[name list]",name_list)
    #print("[crowd list]",crowd_state_list)
    #print("[color list]",color_list)
    #print("[gesture list]",gestures_list)

    # set global value
    setReferredGlobalValue()


# set params in init function
init()
