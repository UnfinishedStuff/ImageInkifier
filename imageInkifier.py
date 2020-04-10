# Needed for displaying images on the inkyWHAT
from inky import InkyWHAT
# Needed for all the image processing
from PIL import Image, ImageEnhance
# Needed for command line arguments
import os, sys
# Needed for parsing arguments from the command line
import argparse

def inkify(image, brightness=1.0, sharpness=1.0, contrast=1.0):
    # Try to open the image to be processed, if it fails quit the program
    try:
        img = Image.open(image)
    except:
        print("Couldn't open the image, are you sure the file path is correct\
    and it's an image file?")
        sys.exit()

    # If the image isn't JPEG format then convert it to RGB
    # (the palette test fails otherwise)
    if img.format != "JPEG":
        img = img.convert("RGB")

    # If a brightness value was given then brighten the image
    if brightness != 1.0:
        print("Brightening!")
        if (brightness > 0) and (brightness < 2):
            brightener = ImageEnhance.Brightness(img)
            img = brightener.enhance(brightness)
        else:
            print("Error, brightness must be between 0 and 2.")

    # If a sharpness value was given then sharpen the image
    if sharpness != 1.0:
        print("Sharpening!")
        if (sharpness > 0) and (sharpness < 2):
            sharpener = ImageEnhance.Sharpness(img)
            img = sharpener.enhance(sharpness)
        else:
            print("Error, sharpness value must be between 0 and 2.")

    # If a contrast value was given then adjust the contrast
    if contrast != 1.0:
        print("Contrasting!")
        if (contrast > 0) and (contrast < 2):
            contraster = ImageEnhance.Contrast(img)
            img = contraster.enhance(contrast)
        else:
            print("Error, contrast value must be between 0 and 2.")

    # If the image isn't 300x400 pixels then resize it
    width, height = img.size
    if (img.width != 400) or (img.height != 300):
        img = img.resize((400, 300))


    # Save the image so that it can be passed to GIMP for processing
    img.save("/tmp/inkyTempImage.jpg")

    # Convert to an inkyWHAT-compatible format with GIMP and save as convertedImage
    print("Converting")
    os.system("gimp-console -b \'(script-fu-inkify \"/tmp/inkyTempImage.jpg\" \"/tmp/convertedImage.png\")\' -b \'(gimp-quit 0)\'")
    print("Done converting!  Displaying!")

    # Open the converted image as a PIL image object
    img = Image.open("/tmp/convertedImage.png")
    # Remove the pre-conversion image file
    os.remove("/tmp/inkyTempImage.jpg")


    # Prep InkyWHAT and show the image
    inky_display = InkyWHAT("red")
    inky_display.set_border(inky_display.WHITE)
    # Set the converted image as the inkyWHAT image
    inky_display.set_image(img)

    # Remove the converted image file
    os.remove("/tmp/convertedImage.png")

    # Show the image on the inkyWHAT
    inky_display.show()

    print("Done!")
