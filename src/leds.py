from gpiozero import Button, LED
from time import sleep
from signal import pause

led = LED(17)
led2 = LED(4)
button = Button(2)
led2.on()

while True:
	if button.is_pressed:
		led2.off()
		led.on()
	else:
		led.off()
		led2.on()
pause()
