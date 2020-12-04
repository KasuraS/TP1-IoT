import RPi.GPIO as GPIO
import time 

BTN = 17
LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		btn_state = GPIO.input(BTN)
		if (btn_state == True):
			print("btn pressed...")
			led_state = GPIO.input(LED)
			if (led_state == True):
				print("led turns off")
				GPIO.output(LED, GPIO.LOW)
			else:
				print("led turns on")
				GPIO.output(LED, GPIO.HIGH)

		time.sleep(0.05)

except KeyboardInterrupt:
	GPIO.cleanup()