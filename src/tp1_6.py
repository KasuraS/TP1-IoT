import RPi.GPIO as GPIO
import time 

LED_R = 16
LED_O = 20
LED_G = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_O, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

GPIO.output(LED_R, GPIO.HIGH)
GPIO.output(LED_O, GPIO.LOW)
GPIO.output(LED_G, GPIO.LOW)

try:
	while True:
		time.sleep(10)
		GPIO.output(LED_R, GPIO.LOW)
		GPIO.output(LED_G, GPIO.HIGH)
		time.sleep(10)
		GPIO.output(LED_G, GPIO.LOW)
		GPIO.output(LED_O, GPIO.HIGH)
		time.sleep(3)
		GPIO.output(LED_O, GPIO.LOW)
		GPIO.output(LED_R, GPIO.HIGH)
		
except KeyboardInterrupt:
	GPIO.cleanup()