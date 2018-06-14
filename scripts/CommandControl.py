# -*- coding: utf-8 -*-
# reference : https://github.com/kyordhel/GPSRCmdGen

# [ParameterStart]----------------------->
IS_ROS_ACTIVE = False 
INTERVAL_TALK_END_TO_START = 5.0 # sec
match_ratio_threshold = 0.7 # 0 ~ 1
is_do_input_test = True
# [ParameterEnd]------------------------

import json
import re
import datetime
import difflib

import Behavior
import XmlPerser as xml_data
import PredefinedQuestions
import ArenaQuestions
import ObjectQuestions
import CrowdQuestions
# For ros ----------->
if IS_ROS_ACTIVE is True:
    import rospy
    from std_msgs.msg import String,Bool

# Grobal Value ------>
mutex = True
last_time_stamp = datetime.datetime.now()
# SPR --------------->
predefined_questions = PredefinedQuestions.data
arena_questions = ArenaQuestions.data
object_questions = ObjectQuestions.data
crowd_questions = CrowdQuestions.data
# GPSR --------------> None

def SpeechTextToBehavior(text, spr = True, gpsr = False):
    ''' ... from speech text '''
    print('-'*70)
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
    try:
        for q_data in sum_pattern:
            for p in q_data['pattern']:
                sre_match = p.search(text) # capture
                if sre_match is not None:
                    #captures = sre_match.groups()
                    captures = sre_match.groupdict() # when capture is empty -> capture:{}
                    captures = removeHipSpace(captures)

                    captures = fittingMostSimilarWord(captures)
                    #print("p['pattern'] :",p) # capture

                    if isSimilarRegexpBlock(captures):
                        print("captures     :",captures)
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
    except:
        import traceback
        print(traceback.format_exc())
        traceback.print_exc()

    #print('A : Please talk again')
    #Behavior.Behavior().picoSpeaker('Please talk again')
    print('A : Sorry. I dont know')
    Behavior.Behavior().picoSpeaker('Sorry. I do not know')
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
        #if v == None:
        #    return captures
        if v[-1] == " ":
            mirror[k] = v[:-1]
    return mirror

def fittingMostSimilarWord(captures):
    ''' using difflib '''
    mirror = captures
    for k,v in captures.items(): # dict.items() : return key,value
        highest_ratio = -1
        target_list = []
        if k == 'name' or k == 'name1' or k == 'name2':
            target_list = xml_data.object_list + xml_data.location_list
        elif k == 'room':
            target_list = xml_data.room_list
        elif k == 'color':
            target_list = xml_data.color_list
        elif k == 'gesture':
            target_list = xml_data.gestures_list
        elif k == 'adja' or k == 'adjr':
            target_list = xml_data.comparison_list
        elif k == 'posppl' or k == 'posprs' or k == 'gprsn' or k == 'gprsng':
            target_list = xml_data.crowd_state_list
        else:
            continue

        for i in target_list:
            try:
                ratio = difflib.SequenceMatcher(None, i[k], v).ratio() # 0 ~ 1
                if ratio > highest_ratio and ratio > match_ratio_threshold:
                    print('Fitting :',ratio, mirror[k] + ' ---> ' + i[k])
                    mirror[k] = i[k] # The highest ratio is updated to the last.
                    #print(i[k])
                    highest_ratio = ratio
            except KeyError:
                pass
    return mirror


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

    correct_count = 0
    for captured_key,captured_value in captures.items(): # dict.items() : return key,value
        # remove obviously strange things
        #   example : captures ---> {'room':'None'},{'name','how'}
        captured_key = num_pattern.sub('',captured_key) # remove number
        for i in xml_data.origins_sum_list:
            try:
                if i[captured_key] == captured_value:
                    #print(captured_value)
                    correct_count += 1
                    break
            except KeyError:
                pass

    #print("---",correct_count)
    if correct_count == len(captures): # mean all hit
        return True
    else:
        return False


