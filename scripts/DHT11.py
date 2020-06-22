import RPi.GPIO as GPIO
import Adafruit_DHT
from Motor import MotorInit, TurnMotorOn, TurnMotorOff

type = Adafruit_DHT.DHT11

dht11 = 22

def TempInit():
    global dht11
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dht11, GPIO.IN)

def getTemperature():
    global type
    global dht11
    humidity, temperature = Adafruit_DHT.read_retry(type, dht11)
    return temperature
            
if __name__ == "__main__":
    TempInit()
    print(getTemperature())
    
    
    
    
    
    