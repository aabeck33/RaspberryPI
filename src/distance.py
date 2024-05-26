from gpiozero import DistanceSensor, Buzzer
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=20)
buzzer = Buzzer(2)

while True:
	print(ultrasonic.distance)
	if (ultrasonic.distance > 2):
		buzzer.on()
	else:
		buzzer.off()
	sleep(2)

