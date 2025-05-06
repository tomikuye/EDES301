import serial
import time

# Open the serial connection to the Mac
ser = serial.Serial('/dev/ttyO4', 9600)  # Adjust to the correct port (check on Mac with `ls /dev/tty*`)

def send_keystroke(key):
    # Send the keystroke as a string (e.g., 'a', 'b', etc.)
    ser.write(key.encode())

# Send a keystroke
"""send_keystroke('a')
time.sleep(0.1)  # Small delay before sending the next key
send_keystroke('b')"""

ser.close()