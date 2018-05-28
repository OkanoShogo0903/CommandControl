# -*- coding: utf-8 -*-
import subprocess
import os
import datetime
import types
import re
import XmlPerser as xml_data

class Behavior():
    ''' reference from CommandControl '''
    def __init__(self):
        self.variable_pattern = re.compile(r'\$\w+') # example : $hoge
        # Text within the embedded key
        self.embedded_key_pattern = re.compile(r'\$(\w+)') # example : $key


    def Talk(self, text):
        ''' args: <tuple> (str,str,...) , test: str '''
        '''
        if args != None:
            for i in args:
                # search iterater's dictation
                #print(i)
                _dict = self.getDict(i)
                if _dict != None:
                    #print("_dict :", _dict)
                    key = self.getKeyFromText(text)
                    #if key in _dict:
                    text = self.variable_pattern.sub(_dict[key],text)

            #text = self.variable_pattern.sub(*args,text)
        else:
            pass
        '''

        print("A :", text)
        self.picoSpeaker(text)


    def customTalk(self, text, **args):
        ''' args: <tuple> (str,str,...) , test: str
        example :
            Q : Where is the desk locate?
                term    args : {'placement':'desk'}
                        text : 'it in $room'

                'pattern_variable':{'placement':'room'} meanning is "<placement> tag ---dict---> dict['room']"
                replace "$room" ---> "dict['room']"
            A : it in bedroom
        '''
        print("args",args)
        #if isCheckPatternVariablePair(args,checklist=p['pattern_variable']) is True:
        #if args != None:
        #keys = args.iterkeys()
        #try:
        for k in args.keys():
            #print(args[k])
            #print(self.getDict(args[k]))
            _dict = self.getDict(args[k])
            if _dict != None: # matching dictation is existted
                #print("_dict :", _dict)
                key = self.getKeyFromText(text)
                #if key in _dict:
                text = self.variable_pattern.sub(_dict[key], text)

                #text = self.variable_pattern.sub(*args,text)
                print("A :", text)
                self.picoSpeaker(text)
                return True
            else: # matching dictation is not existted!!
                # Please pronounce nouns more clearly
                print("<---------dicterr----------->")
                return False
        '''
        except KeyError:
            print("<---------keyerr----------->")
            return False
        '''


# --------------[BaseFuntion START]---------------------->
    def picoSpeaker(self, say_text):
        ''' !!! pico speeck !!! '''
        if os.name == 'posix': # linux
            voice_cmd = '/usr/bin/picospeaker %s' %say_text
            subprocess.call(voice_cmd.strip().split(' '))


    def getDict(self, _value):
        sum_list = xml_data.location_list + xml_data.object_list + xml_data.name_list
        for iter_dict in sum_list: # list naihou no houga ii
            if _value in iter_dict.values():
                return iter_dict
        else:
            return None


    def getKeyFromText(self, _text):
        capture = self.embedded_key_pattern.search(_text).groups() # groups return tuple
        return capture[0]


    def isCheckPatternVariablePair(captures, checklist):
        for i in captures:
            pass
            #if i['placement'] == checklist[]:
        return False


# --------------[One's own callback function START]---------------------->

    def TalkTime(self):
        self.Talk('it is ' + datetime.datetime.now().strftime('%H %M')) # %H mean hour <str number> ,%M mean minute <str number>


    def TalkToday(self):
        self.Talk('today is ' + datetime.datetime.now().strftime('%A')) # %A mean day of the week <str>


    def HowManyObjInTheRoom(self, text, **args):
        import random
        self.Talk(text=str(random.randint(1, 3))) # randint(a, b) -> a <= n <= b

    def HowManyObjAreThere(self, text, **args):
        ''' object question '''
        #$objq = How many {category} are there?
        import random
        self.Talk(text=str(random.randint(1, 3))) # randint(a, b) -> a <= n <= b
