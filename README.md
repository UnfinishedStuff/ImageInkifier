This is a collection of code for converting and displaying images on Pimoroni's [InkyWHAT](https://shop.pimoroni.com/products/inky-what?variant=13590497624147) eInk HAT for the Raspberry Pi.

EInk displays use tiny particles of pigment which are pulled to the front of the screen by electrical charges.  This means that unlike most screen technologies, eInk screens don't emit light themselves: ambient light reflects off the pigment particles, giving it an appearance not entirely different to pigment particles on paper.  

Because Eink uses a very different technology to most display types images need a bit of processing before they can be shown properly.  Pimoroni describe how to do this manually in thier [Getting Started with InkyPHAT Guide](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat) but this script automates that process.

Currently this script uses the Pillow module to open an image file and alter the brightness, sharpness and/or contrast of the image.  The image is resized if required to fit the device, and then gets passed to GIMP ([the GNU Image Manipulation Program](https://www.gimp.org/)) which converts full-colour images into a 2- or 3-colour format compatible with Pimoroni's InkyWHAT screens.  Finally, the image is displayed on the WHAT/PHAT.

# Installation

1) Start by checking your Pi is up to date: `sudo apt-get update && sudo apt-get upgrade`.
2) Clone this Git repo: `git clone https://github.com/UnfinishedStuff/ImageInkifier.git`
3) Install Pimoroni's Inky module: `curl https://get.pimoroni.com/inky | bash`
4) Install GIMP: `sudo apt-get install gimp`
5) We need to add some of the files in the Git repo into GIMP's folders, but they won't be created until GIMP is run at least once.  Try running the example script (you'll need to pass it an image to use).
6) Copy InkyPalette.gpl from the Git repo to `~/.config/GIMP/2.10/palettes`.
7) Copy inkify.scm to `~/.config/GIMP/2.10/scripts`.

That's it! Now try running the test script.....
