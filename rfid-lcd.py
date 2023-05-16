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
        id, text = rfid.read()
        
        # Clear the LCD display
        display.lcd_clear()
        
        # Display the RFID tag ID on the LCD
        display.lcd_display_string(str(id), 2)
        print('ID: ',id)
        
        # Wait for a few seconds before scanning the next tag
        time.sleep(2)
        
except KeyboardInterrupt:
    print('Cleaning up!')
    gpio.cleanup()
