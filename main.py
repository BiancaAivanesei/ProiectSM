from flask import Flask, render_template
from flask_socketio import SocketIO
from scripts.OneLed import TurnON,TurnOFF, BlinkLed, DimmLed
from scripts.RGBLed import DimmTwo, DimmThree, duoBlink, allBlink, duoON, allON, duoOFF, allOFF
from scripts.DHT11 import TempInit, getTemperature
from scripts.Motor import MotorInit, TurnMotorOn, TurnMotorOff
from time import sleep
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
app = Flask(__name__)
socketio = SocketIO(app)


#pin numbering

RGBBlue=19
RGBRed=13
RGBGreen=35
red=12
blue=18
green=10
yellow=8
white=16

#setting output pins for all the leds
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(white, GPIO.OUT)
GPIO.setup(RGBRed, GPIO.OUT)
GPIO.setup(RGBBlue, GPIO.OUT)
GPIO.setup(RGBGreen, GPIO.OUT)

#initialize the other components
TempInit()
MotorInit()


@socketio.on('send_message')
def send_message(data):
    socketio.emit('receive_message_server', data)

def LightUp(msg):
    msg=msg.upper()
    if 'TEMP' or 'TEMPERATURE' in msg:
        response= "The temperature is: "+str(getTemperature())
    if 'RED' in msg:
        response = "Red led "
        if 'BLINK' in msg:
            response += "BLINKs"
            BlinkLed(red)
        if 'ON' in msg:
            response += "ON"
            TurnON(red)
        if 'OFF' in msg:
            response += "OFF"
            TurnOFF(red)
        if 'DIMM' in msg:
            response += "DIMMs"
            DimmLed(red)
    if 'BLUE' in msg:
        response = "Blue led "
        if 'BLINK' in msg:
            response += "BLINKs"
            BlinkLed(blue)
        if 'ON' in msg:
            response += "ON"
            TurnON(blue)
        if 'OFF' in msg:
            response += "OFF"
            TurnOFF(blue)
        if 'DIMM' in msg:
            response += "DIMMs"
            DimmLed(blue)
    if 'WHITE' in msg:
        response = "White led "
        if 'BLINK' in msg:
            response += "BLINK"
            BlinkLed(white)
        if 'ON' in msg:
            response += "ON"
            TurnON(white)
        if 'OFF' in msg:
            response += "OFF"
            TurnOFF(white)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmLed(white)
    if 'YELLOW' in msg:
        response = "Yellow led "
        if 'BLINK' in msg:
            response += "BLINK"
            BlinkLed(yellow)
        if 'ON' in msg:
            response += "ON"
            TurnON(yellow)
        if 'OFF' in msg:
            response += "OFF"
            TurnOFF(yellow)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmLed(yellow)
    if 'GREEN' in msg:
        response = "Green led "
        if 'BLINK' in msg:
            response += "BLINK"
            BlinkLed(RGBGreen)
        if 'ON' in msg:
            response += "ON"
            TurnON(green)
        if 'OFF' in msg:
            response += "OFF"
            TurnOFF(green)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmLed(green)
    if 'MOTOR' in msg:
        response = "Motor "
        if 'ON' in msg:
            response += "ON"
            TurnMotorOn()
        if 'OFF' in msg:
            response += "OFF"
            TurnMotorOff()
    if 'PURPLE' in msg:
        response = "Purple led "
        if 'BLINK' in msg:
            response += "BLINK"
            duoBlink(RGBRed, RGBBlue)
        if 'ON' in msg:
            response += "ON"
            duoON(RGBRed, RGBBlue)
        if 'OFF' in msg:
            response += "OFF"
            duoOFF(RGBRed, RGBBlue)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmTwo(RGBRed, RGBBlue)
    if 'BROWN' in msg:
        response = "Brown led "
        if 'BLINK' in msg:
            response += "BLINK"         
            duoBlink(RGBRed, RGBGreen)
        if 'ON' in msg:
            response += "ON"
            duoON(RGBRed, RGBGreen)
        if 'OFF' in msg:
            response += "OFF"
            duoOFF(RGBRed, RGBGreen)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmTwo(RGBRed, RGBGreen)
    if 'CYAN' in msg:
        response = "Cyen led "
        if 'BLINK' in msg:
            response += "BLINK"
            duoBlink(RGBGreen, RGBBlue)
        if 'ON' in msg:
            response += "ON"
            duoON(RGBGreen, RGBBlue)
        if 'OFF' in msg:
            response += "OFF"
            duoOFF(RGBGreen, RGBBlue)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmTwo(RGBGreen, RGBBlue)
    if 'RGB' in msg:
        response = "RGB led "
        if 'BLINK' in msg:
            response += "BLINK"
            allBlink(RGBGreen, RGBBlue, RGBRed)
        if 'ON' in msg:
            response += "ON"
            allON(RGBGreen, RGBBlue, RGBRed)
        if 'OFF' in msg:
            response += "OFF"
            allOFF(RGBGreen, RGBBlue, RGBRed)
        if 'DIMM' in msg:
            response += "DIMM"
            DimmThree(RGBGreen, RGBBlue, RGBRed)
    send_message(response)
    

@app.route('/')
def home():
    return render_template("index.html")
    

@socketio.on('send_message')
def handle_send_message_event(data):
    socketio.emit('receive_message', data)
    LightUp(data);
    


if __name__ == '__main__':
    socketio.run(app, debug=True)
    GPIO.cleanup()
