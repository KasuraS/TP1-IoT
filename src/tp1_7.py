import RPi.GPIO as GPIO
import time 

LED_R = 16
LED_O = 20
LED_G = 21

BTN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_O, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED_R, GPIO.HIGH)
GPIO.output(LED_O, GPIO.LOW)
GPIO.output(LED_G, GPIO.LOW)

try:
	while True:
		btn_state = GPIO.input(BTN)
		if (btn_state == True):
			if (GPIO.input(LED_R) == True):
				GPIO.output(LED_R, GPIO.LOW)
				GPIO.output(LED_G, GPIO.HIGH)

			elif (GPIO.input(LED_G) == True):
				GPIO.output(LED_G, GPIO.LOW)
				GPIO.output(LED_O, GPIO.HIGH)

			else:
				GPIO.output(LED_O, GPIO.LOW)
				GPIO.output(LED_R, GPIO.HIGH)
			
		time.sleep(0.05)
		
except KeyboardInterrupt:
	GPIO.cleanup()