# ros interface ---->
def riddleWordCB(msg):
    ''' SPR riddle game callback func '''
    global mutex
    #global last_time_stamp
    print("riddleCB")
    word = msg.data
    word.count(' ')
    if word.count(' ') >= 2: # Block short sentence. Maybe,short sentence is noize.
        if mutex == True:
            mutex = False
            # Process start --->
            #if voice_dict['time_stamp'] > last_time_stamp + datetime.timedelta(seconds=INTERVAL_TALK_END_TO_START):
            #last_time_stamp = datetime.datetime.now()
            answer = Bool()
            Behavior.Behavior().picoSpeaker('Your question is ' + word)
            rospy.sleep(2) # sec
            answer.data = SpeechTextToBehavior(word, spr = True)
            rospy.sleep(3) # sec
            print "publish : " + str(answer.data)
            answer_pub.publish(answer)
            # Process end <---
            mutex = True
        else:
            print ('mutex blocking!!')


if IS_ROS_ACTIVE:
    answer_pub = rospy.Publisher('/riddle_res/is_action_state',Bool,queue_size=1)
    speech_sub = rospy.Subscriber('/riddle_req/question_word',String,riddleWordCB)
    #speech_sub = rospy.Subscriber('/riddle_req/question_dict',String,riddleDictCB)

# ----<

# main --->
if IS_ROS_ACTIVE:
    print('--- Command Control Standby ---')
    rospy.init_node('command_control')
    rospy.spin()

if __name__ == '__main__':
    ''' testcode '''
    if is_do_input_test is True:
        string = ''
        while 1:
            print('<------------ Inputtable ;) -------------->')
            if string == 'exit':
                break
            else:
                string = raw_input()
                SpeechTextToBehavior(text=string)
    if IS_ROS_ACTIVE == False:
        pass
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
        #SpeechTextToBehavior(text="How many people in the crowd are standing or sitting")
        #SpeechTextToBehavior(text="Was the person sitting a man or woman") # woman -> man
        #SpeechTextToBehavior(text="Was the person sitting a man or woman") # multi ward
        # ---ObjectQuestions---
        # ok
        #SpeechTextToBehavior(text="How many tuna fish are there?") # false
        #SpeechTextToBehavior(text="How many snacks are there?")

        #SpeechTextToBehavior(text="How many tuna fish are in the kitchen")
        #SpeechTextToBehavior(text="How many snacks are in the desk")
        #SpeechTextToBehavior(text="How many snacks are in the kitchen")

        #SpeechTextToBehavior(text="What names are stored in the bathroom cabinet")

        #SpeechTextToBehavior(text="Where can I find the apple")
        #SpeechTextToBehavior(text="Where can I find the pasta")
        SpeechTextToBehavior(text="Where can I find the toiletries")
        #SpeechTextToBehavior(text="What is the category of the tuna fish") # food

        #SpeechTextToBehavior(text="How many fruits are there?")

        #SpeechTextToBehavior(text="What is the color of the apple")
        #SpeechTextToBehavior(text="What is the color of the soap")

        #SpeechTextToBehavior(text="Do the apple and melon belong to the same category")
        #SpeechTextToBehavior(text="Do the apple and tuna fish belong to the same category")

        #SpeechTextToBehavior(text="Which is the heaviest fruits")

        #SpeechTextToBehavior(text="Between the melon and apple, which one is bigger")
        #SpeechTextToBehavior(text="Between the apple and banana, which one is lighter")

        # ---ArenaQuestions---
        # ok
        #SpeechTextToBehavior(text="Where is the M and M's locate")
        #SpeechTextToBehavior(text="In which room is the Robo O's")
        #SpeechTextToBehavior(text="How many choco flakes are in the bedroom")
        #SpeechTextToBehavior(text="How many choco flakes are in the kitchen")
        #SpeechTextToBehavior(text="How many doors does the bedroom have")

        # ---PredefinedQuestions---
        #SpeechTextToBehavior("When was invented the B programming language")
        #SpeechTextToBehavior("What day is today")
        #SpeechTextToBehavior("What time is it")

