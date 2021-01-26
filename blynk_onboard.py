import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    print("Toggle")
    utime.sleep(1)