import PySimpleGUI as sg
from gui.customGui import CustomGui    


if __name__ == '__main__':
   
    # initialize the gui
    CustomGui.init(sg)

    # run the gui
    CustomGui.run(sg)