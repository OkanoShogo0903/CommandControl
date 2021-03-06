# -*- coding: utf-8 -*-
# reference : https://github.com/kyordhel/GPSRCmdGen

# [ParameterStart]----------------------->
IS_ROS_ACTIVE = True
INTERVAL_TALK_END_TO_START = 5.0 # sec
match_ratio_threshold = 0.7 # 0 ~ 1
is_do_input_test = False
# [ParameterEnd]------------------------

import json
import re
import datetime
import difflib
import time

import Behavior
import XmlPerser as xml_data
import PredefinedQuestions
import ArenaQuestions
import ObjectQuestions
import CrowdQuestions
import subprocess

import google_tts
#import mute
    #Behavior.Behavior().picoSpeaker('Sorry. I do not know')
def speak(sentence):
    #google_tts.say(sentence)
    try:
        voice_cmd = '/usr/bin/picospeaker %s' %sentence
        subprocess.call(voice_cmd.strip().split(' '))
        print "[PICO] " + sentence
    except OSError:
        print "[PICO] Speacker is not activate. Or not installed picospeaker."


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

                    #captures = fittingMostSimilarWord(captures)
                    #print("p['pattern'] :",p) # capture

                    if isSimilarRegexpBlock(captures):
                        print("captures     :",captures)
                        # Warnign !!! -->
                        # <---
                        try:
                            speak('Your question is \"'+str(q_data['textbook_sentence'])+'\"')
                        except:
                            speak('Your question is \"'+str(text)+'\"')

                        if ('text' in q_data) and (len(captures) != 0): # or text element is existting
                            # Contain variable
                            if q_data['callback'](text=q_data['text'], **captures) is not False:
                                return True
                            else:
                                pass
                        elif len(captures) != 0:
                            if q_data['callback'](**captures) is not False:
                                return True
                            else:
                                pass
                        elif 'text' in q_data:
                            # Prefix
                            if q_data['callback'](text=q_data['text']) is not False:
                                return True
                            else:
                                pass
                        else:
                            if q_data['callback']() is not False:
                                return True
                            else:
                                pass
    except:
        import traceback
        print(traceback.format_exc())
        traceback.print_exc()

    print("A : Sorry. I dont know")
    speak('Sorry. I dont know')

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
    print("riddleCB")
    answer = String()
    answer.data = 'None'
    global mutex
    #global last_time_stamp
    # BROCK PATTERN ---------->
    word = msg.data
    #word.count(' ')
    if 'Sorry' in msg.data:
        print '!'*50

        '''
        elif 'play' in msg.data:
            import youtube
            if 'oil' in msg.data:
                youtube.aimer()
            else:
                youtube.kiminonaha()
            answer_pub.publish(True)
        '''
    elif word.count(' ') < 2: # Block short sentence. Maybe,short sentence is noize.
        print ('too short!!')
    # <--------- BROCK PATTERN end
    else:
        if mutex == True:
            mutex = False
            #mute.mute()

            # Process start --->
            
            #Behavior.Behavior().picoSpeaker('Your question is ' + word)
            answer.data = str(SpeechTextToBehavior(word, spr = True))
            rospy.sleep(2) # sec
            # Process end <---

            mutex = True
            #mute.unmute()
        else:
            print ('mutex blocking!!')

    print "publish : " + str(answer.data)
    answer_pub.publish(answer)


if IS_ROS_ACTIVE:
    answer_pub = rospy.Publisher('/riddle_res/result_str',String,queue_size=1)
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
    if IS_ROS_ACTIVE == False:
        if is_do_input_test is True:
            string = ''
            while 1:
                print('<------------ Inputtable ;) -------------->')
                if string == 'exit':
                    break
                else:
                    string = raw_input()
                    SpeechTextToBehavior(text=string)
        else:
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
            SpeechTextToBehavior(text="How many snacks are in the kitchen")

            #SpeechTextToBehavior(text="What names are stored in the bathroom cabinet")

            #SpeechTextToBehavior(text="Where can I find the apple")
            #SpeechTextToBehavior(text="Where can I find the pasta")
            #SpeechTextToBehavior(text="Where can I find the toiletries")
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

