#!/usr/bin/python

import argparse 

from Adafruit_Thermal import *

# Initialize parser 
parser = argparse.ArgumentParser() 
  
# Adding optional argument 
parser.add_argument("-i", "--Image", help = "Image Path") 
  
# Read arguments from command line 
args = parser.parse_args() 
  
if args.Image: 

	printer = Adafruit_Thermal("/dev/serial0", 9600, 16)

	# Print the 135x135 pixel QR code in adaqrcode.py
	printer.printBitmap(adaqrcode.width, adaqrcode.height, adaqrcode.data)
	printer.printImage();
	printer.println("Adafruit!")
	printer.feed(2)

	printer.sleep()      # Tell printer to sleep
	printer.wake()       # Call wake() before printing again, even if reset
	printer.setDefault() # Restore printer to defaults

    print("Success") 

