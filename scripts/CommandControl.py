# -*- coding: utf-8 -*-
# reference : https://github.com/kyordhel/GPSRCmdGen
import re
import datetime
import Behavior

import PredefinedQuestions
import ArenaQuestions
import ObjectQuestions
import XmlPerser as xml_data
# for ros
IS_ROS_ACTIVE = False
if IS_ROS_ACTIVE is True:
    import rospy
    from std_msgs.msg import String,Bool
''' ROSに音声認識の結果を投げるWORDスレッドを管理するクラス '''
# SPR
predefined_questions = PredefinedQuestions.data
arena_questions = ArenaQuestions.data
object_questions = ObjectQuestions.data
# GPSR

def SpeechTextToBehavior(text, spr = True, gpsr = False):
    ''' ... from speech text '''
    print("Q :",text)

    # Regular expression matching
    sum_pattern = None
    if spr is True:
        sum_pattern = predefined_questions + arena_questions + object_questions
    elif gpsr is True:
        sum_pattern = None

    # call a matching pattern's callback function with capture args
    for p in sum_pattern:
        sre_match = p['pattern'].search(text)
        if sre_match is not None:
            #captures = sre_match.groups()
            captures = sre_match.groupdict() # when capture is empty -> capture:{}
            print("captures :",captures,"  p['pattern'] :",p['pattern']) # capture
            if isSimilarRegexpBlock(captures):
                if 'text' in p: # or text element is existting
                    #handler(p['callback'], p['text'])
                    if p['callback'](text=p['text'], **captures) is not False:
                        return True
                    else:
                        pass
                else:
                    print("<---???--->")
                    if p['callback']() is True:
                        return True
                    else:
                        pass
    else:
        print('A : Please talk again')
        Behavior.Behavior().picoSpeaker('Please talk again')
        return False


def handler(func,*args):
    return func(*args)


def isSimilarRegexpBlock(captures):
    ''' This function fix regex's miss match.
    [ERRER EXAMPLE]
        Q : How many snacks are in the desk ?
            |
        Right pattern : How many (?P<category>\w+) are in the (?P<placement>\w+)
        Wrong pattern : How many ((?P<placement>\w+)|(?P<beacon>\w+)) are in the (?P<room>\w+)
            |
            +---> Miss Answer : {'room': 'desk', 'beacon': None, 'placement': 'snacks'}

    [SPECIFICATION]
        Right -> return True
        Wrong -> return False
    '''

    # TODO minaosi
    for captured_key,captured_value in captures.items(): # dict.items() : return key,value
        # reference all origin list
        for i in xml_data.origins_sum_list:
            if captured_key in i: # mean location
                if i[captured_key] == captured_value:
                    print("---1")
                    return True
        # location
    print("---3")
    return False


# ros interface ---->
if IS_ROS_ACTIVE:
    answer_pub = rospy.Publisher('/riddle_res',Bool,queue_size=1)


def riddleCB(msg):
    ''' SPR riddle game callback func '''
    print(msg.data)
    answer = Bool()
    answer.data = SpeechTextToBehavior(msg.data, spr = True)
    answer_pub.publish(answer)


if IS_ROS_ACTIVE:
    speech_sub = rospy.Subscriber('/riddle_req',String,riddleCB)
# ----<

if __name__ == '__main__':
    if IS_ROS_ACTIVE:
        rospy.init_node('command_control')
        rospy.spin()

    # <---testcode--->
    # ---common err---
    #SpeechTextToBehavior(text="Where is the baby chair located?")
    # ---CrowdQuestions---
    # ---ObjectQuestions---
    # ok
    SpeechTextToBehavior(text="Where can I find the apple?")
    #SpeechTextToBehavior(text="How many apple are there?")
    SpeechTextToBehavior(text="How many snacks are in the desk")
    #SpeechTextToBehavior(text="")
    # pre fix
    SpeechTextToBehavior(text="What is the color of the apple")

    # ---ArenaQuestions---
    # ok
    #SpeechTextToBehavior(text="Where is the foo locate?")
    #SpeechTextToBehavior(text="How many freezer are in the kitchen?")
    #SpeechTextToBehavior(text="In which room is the armchair?")
    #SpeechTextToBehavior(text="In which room is the sideboard?")
    # pre fix
    #SpeechTextToBehavior(text="How many freezer are in the bedroom?")

    # ---PredefinedQuestions---
    #SpeechTextToBehavior("When was invented the B programming language")
    #SpeechTextToBehavior("What day is today")
    #SpeechTextToBehavior("What time is it")
    #SpeechTextToBehavior(spr=True, text="What day is today")
