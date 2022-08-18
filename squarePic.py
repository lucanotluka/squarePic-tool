from PIL import Image
import os, sys

square = (1080, 1080)   #pixels, width & height
white = (255, 255, 255)     #RGB values

if len(sys.argv) > 1:   #at least one file as argument check
    rawIm = sys.argv[1]     #first arg is the raw image

    # TO DO
    # - guarda il problema delle foto verticali inizializzate orizzontali
    # - ... per ogni pic nella directory    


    canva = Image.new(mode="RGB", size=square, color=white)    #creating a white square, 1080x1080 pixels obj
    try:    
        img = Image.open(rawIm).copy()  #copying the raw img into "img" object 
        img.thumbnail(square)   #resizing img at max 1080px, no matter which side is the maximum value. aspect ratio preserved
        out = canva     #output will be an empty canva at first
        if img.width > img.height:  #img is horizontal
            position = (0, int(out.height/2 - img. height/2))   #tuple for the upper-left corner of img when centered
        else:   #img is vertical
            position = (int(out.width/2 - img.width/2), 0)
        out.paste(img, position)    #actual merging on canva
        f, e = os.path.splitext(rawIm)     #saving in f the path of rawIm file (not Image obj)
        out.save(f + 'Edt' + '.jpg')    #saving the new image as .jpg

    except OSError:
        print("Cannot open file")
else:
    print("Args error")
