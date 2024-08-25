from machine import Pin
import time

# Initialize the onboard LED on GPIO 25
led = Pin(25, Pin.OUT)

# Blink the LED
while True:
    led.value(1)   # Turn on the LED
    time.sleep(1)  # Wait for 1 second
    led.value(0)   # Turn off the LED
    time.sleep(1)  # Wait for 1 second

