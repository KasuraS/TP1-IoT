import RPi.GPIO as GPIO
import time 

LED_R = 16
LED_O = 20
LED_G = 21

BUZZ = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.LOW)

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_O, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

GPIO.output(LED_R, GPIO.LOW)
GPIO.output(LED_O, GPIO.LOW)
GPIO.output(LED_G, GPIO.LOW)

try:
	while True:
		i = 3
		GPIO.output(LED_R, GPIO.HIGH)
		while i > 0:
			GPIO.output(BUZZ, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(BUZZ, GPIO.LOW)
			time.sleep(0.5)
			i-=1
		time.sleep(7)
		GPIO.output(LED_R, GPIO.LOW)
		i = 2
		GPIO.output(LED_G, GPIO.HIGH)
		while i > 0:
			GPIO.output(BUZZ, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(BUZZ, GPIO.LOW)
			time.sleep(0.5)
			i-=1
		time.sleep(8)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_O, GPIO.HIGH)
		GPIO.output(BUZZ, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(BUZZ, GPIO.LOW)
		time.sleep(0.5)
		time.sleep(2)
		GPIO.output(LED_O, GPIO.LOW)
		
except KeyboardInterrupt:
	GPIO.cleanup()