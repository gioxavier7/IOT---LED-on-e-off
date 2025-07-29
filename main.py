from machine import Pin
from utime import sleep

print("hello, world!")

led = Pin(15, Pin.OUT)

while True:
  led.on()
  print("led ON")
  sleep(0.5)
  led.off()
  print("led OFF")
  sleep(0.5)
