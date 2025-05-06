import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Open the serial connection (adjust to the correct port)
ser = serial.Serial('/dev/tty.usbserial-0001', 115200)  # Adjust to your serial port
release_key = "0"


def send_keystroke(key, release_key):
    # Send the keystroke using AppleScript through osascript
    if(key != '0'):
        keyboard.press(key)
        release_key = key
    else:
        keyboard.release(release_key)

# Continuously listen for data from PocketBeagle
try:
    while True:
        if ser.in_waiting > 0:
            key = ser.read().decode()  # Read a byte and decode to string
           # print(key)  # Send the keystroke to Mac
            send_keystroke(key, release_key)
            
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

