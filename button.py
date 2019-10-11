#!/usr/bin/env python
import os, random
import RPi.GPIO as GPIO
import time
from threading import Thread

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rndmp3 ():
	randomfile = random.choice(os.listdir("/home/pi/sound/"))
	file = ' /home/pi/sound/'+ randomfile
	os.system ('mpg123 -q' + file)

def specific ():
	specificfile = "mario-okiedokie.mp3"
	file = ' /home/pi/sound/'+ specificfile
	os.system ('mpg123 -q' + file)

def mama ():
	specificfile = "mario-mamamia.mp3"
	file = ' /home/pi/sound/'+ specificfile
	os.system ('mpg123 -q' + file)


try:
	while True:
	    GPIO.wait_for_edge(PIN, GPIO.FALLING)
	    print "Pressed"
	    start = time.time()
	    time.sleep(0.2)

	    while GPIO.input(PIN) == GPIO.LOW:
	        time.sleep(0.01)
	    length = time.time() - start
	    print length

	    if length >= 3:
	        print "Long Press"
	        Thread(target=mama).start()
	    elif length > 1:
	        print "Middle Press"
	        Thread(target=specific).start()
	    elif length > 0.02:
			print "Short Press"
			Thread(target=rndmp3).start()
		else
			print "Button was pressed to short"
		


except KeyboardInterrupt:
    GPIO.cleanup ()