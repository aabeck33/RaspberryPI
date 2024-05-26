from gpiozero import Buzzer, Button, LED
from time import sleep
from signal import pause

buzzer = Buzzer(17)
led = LED(4)
button = Button(2)

buzzer.beep()
led.blink(on_time=10,off_time=10,n=5)
sleep(2)

while True:
	if button.is_pressed:
		buzzer.on()
		led.off()
	else:
		led.blink(on_time=10,off_time=10)
		buzzer.off()
pause()

GSP1RMCPRXFRER_BR_DVD
