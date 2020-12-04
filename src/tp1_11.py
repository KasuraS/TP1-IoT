import RPi.GPIO as GPIO
import time 

LED = 23
LDR = 24

BUZZ = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.LOW)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

GPIO.setup(LDR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(LDR) == GPIO.HIGH:
			print("light up")
			i = 2
			while i > 0:
				GPIO.out(BUZZ, GPIO.HIGH)
				time.sleep(0.5)
				i-=1
			GPIO.output(LED, GPIO.HIGH)
		else:
			print("light down")
			GPIO.output(BUZZ, GPIO.LOW)
			GPIO.output(LED, GPIO.LOW)
		time.sleep(1)
			
except KeyboardInterrupt:
	GPIO.cleanup()