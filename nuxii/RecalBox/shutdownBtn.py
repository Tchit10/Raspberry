#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time as time
import os
import signal
# Define mode to access GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# pin id for the shutdown button
GPIO_shutdown=3
GPIO_LED_BTN=4
GPIO_LED_VERTE=27
GPIO_LED_ROUGE=10

# GPIO_shutdown will be an input pin
GPIO.setup(GPIO_shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# GPIO_LED_BTN will be an output pin
GPIO.setup(GPIO_LED_BTN, GPIO.OUT)
GPIO.output(GPIO_LED_BTN, GPIO.HIGH)

# GPIO_LED_ROUGE and GPIO_LED_VERTE will be output pins
GPIO.setup(GPIO_LED_ROUGE, GPIO.OUT)
GPIO.setup(GPIO_LED_VERTE, GPIO.OUT)
GPIO.output(GPIO_LED_ROUGE, GPIO.HIGH)

# Handler to stop the process
def signal_handler(signal, frame):
    GPIO.cleanup()
    exit(0)

# Define what to do when the shutdown button is pressed
def funcShutdown(channel):
    start_time = time.time()
    intSeconds = 0
    # How long to wait for the button
    maxWaitPushButton = 2
    while intSeconds < maxWaitPushButton and GPIO.input(channel) == GPIO.LOW :
         intSeconds = time.time() - start_time
         time.sleep(0.1)
    if intSeconds >= maxWaitPushButton:
        GPIO.output(GPIO_LED_BTN, GPIO.LOW)
	GPIO.output(GPIO_LED_ROUGE, GPIO.LOW)
        GPIO.cleanup()
        os.system('sudo halt')
        #exit()  

# Add a signal handler for the SIGTERM signal
signal.signal(signal.SIGTERM, signal_handler)
# Wait for the shutdown button to be pressed
GPIO.add_event_detect(GPIO_shutdown, GPIO.FALLING, callback=funcShutdown, bouncetime=300) 

# Loop
while 1:
    time.sleep(0.2)
