import RPi.GPIO as GPIO
import time 

LED_1 = 17
LED_2 = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)

GPIO.output(LED_1, GPIO.HIGH)
GPIO.output(LED_2, GPIO.LOW)

try:
	while True:
		time.sleep(0.5)
		if (GPIO.input(LED_1) == GPIO.HIGH):
			GPIO.output(LED_1, GPIO.LOW)
			GPIO.output(LED_2, GPIO.HIGH)
		else:
			GPIO.output(LED_2, GPIO.LOW)
			GPIO.output(LED_1, GPIO.HIGH)

except KeyboardInterrupt:
	GPIO.cleanup()