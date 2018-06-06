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
        print("A :", text)
        self.picoSpeaker(text)
        return True


    def customTalk(self, text, **args):
        '''
        args    : <tuple> (str,str,...) , test: str
        example :
            Q : Where is the desk locate?
                term    args : {'placement':'desk'}
                        text : 'it in $room'

                'pattern_variable':{'placement':'room'} meanning is "<placement> tag ---dict---> dict['room']"
                replace "$room" ---> "dict['room']"
            A : it in bedroom
        '''
        print("args",args)
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
                self.Talk(text)
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
            try:
                subprocess.call(voice_cmd.strip().split(' '))
            except:
                print("[ERRER] pico speaker is not active")


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


    def returnCompareDict(self, comparison, *obj):
        '''
            comparison:
                biggest,smallest,bigger,smaller,... ex
            return:
                This func return matched object(?) dict
        '''
        is_size = False
        is_weight = False
        # Detect compare types
        if comparison == 'biggest' or comparison == 'smallest' or\
        comparison == 'bigger' or comparison == 'smaller':
            is_size = True
        elif comparison == 'heaviest' or comparison == 'lightest' or\
        comparison == 'heavier' or comparison == 'lighter':
            is_weight = True

        print (obj) # taple
        if is_weight == True:
            return 'weight'
        elif is_size == True:
            return 'size'
        else:
            # TODO raise err
            return None


# --------------[One's own callback function START]---------------------->

    def TalkTime(self):
        self.Talk('it is ' + datetime.datetime.now().strftime('%H %M')) # %H mean hour <str number> ,%M mean minute <str number>
        return True


    def TalkToday(self):
        self.Talk('today is ' + datetime.datetime.now().strftime('%A')) # %A mean day of the week <str>
        return True


    def HowManyObjInTheRoom(self, text, **args):
        import random
        self.Talk(text=str(random.randint(1, 3))) # randint(a, b) -> a <= n <= b
        return True


    def HowManyObjAreThere(self, text, **args):
        ''' object question '''
        #$objq = How many {category} are there?
        import random
        self.Talk(text=str(random.randint(1, 3))) # randint(a, b) -> a <= n <= b
        return True


    def whichIsTheCompare(self, **args):
        #print("args",args) # {'adja': 'biggest', 'category': 'fruits'}
        obj = {}
        comparison = ''
        # Devide obj from comparison
        for k,v in args.items():
            k_match = re.search(r'\w+[0-9]',k)
            if k_match != None:
                obj['name'] == v
            else:
                comparison = v
            #try:
            #except AttributeError:

        #print(obj)
        #print(comparison)

        text = self.returnCompareDict(*obj, comparison)
        self.Talk(text=text)
        return True


    def UnimplementedCountReply(self, **args):
        import random
        self.Talk(text=str(random.randint(1, 2))) # randint(a, b) -> a <= n <= b
        return True

    def belongToSameCategory(self, **args):
        '''
        [INPUT EXAMPLE]
        [args]
            {'adja': 'biggest', 'category': 'fruits'}
        '''
        pass



    def twoObjectComparison(self, **args):
        '''
        [INPUT EXAMPLE]
        '''
        '''
        text = CompareThings(args)
        self.Talk(text=text)
        '''
        print(args)
        # creagte two dict object
        obj_a = {'name':args['name1']}
        obj_b = {'name':args['name2']}

        _dict = self.getDict(obj_a['name'])
        if _dict != None: # matching dictation is existted
            obj_a['size'] = _dict['size']
        else: # matching dictation is not existted!!
            print("<---------dicterr----------->")
            return False

        _dict = self.getDict(obj_b['name'])
        if _dict != None: # matching dictation is existted
            obj_b['size'] = _dict['size']
        else: # matching dictation is not existted!!
            print("<---------dicterr----------->")
            return False


        if obj_a['size'] > obj_b['size']:
            self.Talk(args['adjr'] + "is" + obj_a['name'])
        elif obj_a['size'] < obj_b['size']:
            self.Talk(args['adjr'] + "is" + obj_b['name'])
        else:
            self.Talk("size equal")
        return True
