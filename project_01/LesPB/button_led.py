import button as BUTTON
import Adafruit_BBIO.GPIO as GPIO
import os
import serial
import time

GPIO.setup("P2_18", GPIO.OUT)
GPIO.setup("P2_20", GPIO.OUT)
GPIO.setup("P2_22", GPIO.OUT)

GPIO.setup("P2_30", GPIO.OUT)
GPIO.setup("P2_32", GPIO.OUT)
GPIO.setup("P2_34", GPIO.OUT)


GPIO.output("P2_18", GPIO.HIGH)
GPIO.output("P2_20", GPIO.HIGH)
GPIO.output("P2_22", GPIO.HIGH)

GPIO.output("P2_30", GPIO.HIGH)
GPIO.output("P2_32", GPIO.HIGH)
GPIO.output("P2_34", GPIO.HIGH)


# ------------------------------------------------------------------------
# Macros nad FUnctions
# ------------------------------------------------------------------------
#ser = serial.Serial('/dev/ttyO4', 9600) 

def send_keystroke(key):
    ser = serial.Serial('/dev/ttyO4', 115200) 
    # Send the keystroke as a string (e.g., 'a', 'b', etc.)
    ser.write(key.encode())
    ser.close()
    


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

"""
First led is common anode
"""


if __name__ == '__main__':
    try:
        print("Program Start")
        green_btn =  BUTTON.Button("P2_10", press_low=False)
        red_btn =  BUTTON.Button("P2_8", press_low=False)
        
        while(1):
            if(green_btn.is_pressed()):
                #print("presed")
                send_keystroke('A') # Send/Press A
                print("pressed")
                GPIO.output("P2_20", GPIO.LOW)
                GPIO.output("P2_22", GPIO.HIGH)
                GPIO.output("P2_18", GPIO.HIGH)
            elif(not green_btn.is_pressed()):
                send_keystroke('0')
                GPIO.output("P2_18", GPIO.HIGH)
                GPIO.output("P2_20", GPIO.HIGH)
                GPIO.output("P2_22", GPIO.HIGH)
            if(red_btn.is_pressed()):
                print("rpresed")
                send_keystroke('B') #Send/press b
                GPIO.output("P2_30", GPIO.LOW)
                GPIO.output("P2_32", GPIO.HIGH)
                GPIO.output("P2_34", GPIO.HIGH)
            elif(not red_btn.is_pressed()):
                send_keystroke('0')
                GPIO.output("P2_30", GPIO.HIGH)
                GPIO.output("P2_32", GPIO.HIGH)
                GPIO.output("P2_34", GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.output("P2_18", GPIO.HIGH)
        GPIO.output("P2_20", GPIO.HIGH)
        GPIO.output("P2_22", GPIO.HIGH)
        GPIO.output("P2_30", GPIO.HIGH)
        GPIO.output("P2_32", GPIO.HIGH)
        GPIO.output("P2_34", GPIO.HIGH)
        ser.close()