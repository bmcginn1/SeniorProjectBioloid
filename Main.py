#!/usr/bin/env python

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio


TJBot

Author: Brian McGinnis
Date: 6/23/17
"""

import conversation
import ledProcess
import led
import textToSpeech
import streaming
import time
import RPi.GPIO as GPIO
import time
import movements
import bioloid as bio
from subprocess import call



def main():

    stt = streaming.StreamingSTT(

        # replace with speech to text credentials username
        '030a85a9-4a06-4e21-806b-da2cf29549fb',

        # replace with speech to text credentials password
        'AP3aAaPi0TSq')

    tts = textToSpeech.TextToSpeech(

        # replace with text to speech credentials username
        '2cb70eda-ccc5-40d7-adee-91c9aa249841',

        # replace with text to speech credentials password
        'zyzBtEqo73D7')

    convo = conversation.Conversation(

        # replace with conversation credentials username
        '154b5b29-d1ca-4ff2-be09-c33c5e1d9e20',

        # replace with conversation credentials password
        'pmNftYlpvMS8',

        # replace with workspace ID.
        'da21184b-ae02-4159-9727-d994fc1bbaaf')

    bioloid = bio.Bioloid()

    # replace with robot name
    name = 'Bonnie'

    lastActiveTime = time.time()

    activeTimeCheck = True # This boolean differentiates between inactivity for 60 or 120 seconds.

   # bioloid.doBow()
    tts.speak('Hello my name is ' + name + ' I am a total Bro')


    while True:
        if all( [time.time() - lastActiveTime > 60, activeTimeCheck == True] ):
            bioloid.doSit()
            tts.speak("I have been inactive for 1 minute. After another minute, I will shut down")
            activeTimeCheck = False

        if all( [time.time() - lastActiveTime > 120, activeTimeCheck == False] ):
            tts.speak("Shutting down now.")
            call("sudo shutdown -h now", shell=True)

        """
        if(lastActiveTime - time.time() > 60): #if it is inactive for 1 min then it powers down.
            #Go home
            tts.speak("I have been inactive for 1 minute. After another minute, I will shut down")
        """
        phrase = stt.get_phrase()
        if (name in phrase) or ('bunny'in phrase) or ('body' in phrase) or ('Bani' in phrase):
            lastActiveTime = time.time() #if its name is heard then we can assume it is active
            activeTimeCheck = True
            response = convo.sendMessage(phrase)
            if '~' in response:
                processCommand(response)

            tts.speak(response)


def processCommand(response):
    '''
    if '~RED' in response:
        ledP.red()
        response = response.replace('~RED', '', 1)
    if '~ORANGE' in response:
        ledP.orange()
        response = response.replace('~ORANGE', '', 1)
    if '~YELLOW' in response:
        ledP.yellow()
        response = response.replace('~YELLOW', '', 1)
    if '~GREEN' in response:
        ledP.green()
        response = response.replace('~GREEN', '', 1)
    if '~BLUE' in response:
        print('Its Blue')
        ledP.blue()
        response = response.replace('~BLUE', '', 1)
    if '~PURPLE' in response:
        ledP.purple()
        response = response.replace('~PURPLE', '', 1)
    if '~PINK' in response:
        ledP.pink()
        response = response.replace('~PINK', '', 1)
    if '~WHITE' in response:
        ledP.white()
        response = response.replace('~WHITE', '', 1)
    if '~RAINBOW' in response:
        ledP.rainbow()
        response = response.replace('~RAINBOW', '', 1)
    if '~RAINBOWCYCLE' in response:
        ledP.rainbowCycle()
        response = response.replace('~RAINBOWCYCLE', '', 1)
    if '~MUSICPLAY' in response:
        musicP.play()
        response = response.replace('~MUSICPLAY', '', 1)
    if '~MUSICSTOP' in response:
        musicP.stop()
        response = response.replace('~MUSICSTOP', '', 1)
    if '~LEDOFF' in response:
        ledP.off()
        response = response.replace('~LEDOFF', '', 1)
    if '~ARMSTOP' in response:
        servoP.stop()
        response = response.replace('~ARMSTOP', '', 1)
    if '~ARMUP' in response:
        servoP.armUp()
        response = response.replace('~ARMUP', '', 1)
    if '~ARMDOWN' in response:
        servoP.armDown()
        response = response.replace('~ARMDOWN', '', 1)
    if '~DANCE' in response:
        servoP.wave(10)
        ledP.rainbowCycle(1, 50)
        response = response.replace('~DANCE', '', 1)
    if '~ARMANGLE' in response:
        response = response.replace('~ARMANGLE', '', 1)
        param = int(response.split("~", 1)[0])
        response = response.split("~", 1)[1]
        servoP.angle(param)
    if '~ARMWAVECOUNT' in response:
        response = response.replace('~ARMWAVECOUNTARMANGLE', '', 1)
        param = int(response.split("~", 1)[0])
        response = response.split("~", 1)[1]
        servoP.wave(param)
    if '~ARMWAVE' in response:
        servoP.wave(2)
        response = response.replace('~ARMWAVE', '', 1)
    if response == '':
        response = 'akward silence'
    '''

if __name__ == "__main__":
    main()
