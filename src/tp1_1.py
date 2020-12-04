import RPi.GPIO as GPIO
import time 

LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
	while True:
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()