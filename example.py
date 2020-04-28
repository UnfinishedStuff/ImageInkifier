#!/usr/bin/env python3

import argparse
import imageInkifier

# A parser for the command line arguments
parser = argparse.ArgumentParser(description="Interface with ImageInkifier.")

# Argument for the image
parser.add_argument("-image", metavar="i", type=str, required=True,
help="Location of the file to display")

# Argument for the brightness
parser.add_argument("-brightness", metavar="b", type=float,
 help="A brightness value between 0 and 2.")

# Argument for the contrast
parser.add_argument("-contrast", metavar="c", type=float,
 help="A contrast value between 0 and 2.")

# Argument for the sharpness
parser.add_argument("-sharpness", metavar="s", type=float,
 help="A sharpness value between 0 and 2.")

# Argument for the Inky display model
parser.add_argument("-model", metavar="m", type=str, required=True,
 help="The model of Inky display to be used.  Should be 'InkyPHAT' or\
 'InkyWHAT'.")

# Argument for the Inky display colour
parser.add_argument("-type", metavar="t", type=str, required=True,
 help="The type of Inky display to be used.  Should be 'black', 'red', or\
 'yellow'.") 

# Process the arguments
args = parser.parse_args()


# Set up the display
inky = imageInkifier.inkifier(args.model, args.type)


# Set the value for the brightness variable
if args.brightness == None:
    brightValue = 1
else:
    brightValue = args.brightness

# Set the value for the sharpness variable
if args.sharpness == None:
    sharpValue = 1
else:
    sharpValue = args.sharpness

# Set tje value for the contrast variable
if args.contrast == None:
    contrastValue = 1
else:
    contrastValue = args.contrast

inky.show_image(args.image, brightValue, contrastValue, sharpValue)
