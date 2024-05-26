import _thread               # baixo nível
from threading import Thread # alto ńível
import time
from gpiozero import LED
from time import sleep
from gpiozero import Button

#run_fibs()
#run_fibs_with_threads()


def led_one():
        led.on()
        sleep(1)
        led.off()
        sleep(1)


def led_two():
        led2.on()
        sleep(1)
        led2.off()
        sleep(1)


def button_one():
        button.wait_for_press()
        print("You pushed me")
        sleep(2)

# Usando _thread
def run_fibs_with_threads():
    _thread.start_new_thread(test_fib, (35, ))
    _thread.start_new_thread(test_fib, (10, ))
    _thread.start_new_thread(test_fib, (30, ))
    time.sleep(15)

"""
for i in range(0, 36, 5):
    t = Thread(target=test_fib, args=(i, ))
    t.start()
"""
led = LED(17)
led2 = LED(27)
button = Button(2)
while True:
	_thread.start_new_thread(led_one,())
	_thread.start_new_thread(led_two,())
	_thread.start_new_thread(button_one,())
	time.sleep(2)
#time.sleep(15)
