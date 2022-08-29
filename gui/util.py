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
    # RETURN: None
    def convert_image(rawImage: str) -> None:

        try:

            image = Image.open(rawImage)
            image = image.convert('RGB')                   # every image now has RGB mode. operation needed for troubleshoot a .jpeg opening error bug
            image = ImageOps.exif_transpose(image)         # operation that saves the rotation flag of the original pic into Image object

            image = PrivateUtil.__set_orientation(image)

            PrivateUtil.__save_edit(rawImage, image)


        except OSError:
            raise OSError



# private utility methods for the gui (used in the class above)
class PrivateUtil:

    
    # DESC: set the orientation of the image
    # PARAMS: image, the image to set the orientation
    # RETURN: the image with the orientation set
    def __set_orientation(image: Image) -> Image:

        # the image is landscape oriented
        if image.width > image.height:      
            image = ImageOps.pad(image, config['square'], color=config['colors']['white'], centering=(0.5, 0.5))  

        # the image is portrait oriented
        else:                              
            image = ImageOps.pad(image, config['square'], color=config['colors']['white'], centering=(0.5, 0.5))

    
    # DESC: save the edited image
    # PARAMS: rawImage, the image to save
    #         image, the image to save
    # RETURN: None
    def __save_edit(rawImage: str, image: Image) -> None:

        try:
            fileName = os.path.splitext(rawImage)[0]   
            image.save(fileName + '_Edit.jpg')
            image.close()
        
        except OSError:
            raise OSError