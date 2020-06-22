from time import sleep 
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)


def DimmTwo(firstLed, secondLed):
    firstLed = GPIO.PWM(firstLed, 1000) 
    secondLed= GPIO.PWM(secondLed, 1000)
    firstLed.start(0)
    secondLed.start(0)
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)

            
def DimmThree(firstLed, secondLed, thirdLed):
    firstLed = GPIO.PWM(firstLed, 1000) 
    secondLed = GPIO.PWM(secondLed, 1000) 
    thirdLed = GPIO.PWM(thirdLed, 1000)
    firstLed.start(0)
    secondLed.start(0)
    thirdLed.start(0)
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)
    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)


def duoBlink(pin1, pin2):
    i=0
    while i<10:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        sleep(1)
        i=i+1
                
def allBlink(pin1, pin2, pin3):
    i=0
    while i<10:
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(pin3, GPIO.HIGH)
        sleep(1)
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.LOW)
        sleep(1)
        i=i+1

def duoON(pin1, pin2):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    
def allON(pin1, pin2, pin3):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.HIGH)

def duoOFF(pin1, pin2):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
                      
def allOFF(pin1, pin2, pin3):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW) 
