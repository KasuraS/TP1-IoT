import RPi.GPIO as GPIO
import time 

LED_1 = 16
LED_2 = 20
LED_3 = 21

BTN_1 = 17
BTN_2 = 27
BTN_3 = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

GPIO.setup(BTN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED_1, GPIO.LOW)
GPIO.output(LED_2, GPIO.LOW)
GPIO.output(LED_3, GPIO.LOW)

try:
	while True:
		btn_state_1 = GPIO.input(BTN_1)
		btn_state_2 = GPIO.input(BTN_2)
		btn_state_3 = GPIO.input(BTN_3)
		
		if (btn_state_1 == True):
			print("btn_1 pressed...")
			if (GPIO.input(LED_1) == True):
				print("led_1 turns off")
				GPIO.output(LED_1, GPIO.LOW)
			else:
				print("led_1 turns on")
				GPIO.output(LED_1, GPIO.HIGH)
		
		if (btn_state_2 == True):
			print("btn_2 pressed...")
			if (GPIO.input(LED_2) == True):
				print("led_2 turns off")
				GPIO.output(LED_2, GPIO.LOW)
			else:
				print("led_2 turns on")
				GPIO.output(LED_2, GPIO.HIGH)

		if (btn_state_3 == True):
			print("btn_3 pressed...")
			if (GPIO.input(LED_3) == True):
				print("led_3 turns off")
				GPIO.output(LED_3, GPIO.LOW)
			else:
				print("led_3 turns on")
				GPIO.output(LED_3, GPIO.HIGH)
		
		time.sleep(0.05)

except KeyboardInterrupt:
	GPIO.cleanup()