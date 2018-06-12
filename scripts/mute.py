import alsaaudio
#m = alsaaudio.Mixer()
for i in range(0,5):
    m = alsaaudio.Mixer(control='IEC958',id=i) # $ amixer
    print '-'*70
    print 'mixer     : ' + m.mixer()
    print 'id        : ' + str(m.mixerid())
    print 'switchcap : ' + str(m.switchcap())
    print 'setmute   : '
    m.setmute(1)
    print 'getmute   : ' + str(m.getmute())
    print 'volume    : ' + str(m.getvolume()) # return volume list
    #print m.setvolume(100, alsaaudio.MIXER_CHANNEL_ALL) # None
    #print m.getvolume() # return volume list
