import os
from PIL import Image
from fotoshop import Fotoshop


def testWriteWatermark(image):
    image = fotoshop.writeTextOver(image,"fotoshop")
    # display image on the screen and save to out folder
    fotoshop.showAndSave(image, 'fsWaterMark')


def testMakeBlackAndWhite(image):
    image = fotoshop.makeBlackAndWhite(image)
    # display image on the screen and save to out folder
    fotoshop.showAndSave(image, 'fsBlacNwhite')


def testAddSpecialEffects(image):
    image = fotoshop.addSpecialEffects(image)
    # display image on the screen and save to out folder
    fotoshop.showAndSave(image, 'fsSpecialEffects')


def testOverlayImage(image,overlay):
    image = fotoshop.overlayImage(image,overlay)
    # display image on the screen and save to out folder
    fotoshop.showAndSave(image, 'fsOverlay')
    del image

def testDeformImage(image):
    image = fotoshop.deformImage(image)
    # display image on the screen and save to out folder
    fotoshop.showAndSave(image, 'fsDeform')

def testAddFrame(image):
    image = fotoshop.addFrame(image,'blue',15)
    # display image on the screen
    fotoshop.showAndSave(image, 'fsFrame')

def testFrameOverlayAndWaterMark(image,overlay,textWatermark='fotoshop'):
    image = fotoshop.addFrame(image,'red',25)
    image = fotoshop.overlayImage(image,overlay)
    image = fotoshop.writeTextOver(image,textWatermark)
    fotoshop.showAndSave(image, 'fsFrameWatermarkNoverlay')

def testAddSpecialEffectsWithOverLayAndText(image,overlay,overlaytext):
    image = fotoshop.addSpecialEffects(image)
    image = fotoshop.writeTextOver(image,overlaytext,'WHITE')
    image = fotoshop.overlayImage(image,overlay)
    fotoshop.showAndSave(image,'fsEffectsCombo')

''' main test method that calls various test method '''
def runTestSuite():

    # open image to manipulate
    image = Image.open(cwd + "/Images/big-mac-burger.jpg")
    #open overlay image
    overlay = Image.open(cwd + "/Images/mac-logo-transparent.png")

    #call the tests one by one
    testFrameOverlayAndWaterMark(image, overlay, 'fotoshop magic')
    testAddSpecialEffectsWithOverLayAndText(image,overlay,'fotoshop magic')
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