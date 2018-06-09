# -*- coding: utf-8 -*-
import subprocess
import os
import datetime
import types
import re
import XmlPerser as xml_data
#import CommandControl as cc

# [ParameterStart]----------------------->
SPR_PLAY_ROOM = 'living room' # <string>
# [ParameterEnd]------------------------

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
        #print("args",args)
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
        ''' pico speeck '''
        if os.name == 'posix': # os is linux
            voice_cmd = '/usr/bin/picospeaker %s' %say_text
            try:
                subprocess.call(voice_cmd.strip().split(' '))
            except:
                print("[PICO] pico speaker is not active")


    def getDict(self, _value,target_list=None):
        '''
        [SPECIFICATION]
            return farst match dictation!
        [WARNIGN]
            リストに同じキーと値のペアを持つものがいることを想定していない
            大会会場で例えばリビングにリンゴがあって、ベッドルームにもリンゴがあるというのは想定していない
        '''
        #sum_list = xml_data.location_list + xml_data.object_list + xml_data.name_list
        if target_list == None:
            target_list = xml_data.origins_sum_list
        else:
            pass

        for iter_dict in target_list: # list naihou no houga ii
            if _value in iter_dict.values():
                return iter_dict
        else:
            return None


    def getKeyFromText(self, _text):
        capture = self.embedded_key_pattern.search(_text).groups() # groups return tuple
        return capture[0]


    def getComparedResultDict(self, comparison, target_list):
        '''
            comparison:
                biggest,smallest,bigger,smaller,... ex
            return:
                This func return matched object(?) dict
        '''
        
        # Init
        c_key = '' # 'c' mean 'compare'.
        c_unit = ''

        # Detect compare types
        if comparison == 'biggest' or comparison == 'bigger':
            c_key = 'size'
            c_unit = 'plus'
        elif comparison == 'smallest' or comparison == 'smaller':
            c_key = 'size'
            c_unit = 'minus'
        elif comparison == 'heaviest' or comparison == 'heavier':
            c_key = 'weight'
            c_unit = 'plus'
        elif comparison == 'lightest' or comparison == 'lighter':
            c_key = 'weight'
            c_unit = 'minus'
        print(c_key)
        print(c_unit)

        # compare
        sorted_list = sorted(target_list, key=lambda i:i[c_key]) # sort in ascending order. (1,2,3,...)
        if c_unit == 'plus':
            result_dict = sorted_list[-1]
        elif c_unit == 'minus':
            result_dict = sorted_list[0]

        # output
        print(sorted_list)
        #print(result_dict)
        return result_dict


# --------------[emergency function START]---------------------->
    def UnimplementedCountReply(self, **args):
        '''
        [SPECIFICATION]
            Say 1 or 2.
            That is all.
            Use it in emergency. ;)
        '''
        import random
        self.Talk(text=str(random.randint(1, 2))) # randint(a, b) -> a <= n <= b
        return True


    def UnimplementedColorReply(self, **args):
        '''
        [PATTERN]
        [SPECIFICATION]
            Say predefined color.
            Use it in emergency. ;)
        '''
        self.Talk(text='red')
        return True


    def UnimplementedGprsnReply(self, **args):
        '''
        [PATTERN]
            $crowdq = Tell me if the person ($posprs | {gesture}) was a $gprsn?
            $gprsn  = male | female | man | woman | boy | girl
        [SPECIFICATION]
            Shit.
        '''
        self.Talk(text=args['gprsn']+' is')
        return True


    def UnimplementedGprsngReply(self, **args):
        '''
        [PATTERN]
            $crowdq = Was the person $posprs a $gprsng?
            $gprsng = male or female | man or woman | boy or girl
        [SPECIFICATION]
            Shit.
        '''
        say = ''
        if args['gprsng'] == 'male or female':
            say = 'male'
        elif args['gprsng'] == 'man or woman':
            say = 'man'
        elif args['gprsng'] == 'boy or girl':
            say = 'boy'
        
        self.Talk(text=say+' is')
        return True


