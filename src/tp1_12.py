import RPi.GPIO as GPIO
import time 
import random

RED = 16
BLUE = 20
GREEN = 21

BUZZ = 18

color = (RED, BLUE, GREEN)

def choice_1():
	GPIO.output(RED, GPIO.HIGH)
	return 'RED ON"
def choice_2():
	GPIO.output(RED, GPIO.LOW)
	return 'RED OFF'
def choice_3():
	GPIO.output(BLUE, GPIO.HIGH)
	return 'BLUE ON'
def choice_4():
	GPIO.output(RED, GPIO.LOW)
	return 'BLUE OFF'
def choice_5():	
	GPIO.output(GREEN, GPIO.HIGH)
	return 'GREEN ON'
def choice_6():
	GPIO.output(GREEN, GPIO.LOW)
	return 'GREEN OFF'
def choice_7():
	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.HIGH)
	return 'TURN ON ALL'
def choice_8():
	GPIO.output(RED, GPIO.LOW)
	GPIO.output(BLUE, GPIO.LOW)
	GPIO.output(GREEN, GPIO.LOW)
	return 'TURN OFF ALL'
def choice_9():
	x = int(random.random()*2)
	GPIO.output(color[x], GPIO.HIGH)
	time.sleep(0.05)
	x = int(random.random()*2)
	GPIO.output(color[x], GPIO.LOW)
	return 'RANDOM COLOR'
def choice_0():
	return 'EXIT'

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.LOW)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)

GPIO.setup(LDR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		print("Menu\n
		1- RED ON\n
		2- RED OFF\n
		3- BLUE ON\n
		4- BLUE OFF\n
		5- GREEN ON\n
		6- GREEN OFF\n
		7- TURN ON ALL\n
		8- TURN OFF ALL\n
		9- RANDOM COLOR\n
		0- EXIT\n")

		choice = input("Enter a number: ")
		
		switcher = {
		0: choice_0,
		1: choice_1,
		2: choice_2,
		3: choice_3,
		4: choice_4,
		5: choice_5,
		6: choice_6,
		7: choice_7,
		8: choice_8,
		9: choice_9
		}

		switcher.get(int(choice), "Wrong input, retry...")

		if int(choice) == 0:
			break

		time.sleep(1)
			
except KeyboardInterrupt:
	GPIO.cleanup()