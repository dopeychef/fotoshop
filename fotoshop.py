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
        self.outFolder = self.cwd + '/Out'


    ''' write the text passed over the image'''
    def writeTextOver(self,im,text2Write,color='BLACK'):

        colr = (0, 0, 0) #default text color is black
        
        if(color == 'WHITE'):
            colr = (255, 255, 255)
        elif(color == 'RED'):
            colr = (255, 0, 0)
        elif(color == 'BLUE'):
            colr = (0, 0, 255)
        elif(color == 'GREEN'):
            colr = (0, 255, 0)

        #load the font from the fonts folder
        ft = ImageFont.load(self.cwd + "/pilfonts/helvB14.pil")

        #get the size of the text to write
        wh = ft.getsize(text2Write)
        draw = ImageDraw.Draw(im)
        # draw.line((0, 0) + im.size, fill=(255, 255, 255))
        # draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
        wh = ft.getsize(text2Write)
        # draw.text((im.size[0]/2 - wh[0]/2, im.size[1]/2 + 20), text2Write,fill=(0, 0, 0), font=ft)
        draw.text((40, im.size[1]-60), text2Write,fill=colr, font=ft)
        del draw  
        return im

    '''overlay the image over the actual image'''
    def overlayImage(self,image,overlay):
        sizeImage = image.size
        #print(sizeImage)

        sizeOverlay = overlay.size
        #print(sizeOverlay)

        box = (sizeImage[0]-sizeOverlay[0]-10,sizeImage[1]-sizeOverlay[1]-10)
        image.paste(overlay,box,overlay)
        return image

    #make yje image black and white
    def makeBlackAndWhite(self,image):
        return image.convert('L')

    # image filters for adding special effcets
    def addSpecialEffects(self,image):
        #image = image.filter(ImageFilter.BLUR)
        #image = image.filter(ImageFilter.FIND_EDGES)
        image = image.filter(ImageFilter.EMBOSS)
        return image

    '''deforms th eimage into a new one'''
    def deformImage(self,image):
        return ImageOps.deform(image, self.deformer)

    '''adds a frame of given color around the image'''
    def addFrame(self,image,color,widthOfBorder):
        return ImageOps.expand(image,border=widthOfBorder,fill=color)

    '''save the image as the file name givem'''
    def saveImage(self,image,fileName):
        image.save(self.outFolder+ '/' + fileName +'.jpg')

    '''displayes the image on screen'''
    def showImage(self,image):
        image.show()
    
    '''display and save the image'''
    def showAndSave(self, image,fileName):
        image.save(self.outFolder+  '/' + fileName + '.jpg')
        image.show()

