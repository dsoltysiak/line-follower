from machine import Pin
from time import sleep

# print("TTP")
# led = machine.Pin(2, Pin.OUT)
#
# while True:
#     led.value(not led.value())
#     sleep(0.5)

left_sensor = Pin(13, Pin.OUT)
# right_sensor = Pin(2, Pin.OUT)
#
# left_wheel = Pin(2, Pin.IN)
# right_wheel = Pin(3, Pin.IN)
#
# if left_sensor.value() > x

while(True):
    print(f"Left sensor value:{left_sensor}")