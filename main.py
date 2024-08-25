from machine import Pin
import time

# Initialize the onboard LED on GPIO 25
led = Pin(19, Pin.OUT)
d=2.5
# Blink the LED
while True:
    led.off()   # Turn on the LED
    time.sleep(d)  # Wait for 1 second
    led.on()   # Turn off the LED
    time.sleep(d)  # Wait for 1 second

