import RPi.GPIO as GPIO
import time 

BTN = 17
LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		btn_state = GPIO.input(BTN)
		if (btn_state == True):
			print("btn not pressed...")
			GPIO.output(LED, GPIO.LOW)
		else:
			print("btn pressed...")
			GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.05)

except KeyboardInterrupt:
	GPIO.cleanup()