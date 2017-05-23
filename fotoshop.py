import os
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

class Deformer:
    def getmesh(self, im):
        x, y = im.size
        return [((0, 0, x, y), (0, 0, x, 0, x, y, y, 0))]
  

class Fotoshop:

    def __init__(self):
        self.cwd = os.getcwd()
        self.deformer = Deformer()


    ''' write the text passed over the image'''
    def writeWatermark(self,im,text2Write):

        #load the font from the fonts folder
        ft = ImageFont.load(self.cwd + "/pilfonts/helvB24.pil")

        #get the size of the text to write
        wh = ft.getsize(text2Write)
        draw = ImageDraw.Draw(im)
        # draw.line((0, 0) + im.size, fill=(255, 255, 255))
        # draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
        wh = ft.getsize(text2Write)
        # draw.text((im.size[0]/2 - wh[0]/2, im.size[1]/2 + 20), text2Write,fill=(0, 0, 0), font=ft)
        draw.text((40, im.size[1]-60), text2Write,fill=(0, 0, 0), font=ft)
        del draw  
        return im

    def overlayImage(self,image,overlay):
        sizeImage = image.size
        #print(sizeImage)

        sizeOverlay = overlay.size
        #print(sizeOverlay)

        box = (sizeImage[0]-sizeOverlay[0]-10,sizeImage[1]-sizeOverlay[1]-10)
        image.paste(overlay,box,overlay)
        return image

    #make it black and white
    def makeBlackAndWhite(self,image):
        return image.convert('L')

    # image filters
    def addSpecialEffects(self,image):
        #image = image.filter(ImageFilter.BLUR)
        #image = image.filter(ImageFilter.FIND_EDGES)
        image = image.filter(ImageFilter.EMBOSS)
        return image

    def deformImage(self,image):
        return ImageOps.deform(image, self.deformer)

    def addFrame(self,image):
        return ImageOps.expand(image,border=15,fill='red')

