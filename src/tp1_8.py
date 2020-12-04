import RPi.GPIO as GPIO
import time 
import random

secret = random.random() * 20
nb_attempts = 4

LED_G = 16
LED_R = 20
LED_B = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

GPIO.output(LED_G, GPIO.LOW)
GPIO.output(LED_R, GPIO.LOW)
GPIO.output(LED_B, GPIO.LOW)

try:
	while True:
		x_input = int(input("Put a number between 0 and 20: ")
		if (x_input == secret):
			print("Found it!!")
			GPIO.output(LED_G, GPIO.HIGH)
			time.sleep(10)
			return
		else:
			nb_attempts-=1
			if (nb_attempts != 0):
				print("You have "+str(nb_attempts)+" attempts...")
				time.sleep(2)
			else:
				print("You lost!! The secret number is "+str(secret))
				time.sleep(3)
				return
				
			if (x_input < secret):
				print("Try a bit higher...")
				i = 5
				while i > 0:
					GPIO.output(LED_R, GPIO.HIGH)
					time.sleep(0.5)
					GPIO.output(LED_R, GPIO.LOW)
					time.sleep(0.5)
					i-=1
			else:
				print("Try a bit lower...")
				j = 5
				while j > 0:
					GPIO.output(LED_B, GPIO.HIGH)
					time.sleep(0.5)
					GPIO.output(LED_B, GPIO.LOW)
					time.sleep(0.5)
					j-=1
		
except KeyboardInterrupt:
	GPIO.cleanup()