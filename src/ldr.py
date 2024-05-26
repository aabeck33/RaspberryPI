from gpiozero import LightSensor, Buzzer
from time import sleep

ldr = LightSensor(4)

while True:
	print(ldr.value * 100)
	sleep(3)

