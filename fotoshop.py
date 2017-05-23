import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps


''' write the text passed over the image'''
def writeWatermark(im,text2Write):

    #load the font from the fonts folder
    font = ImageFont.load(cwd + "/pilfonts/courR24.pil")

    #get the size of the text to write
    wh = font.getsize(text2Write)
    draw = ImageDraw.Draw(im)
    # draw.line((0, 0) + im.size, fill=(255, 255, 255))
    # draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
    wh = font.getsize(text2Write)
    # draw.text((im.size[0]/2 - wh[0]/2, im.size[1]/2 + 20), text2Write,fill=(0, 0, 0), font=ft)
    draw.text((10, im.size[1]-40), text2Write,fill=(0, 0, 0), font=font)
    del draw  
    return im
    



''' main function that calls various functions '''
def __main():
    # open image to manipulate
    image = Image.open(cwd + "/Images/big-mac-burger.jpg")

    #open overlay image
    overlay = Image.open(cwd + "/Images/mac-logo-transparent.png")

    image = writeWatermark(image,"using fotoshop")
    #image = makeBlackAndWhite(image)
    #image = addSpecialEffects(image)
    #image = overlayImage(image,overlay)
    #image = deformImage(image)
    #image = addFrame(image)
    # display image on the screen
    image.show()
    
    
cwd = os.getcwd()
__main()
