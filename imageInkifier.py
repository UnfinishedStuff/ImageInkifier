# Needed for all the image processing
from PIL import Image, ImageEnhance
# Needed for command line arguments (abortive exits and GIMP commands)
import os, sys


class inkifier:

    # The constructor for the class
    def __init__(self, model, colour, setupDisplay=True):
        # Check which model of Inky board is being used
        if model == "InkyWHAT":
            from inky import InkyWHAT
            self.model = "InkyWHAT"
        elif model == "InkyPHAT":
            from inky import InkyPHAT
            self.model = "InkyPHAT"
        else:
            sys.exit("ERROR, model must be InkyPHAT or InkyWHAT, value given\
 was " + str(model))

        # Check which colour of Inky board is being used
        if colour == "red":
            self.colour = "red"
        elif colour == "yellow":
            self.colour = "yellow"
        elif colour == "black":
            self.colour = "black"
        else:
            sys.exit("ERROR, colour must be red, yellow or black, value given\
 was " + str(colour))

        # By default creating an instance of the class will also instantiate
        # the InkyPHAT/WHAT.  If for some reason you don't want this, you
        # can pass setupDisplay=False when instantiating the class.
        if setupDisplay == True:
            # Instantiate the PHAT/WHAT
            if self.model == "InkyWHAT":
                self.inkyDisplay = InkyWHAT(self.colour)
            elif self.model == "InkyPHAT":
                self.inkyDisplay = InkyPHAT(self.colour)


    # A function to open an image from a file, process it and display it
    def show_image(self, imageFile, brightness=1, contrast=1, sharpness=1):

        # Try to open the image to be processed
        try:
            self.img = Image.open(imageFile)
        # If the image can't be opened inform the user and exit the function
        except:
            print("Couldn't open the image, are you sure the file path is correct\
and it's an image file?")
            return

        # Process the image for palette, brightness, contrast and sharpness
        processedImage = self.process_image(self.img, brightness, contrast, sharpness)

        # Set the processed image as the inkyWHAT image
        self.inkyDisplay.set_image(processedImage)

        # Show the image on the inkyWHAT
        self.inkyDisplay.show()


    # Convert an image to the inky palette, do brightness etc. if asked
    def process_image(self, imageObject, brightness, contrast, sharpness):

        processingImg = imageObject

        # If the image isn't JPEG format then convert it to RGB
        # (the palette conversion may fail otherwise)
        if processingImg.format != "JPEG":
            processingImg = processingImg.convert("RGB")

        # If a brightness value was given then brighten the image
        if brightness != 1:
            print("Brightening!")
            if (brightness > 0) and (brightness < 2):
                brightener = ImageEnhance.Brightness(processingImg)
                processingImg = brightener.enhance(brightness)
            else:
                print("Error, brightness must be between 0 and 2.")

        # If a sharpness value was given then sharpen the image 
        if sharpness != 1:
            print("Sharpening!")
            if (sharpness > 0) and (sharpness < 2):
                sharpener = ImageEnhance.Sharpness(processingImg)
                processingImg = sharpener.enhance(sharpness)
            else:
                print("Error, sharpness value must be between 0 and 2.")

        # If a contrast value was given then adjust the contrast
        if contrast != 1:
            print("Contrasting!")
            if (contrast > 0) and (contrast < 2):
                contraster = ImageEnhance.Contrast(processingImg)
                processingImg = contraster.enhance(contrast)
            else:
                print("Error, contrast value must be between 0 and 2.")

        # If the image isn't 300x400 pixels then resize it
        width, height = processingImg.size
        if (width != self.inkyDisplay.WIDTH) or (height != self.inkyDisplay.HEIGHT):
            processingImg = processingImg.resize((self.inkyDisplay.WIDTH, self.inkyDisplay.HEIGHT))

        # Save the image so that it can be passed to GIMP for processing
        processingImg.save("/tmp/imageInkifierTempImage.jpg")

        # Convert to an inkyWHAT-compatible format with GIMP and save as convertedImage
        print("Converting")
        os.system("gimp-console -b \'(script-fu-inkify \"/tmp/imageInkifierTempImage.jpg\" \"/tmp/imageInkifierConvertedImage.png\" )\' -b \'(gimp-quit 0)\'")
        print("Done converting!  Displaying!")

        # Open the converted image as a PIL image object
        processingImg = Image.open("/tmp/imageInkifierConvertedImage.png")

        # Remove the pre-conversion image file
        os.remove("/tmp/imageInkifierTempImage.jpg")

        # Remove the converted image file
        os.remove("/tmp/imageInkifierConvertedImage.png")

        # Return the converted image file
        return(processingImg)