# --------------[One's own callback function START]---------------------->
    def TalkTime(self):
        self.Talk('it is ' + datetime.datetime.now().strftime('%H %M')) # %H mean hour <str number> ,%M mean minute <str number>
        return True


    def TalkToday(self):
        self.Talk('today is ' + datetime.datetime.now().strftime('%A')) # %A mean day of the week <str>
        return True


    def howManyDoors(self, text, **args):
        '''
        ArenaQuestions
        [PATTERN]
            $arenaq = How many doors does the {room} have?
        '''
        # process
        d = self.getDict(args['room'],xml_data.room_list)
        door_num = d['door']
        # output
        self.Talk(text=str(door_num)) # randint(a, b) -> a <= n <= b
        return True


    def howManyObjInTheRoom(self, text, **args):
        '''
        ArenaQuestions
        [PATTERN]
            $arenaq = How many {name} are in the {room}?
        '''
        # init
        ans = None
        name = args['name']
        room = args['room']

        # count object in room
        for i_dict in xml_data.object_list: # list naihou no houga ii
            if room in i_dict.values():
                if name in i_dict.values():
                    ans = self.getDict(args['name'])
                    break

        # output
        if ans == None:
            self.Talk(text='0')
        else:
            self.Talk(text=str(ans['num'])) # randint(a, b) -> a <= n <= b
        return True


    def howManyCategoryAreThere(self, text, **args):
        '''
        ObjectQuestion
        [PATTERN]
            $objq = How many {category} are there?
        [SPECIFICATION]
            say category objects number in room ;)
        '''
        # init
        object_num = 0
        category = args['category']

        # count object in room
        for i_dict in xml_data.object_list:
            if category in i_dict.values():
                if SPR_PLAY_ROOM in i_dict.values():
                    object_num += int(i_dict['num'])

        # output
        self.Talk(text=str(object_num))
        return True


    def howManyObjInThePlacement(self, text, **args):
        # TODO 実装
        '''
        ObjectQuestion
        [pattern]
            $objq = How many ({category} | names) are in the {placement}? # placement-->name or room??
        [SPECIFICATION]
            say number
        [IDEA]
            defaultLocation
        '''
        # init
        #ans = None
        #place = args['name']
        #var = args['name']
        #var = args['category']

        # count object in room
        '''
        for i_dict in xml_data.object_list:
            if category in i_dict.values():
                if SPR_PLAY_ROOM in i_dict.values():
                    object_num += int(i_dict['num'])
        '''

        # output
        import random
        self.Talk(text=str(random.randint(1, 2))) # randint(a, b) -> a <= n <= b
        return True


    def whatNames(self, text, **args):
        '''
        ObjectQuestion
        [PATTERN]
            $objq = What names are stored in the {placement}?
        [SPECIFICATION]
            say object names from lacation name
        '''
        # init
        answers = []
        placement = args['name']

        # count object in room
        for i_dict in xml_data.object_list:
            if i_dict['defaultLocation'] == placement:
                answers.append(i_dict['name'])
        # output
        if len(answers) == 0:
            string = ("I dont know")
        else:
            string = ' '.join(answers) # joint each name
        self.Talk(text=string)
        return True


    def belongToSameCategory(self, **args):
        '''
        ObjectQuestion
        [PATTERN]
            $objq = Do the {name 1} and {name 2} belong to the same category?
        [args exp]
            {'adja': 'biggest', 'category': 'fruits'}
        [SPECIFICATION]
            response is YES or NO
        '''
        # init
        dict_a = self.getDict(args['name1'], xml_data.object_list)
        dict_b = self.getDict(args['name2'], xml_data.object_list)
        # process and output
        if dict_a['category'] == dict_b['category']:
            self.Talk(text='same category')
        else:
            self.Talk(text='different category')
        return True


    def whichIsTheCompare(self, **args):
        '''
        ObjectQuestion
        [PATTERN]
            $objq = Which is the $adja {category}?
            $adja = heaviest | smallest | biggest | lightest
        [args exp]
            print("args",args) # ---> {'adja': 'biggest', 'category': 'fruits'}
        [SPECIFICATION]
            say correct obj name
        '''
        # init
        targets = [] # dictation list
        comparison = args['adja']

        # process
        if 'category' in args.keys():
            for i_dict in xml_data.object_list:
                if i_dict['category'] == args['category']:
                    targets.append(i_dict)

        else:
            self.Talk(text="I dont know")
            return True # have no false

        result_dict = self.getComparedResultDict(comparison, targets)

        # output
        self.Talk(text=result_dict['name'])
        return True


    def whichIsTheMost(self, **args):
        '''
        ObjectPattern
        [PATTERN]
            $objq = Which is the $adja object?
            $adja = heaviest | smallest | biggest | lightest
        [args exp]
            print("args",args) # ---> {'adja': 'biggest'}
        [SPECIFICATION]
            say correct obj name
        '''
        #targets = [] # dictation list
        comparison = args['adja']
        targets = xml_data.object_list 

        result_dict = self.getComparedResultDict(comparison, targets)

        # output
        self.Talk(text=result_dict['name'])
        return True


    def twoObjectComparison(self, **args):
        '''
        ObjectQuestion
        [PATTERN]
            $objq = Between the {name 1} and {name 2}, which one is $adjr?
            $adjr = heavier | smaller | bigger | lighter
        [INPUT EXAMPLE]
            text = CompareThings(args)
            self.Talk(text=text)
        [SPECIFICATION]
            Say match object name.
            That's all. ;)
            I think improve this function.
            Please add processing when the answer was EQUAL
            
        '''

        try:
            # Init
            obj_a = self.getDict(args['name1']) # This process use name because of it's unique
            obj_b = self.getDict(args['name2'])

            result_dict = self.getComparedResultDict(args['adjr'],[obj_a,obj_b])

            # output
            self.Talk(text=result_dict['name'])
            return True

            '''
            if obj_a['size'] > obj_b['size']:
                self.Talk(args['adjr'] + " is " + obj_a['name'])
                return True
            elif obj_a['size'] < obj_b['size']:
                self.Talk(args['adjr'] + " is " + obj_b['name'])
                return True
            else:
                self.Talk("size equal")
                return True
            '''
        except KeyError:
            print("KeyError")
            return False

