import RPi.GPIO as GPIO
from time import sleep 

motorspeed_pin = 40

DIRA = 36
DIRB = 38
pwmPin = any


GPIO.setwarnings(False)

def MotorInit():
    global pwmPin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorspeed_pin, GPIO.OUT)
    GPIO.setup(DIRA, GPIO.OUT)
    GPIO.setup(DIRB, GPIO.OUT)
    pwmPin = GPIO.PWM(motorspeed_pin, 100)
    pwmPin.start(0)
    

def TurnMotorOn():
    pwmPin.ChangeDutyCycle(100)
    GPIO.output(DIRA, GPIO.HIGH)
    GPIO.output(DIRB, GPIO.LOW)
    print('motor on')

def TurnMotorOff():
    pwmPin.ChangeDutyCycle(0)
    GPIO.output(DIRA, GPIO.LOW)
    GPIO.output(DIRB, GPIO.LOW)
    print('motor off')

if __name__ == "__main__":
    MotorInit()
    TurnMotorOn()
    sleep(4)
    TurnMotorOff()
    
   
