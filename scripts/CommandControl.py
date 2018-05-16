# -*- coding: utf-8 -*-
# IS_ROS_ACTIVE = False
import re
import PreDefine
import datetime
def hoge1():
    print('B was developed circa 1969 at Bell Labs')


class CommandControl():
    ''' ROSに音声認識の結果を投げるWORDスレッドを管理するクラス '''
    # クラス共通の変数
    predefine = PreDefine.data
    def __init__(self):
        pass


    def SpeechTextToBehavior(self,text):
        # 正規表現マッチング
        for p in self.predefine:
            obj = p['pattern'].search(text)
            if obj:
                #print(obj.group())
                if p['date'] == True:
                    week_num = datetime.date.today().weekday() # int
                    return 'today is ' + datetime.datetime.now().strftime('%A')
                elif p['time'] == True:
                    time_str = datetime.datetime.now().strftime('%H') + " " + datetime.datetime.now().strftime('%M')
                    return 'it is ' + time_str
                else:
                    return p['print']
                #print(p['func'])
            #p['func']


class Behavior():
    def __init__(self):
        pass


if __name__ == '__main__':
    c = CommandControl()
    txt = c.SpeechTextToBehavior("When was invented the B programming language")
    print(txt)
    txt = c.SpeechTextToBehavior("What day is today")
    print(txt)
    txt = c.SpeechTextToBehavior("What time is it")
    print(txt)
