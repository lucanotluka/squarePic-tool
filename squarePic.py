from PIL import Image, ImageOps
import os
from pathlib import Path
import PySimpleGUI as sg

#   Global variables declaration
SIDE = 1080
SQUARE = SIDE, SIDE   #pixels, width & height
WHITE = 255, 255, 255     #RGB values

#   GUI opening
sg.theme()
folder = sg.popup_get_folder('Inserisci la cartella di foto', default_path = '', grab_anywhere = True, keep_on_top = True, history = False, no_titlebar = True)
if not folder:
    sg.popup_error('', auto_close=True, auto_close_duration=1)
    raise SystemExit()


for rawIm in Path(folder).iterdir():
    if not rawIm.is_file(): #skip iteration if it isnt an image file
        continue
    try:
        img = Image.open(rawIm)  #copying the raw img into "img" object
        img = img.convert('RGB')    #every image now has RGB mode. operation needed for troubleshoot a .jpeg opening error bug
        img = ImageOps.exif_transpose(img)  #operation that saves the rotation flag of the original pic into Image object 

        if img.width > img.height:      #img is HORIZONTAL
            img = ImageOps.pad(img, SQUARE, color=WHITE, centering=(0.5, 0.5))  #actual padding
        else:                   #img is VERTICAL
            img = ImageOps.pad(img, SQUARE, color=WHITE, centering=(0.5, 0.5))

        fileNm, ext = os.path.splitext(rawIm)   #name and extension of the pic, for convertion and saving
        img.save(fileNm + 'Edit.jpg')
        img.close() #closing the img Image object

    except OSError:
        print("Cannot open file")


