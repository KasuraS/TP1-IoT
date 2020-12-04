import RPi.GPIO as GPIO
import time 

LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
	x = input("Enter a value: ")
	FRESH = int(x)
	while True:
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(FRESH)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(FRESH)

except KeyboardInterrupt:
	GPIO.cleanup()