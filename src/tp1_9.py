import RPi.GPIO as GPIO
import time 

BUZZ = 17
BTN = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.LOW)

GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		btn_state = GPIO.input(BTN)
		if (btn_state == True):
			print("btn pressed...")
			GPIO.output(BUZZ, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(BUZZ, GPIO.LOW)
			time.sleep(0.5)
		
except KeyboardInterrupt:
	GPIO.cleanup()