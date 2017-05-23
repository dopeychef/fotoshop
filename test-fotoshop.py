import os
from PIL import Image
from fotoshop import Fotoshop


def testWriteWatermark(image):
    image = fotoshop.writeWatermark(image,"fotoshop")
    # display image on the screen
    image.show()

def testMakeBlackAndWhite(image):
    image = fotoshop.makeBlackAndWhite(image)
    # display image on the screen
    image.show()

def testAddSpecialEffects(image):
    image = fotoshop.addSpecialEffects(image)
    # display image on the screen
    image.show()

def testOverlayImage(image,overlay):
    image = fotoshop.overlayImage(image,overlay)
    # display image on the screen
    image.show()
    del image

def testDeformImage(image):
    image = fotoshop.deformImage(image)
    # display image on the screen
    image.show()

def testAddFrame(image):
    image = fotoshop.addFrame(image)
    # display image on the screen
    image.show()

def testFrameOverlayAndWaterMark(image,overlay,textWatermark='fotoshop'):
    image = fotoshop.addFrame(image)
    image = fotoshop.overlayImage(image,overlay)
    image = fotoshop.writeWatermark(image,textWatermark)
    image.show()

''' main test method that calls various test method '''
def runTestSuite():

    # open image to manipulate
    image = Image.open(cwd + "/Images/big-mac-burger.jpg")
    #open overlay image
    overlay = Image.open(cwd + "/Images/mac-logo-transparent.png")

    #call the tests one by one
    testFrameOverlayAndWaterMark(image, overlay, "fotoshop magic")
    testAddFrame(image)
    testAddSpecialEffects(image)
    testDeformImage(image)
    testMakeBlackAndWhite(image)
    testOverlayImage(image, overlay)
    testWriteWatermark(image)


# get current working directory
cwd = os.getcwd()
#initialize the Fotoshop module
fotoshop = Fotoshop()

#run all the tests
runTestSuite()