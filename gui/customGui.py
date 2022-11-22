import PySimpleGUI
from configuration import Configuration as config
from pathlib import Path
from gui.util import Util


# custom gui implementation from PySimpleGUI
class CustomGui:
    

    # DESC: initialize the gui with the custom theme
    # PARAMS: gui, the gui to initialize
    # RETURN: None
    def init(gui: PySimpleGUI) -> None:

        gui.theme('Default1')
        gui.theme_background_color(config['colors']['white'])
        gui.theme_button_color((config['colors']['white'], config['colors']['yellow']))
        gui.theme_text_color(config['colors']['black'])
        gui.theme_text_element_background_color(config['colors']['white'])

    
    # DESC: run the gui and handle the events
    # PARAMS: gui, the gui to run
    # RETURN: None
    # RAISE: OSError, if the image cannot be opened (handled in the gui)
    def run(gui: PySimpleGUI) -> None:

        while True:

            folder = Util.get_folder(gui)

            if not folder:
                gui.popup_error(f'Non hai selezionato alcuna cartella', no_titlebar = True, auto_close=True, auto_close_duration=1)

            else:
                images = [image for image in Path(folder).iterdir() if image.is_file()]
                for rawImage in images:
                    try:
                        Util.convert_image(rawImage)
                    except OSError:
                        gui.popup_error(f'Impossibile aprire un file, controllare la cartella.', auto_close=True, auto_close_duration=1)
            
            if gui.popup_yes_no('Vuoi terminare ed uscire?', no_titlebar = True) == "Yes":
                break
