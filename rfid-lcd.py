import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
import time
import drivers

# Initialize the RFID reader
rfid = SimpleMFRC522()

# Initialize the LCD display
display = drivers.Lcd()

try:
    while True:
        # Scan for RFID tags
        print('Scanning for a card...')
        id = rfid.read()
        
        # Clear the LCD display
        display.lcd_clear()
        
        # Display the RFID tag ID on the LCD
        display.lcd_display_string('RFID Tag ID:', 1)
        display.lcd_display_string(str(id), 2)
        
        # Wait for a few seconds before scanning the next tag
        time.sleep(2)
        
except KeyboardInterrupt:
    print('Cleaning up!')
    gpio.cleanup()
