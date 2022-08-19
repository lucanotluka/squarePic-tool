from PIL import Image, ImageOps
import os, sys

SIDE = 1080
SQUARE = SIDE, SIDE   #pixels, width & height
WHITE = 255, 255, 255     #RGB values

if len(sys.argv) > 1:   #at least one file as argument check
    rawIm = sys.argv[1]     #first arg is the raw image

    # TO DO
    # - ... per ogni pic nella directory
    # - centra le immagini con ImageOps.expand & x.fit

        


    #canva = Image.new(mode="RGB", size=SQUARE, color=WHITE)    #creating a WHITE SQUARE, 1080x1080 pixels, Image object
    # qui ci va un bel for
    try:
        #out = canva
        fileNm, ext = os.path.splitext(rawIm)   #name and extension of the pic, for convertion and saving
        if ext != '.jpg':
            rawIm = Image.open(rawIm)
            rawIm.save(fileNm + '.jpg')
            img = rawIm.copy()
            rawIm.close()
        else:             
            img = Image.open(rawIm)  #copying the raw img into "img" object
        
        img = ImageOps.exif_transpose(img)  #operation that saves the rotation flag of the original pic into Image object 

        width = img.width
        height = img.height

        # if width > height:  #img is horizontal
        #     if(width > SIDE):
        #         img.thumbnail(SQUARE)

        #     elif(width < SIDE):
        #         factor = float(SIDE/width)
        #         img.resize((SIDE, int(factor*height)))

        #     position = 0, int(out.height/2 - height/2)   #tuple for the upper-left corner of img when centered

        # else:   #img is vertical
        #     if(height > SIDE):
        #         img.thumbnail(SQUARE)

        #     elif(height < SIDE):
        #         factor = float(SIDE/height)
        #         img.resize((int(factor*width), SIDE))

        #     position = int(out.width/2 - width/2), 0

        if width > height:      #img is HORIZONTAL
            factor = float(SIDE/width)
            img = ImageOps.scale(img, factor)   #scaling the image by factor
            width = img.width
            height = img.height
            #position = 0, int(out.height/2 - height/2)   #tuple for the upper-left corner of img when 
            img = ImageOps.expand(img, border=int((SIDE-height)/2), fill=WHITE)
            
        else:                   #img is VERTICAL
            factor = float(SIDE/height)
            img = ImageOps.scale(img, factor)
            width = img.width
            height = img.height
            #position = 0, int(out.height/2 - height/2)   #tuple for the upper-left corner of img when 
            img = ImageOps.expand(img, border=int((SIDE-width)/2), fill=WHITE)
        
        print(img.mode)
        print(img.size)
        img.show()

        # END OF ITERATION

    except OSError:
        print("Cannot open file")
else:
    print("Args error")
