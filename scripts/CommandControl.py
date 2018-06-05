# -*- coding: utf-8 -*-
# reference : https://github.com/kyordhel/GPSRCmdGen

# [ParameterStart]----------------------->
IS_ROS_ACTIVE = False
# [ParameterEnd]------------------------

import re
import datetime
import Behavior

import PredefinedQuestions
import ArenaQuestions
import ObjectQuestions
import CrowdQuestions
import XmlPerser as xml_data
# for ros
if IS_ROS_ACTIVE is True:
    import rospy
    from std_msgs.msg import String,Bool
''' ROSに音声認識の結果を投げるWORDスレッドを管理するクラス '''
# SPR
predefined_questions = PredefinedQuestions.data
arena_questions = ArenaQuestions.data
object_questions = ObjectQuestions.data
crowd_questions = CrowdQuestions.data
# GPSR

def SpeechTextToBehavior(text, spr = True, gpsr = False):
    ''' ... from speech text '''
    print("Q :",text)

    # Regular expression matching
    sum_pattern = None
    if spr is True:
        sum_pattern = \
            predefined_questions + arena_questions + object_questions + crowd_questions
        #sum_pattern = predefined_questions + arena_questions
    elif gpsr is True:
        sum_pattern = None

    # call a matching pattern's callback function with capture args
    for q_data in sum_pattern:
        for p in q_data['pattern']:
            sre_match = p.search(text) # capture
            if sre_match is not None:
                #captures = sre_match.groups()
                captures = sre_match.groupdict() # when capture is empty -> capture:{}
                captures = removeHipSpace(captures)

                print("captures     :",captures)
                #print("p['pattern'] :",p) # capture

                if isSimilarRegexpBlock(captures):
                    if 'text' in q_data: # or text element is existting
                        #handler(p['callback'], p['text'])
                        if q_data['callback'](text=q_data['text'], **captures) is not False:
                            return True
                        else:
                            pass
                    else:
                        if q_data['callback'](**captures) is True:
                            return True
                        else:
                            pass
    else:
        print('A : Please talk again')
        Behavior.Behavior().picoSpeaker('Please talk again')
        return False


def handler(func,*args):
    return func(*args)


def removeHipSpace(captures):
    '''
    remove space for compare match
    "side board " -> "side board"
    '''
    mirror = captures
    for k,v in captures.items(): # dict.items() : return key,value
        if v[-1] == " ":
            mirror[k] = v[:-1]
    return mirror


def TrimNumberPart(captures):
    ''' {'name1':'apple'} ---> {'name':'apple'} '''
    num_p = re.compile(r'[0-9]')
    new_captures = {}
    for k in captures.keys(): # get key list
        # trim numbers
        #non_num_k =
        new_captures[num_p.sub('',k)] = captures[k]

    return new_captures


num_pattern = re.compile(r'[0-9]')
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
    correct_count = 0
    for captured_key,captured_value in captures.items(): # dict.items() : return key,value
        # remove obviously strange things
        # example : {'room':'None'},{'name','how'}
        for i in xml_data.origins_sum_list:
            captured_key = num_pattern.sub('',captured_key)
                
            if captured_key in i: # mean location
                if i[captured_key] == captured_value:
                    print(captured_value)
                    correct_count += 1
                    break
                    #return True

        # location
    #else:
        #return False

    print("---",correct_count)
    if correct_count == len(captures): # mean all hit
        return True
    else:
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
    #SpeechTextToBehavior(text="")
    # ---CrowdQuestions---
    # ok
    #SpeechTextToBehavior(text="How many elders are in the crowd")
    #SpeechTextToBehavior(text="How many people in the crowd are waving")
    #SpeechTextToBehavior(text="Tell me the number of boys in the crowd")
    #SpeechTextToBehavior(text="Tell me if the person waving was a man")
    #SpeechTextToBehavior(text="Tell me if the person standing was a man")
    #SpeechTextToBehavior(text="Tell me how many people were wearing red")
    # pre fix
    #SpeechTextToBehavior(text="How many people in the crowd are standing or sitting")
    #SpeechTextToBehavior(text="Was the person sitting a man or woman") # woman -> man
    #SpeechTextToBehavior(text="Was the person sitting a man or woman") # multi ward
    # ---ObjectQuestions---
    # ok
    #SpeechTextToBehavior(text="How many tuna fish are there?") # false
    #SpeechTextToBehavior(text="How many food are there?")

    #SpeechTextToBehavior(text="How many tuna fish are in the kitchen")
    #SpeechTextToBehavior(text="How many snacks are in the desk")
    #SpeechTextToBehavior(text="How many snacks are in the kitchen")

    #SpeechTextToBehavior(text="What names are stored in the kitchen")

    #SpeechTextToBehavior(text="Where can I find the apple")
    #SpeechTextToBehavior(text="Where can I find the pasta")
    #SpeechTextToBehavior(text="Where can I find the toiletries")
    #SpeechTextToBehavior(text="What is the category of the tuna fish") # food

    #SpeechTextToBehavior(text="How many fruits are there?")
    # pre fix
    #SpeechTextToBehavior(text="What is the color of the apple")
    #SpeechTextToBehavior(text="Between the apple and melon, which one is bigger")
    #SpeechTextToBehavior(text="Do the apple are melon belong to the same category")
    #SpeechTextToBehavior(text="Which is the biggest fruits")

    # ---ArenaQuestions---
    # ok
    #SpeechTextToBehavior(text="Where is the foo locate")
    #SpeechTextToBehavior(text="How many freezer are in the kitchen")
    #SpeechTextToBehavior(text="In which room is the tuna fish")
    #SpeechTextToBehavior(text="Where is the M and M's locate")
    #SpeechTextToBehavior(text="In which room is the Robo O's")

    # ---PredefinedQuestions---
    #SpeechTextToBehavior("When was invented the B programming language")
    #SpeechTextToBehavior("What day is today")
    #SpeechTextToBehavior("What time is it")
    #SpeechTextToBehavior(spr=True, text="What day is today")
