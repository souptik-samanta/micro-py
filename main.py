from machine import Pin
import time

# Initialize the onboard LED on GPIO 25
led = Pin(19, Pin.OUT)

# Blink the LED
while True:
    led.off()   # Turn on the LED
    time.sleep(1)  # Wait for 1 second
    led.on()   # Turn off the LED
    time.sleep(1)  # Wait for 1 second


