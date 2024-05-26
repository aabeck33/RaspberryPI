from gpiozero import Button, LED, Buzzer
from time import sleep
from signal import pause

am = LED(17)
vm = LED(4)
vd = LED(27)
bt = Button(2)
bz = Buzzer(21)

def blink_am():
	bz.on()	
	while bt.is_pressed:
		am.on()
		sleep(1)
		am.off()
		sleep(1)
	bz.off()

while True:
	if bt.is_pressed:
		blink_am()
	else:
		am.on()
	sleep(1)
	am.off()
	vm.on()
	sleep(3)
	vm.off()
	vd.on()
	sleep(3)
	vd.off()
pause()
