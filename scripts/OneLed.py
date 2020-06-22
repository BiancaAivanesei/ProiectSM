import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

def TurnON(pin):
    GPIO.output(pin, GPIO.HIGH)
       
def TurnOFF(pin):
    GPIO.output(pin, GPIO.LOW)

def BlinkLed(pin):
    i=0
    while i<10:
        GPIO.output(pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin, GPIO.LOW)
        sleep(1)
        i=i+1
        
def DimmLed(pin):
    pin = GPIO.PWM(pin, 100)
    pin.start(0)
    for i in range(100): 
        pin.ChangeDutyCycle(i)
        sleep(0.015)
    for i in reversed(range(100)): 
        pin.ChangeDutyCycle(i)
        sleep(0.015)
    pin.stop()
