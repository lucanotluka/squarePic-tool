import os
import PySimpleGUI
from PIL import Image, ImageOps
from configuration import Configuration as config



# utility methods for the gui
class Util:


    # DESC: get the folder from the gui
    # PARAMS: gui, the gui to get the folder from
    # RETURN: the folder selected by the user
    def get_folder(gui: PySimpleGUI) -> str:

        folder = gui.popup_get_folder(title = config['app_name'], 
                                          message = 'Seleziona la cartella di foto:', 
                                          default_path = '', grab_anywhere = True, 
                                          keep_on_top = True, 
                                          history = False, 
                                          image = "assets/analogpolimi.png")

        return folder


    # DESC: convert the image
    # PARAMS: rawImage, the image to convert
    #         isSquared,flag to know how work on the image
    # RETURN: None
    def convert_image(rawImage: str, isSquared: bool) -> None:

        try:

            image = Image.open(rawImage)
            image = image.convert('RGB')                   # every image now has RGB mode. operation needed for troubleshoot a .jpeg opening error bug
            image = ImageOps.exif_transpose(image)         # operation that saves the rotation flag of the original pic into Image object

            if isSquared:
                image = PrivateUtil.set_orientation(image)

            PrivateUtil.save_edit(rawImage, image, isSquared)

        except OSError:
            raise OSError



# private utility methods for the gui (used in the class above)
class PrivateUtil:

    
    # DESC: set the orientation of the image
    # PARAMS: image, the image to set the orientation
    # RETURN: the image with the orientation set
    def set_orientation(image: Image) -> Image:

        # the image is landscape oriented
        if image.width > image.height:      
            return ImageOps.pad(image, config['square'], color=config['colors']['white'], centering=(0.5, 0.5))  

        # the image is portrait oriented
        else:                              
            return ImageOps.pad(image, config['square'], color=config['colors']['white'], centering=(0.5, 0.5))

    
    # DESC: save the edited image
    # PARAMS: rawImage, the image to save
    #         image, the image to save
    #         isSquared, flag to set how is the saving of the picture
    # RETURN: None
    def save_edit(rawImage: str, image: Image, isSquared: bool) -> None:

        try:
            fileName, ext = os.path.splitext(rawImage)
            if isSquared:
                image.save(fileName + "sqrd.jpg")
            else:
                image.save(fileName + ".jpg")
            image.close()
        
        except OSError:
            raise OSError
