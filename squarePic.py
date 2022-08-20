from PIL import Image, ImageOps
import os
from pathlib import Path

SIDE = 1080
SQUARE = SIDE, SIDE   #pixels, width & height
WHITE = 255, 255, 255     #RGB values

print('Inserisci path cartella')
folder = input()

for rawIm in Path(folder).iterdir():
    if not rawIm.is_file(): #skip iteration if it isnt a file
        continue
    try:
        img = Image.open(rawIm)  #copying the raw img into "img" object
        img = img.convert('RGB')    #every image now has RGB mode. operation needed for troubleshoot a .jpeg opening error bug
        img = ImageOps.exif_transpose(img)  #operation that saves the rotation flag of the original pic into Image object 

        if img.width > img.height:      #img is HORIZONTAL
            img = ImageOps.pad(img, SQUARE, color=WHITE, centering=(0.5, 0.5))
        else:                   #img is VERTICAL
            img = ImageOps.pad(img, SQUARE, color=WHITE, centering=(0.5, 0.5))

        fileNm, ext = os.path.splitext(rawIm)   #name and extension of the pic, for convertion and saving
        img.save(fileNm + 'Edit.jpg')
        img.close()

        # END OF ITERATION

    except OSError:
        print("Cannot open file")


