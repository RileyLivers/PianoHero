# Created by Riley Livers

# The main file calls all of the User interface functions, passing and returning the necessary parameters used
# within each respective function.

import pygame
import random
import os
import mido
from pygame.locals import *

#Importing the User Interface Files

from UI.MainMenu import MainMenu
from UI.LoadSongMenu import LoadSongMenu
from UI.PlaySong import PlaySong
from UI.TempMenu import TempMenu
from UI.PortSelect import PortSelect
from UI.PlayGround import PlayGround
from UI.LearnPianoMenu import LearnPianoMenu
from UI.LearnScreen import LearnScreen


#=================================================== ===================================================
#=================================================== ===================================================
#                                     Main Execution of Functions
#=================================================== ===================================================
#=================================================== ===================================================

#Initialize Pygame
pygame.init()

#Set up the initial window size
window_width, window_height = 1440, 900
window = pygame.display.set_mode((window_width, window_height), RESIZABLE)
pygame.display.set_caption("Piano Hero")


current_screen = 'MainMenu'
MenuActive = False

running = True


while running:

    #Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            #Update window width and height when the window is resized
            window_width, window_height = event.dict['size']



    if current_screen == 'MainMenu':
        print('Main Menu Active')
        window_width, window_height, current_screen = MainMenu(window, window_width, window_height)

    elif current_screen == 'TempMenu':
        print('Temp Menu Active')
        window_width, window_height, current_screen = TempMenu(window, window_width, window_height)

    elif current_screen == 'LoadSong':
        print('Load Song Menu Active')
        window_width, window_height, current_screen, Chosen_Song = LoadSongMenu(window, window_width, window_height)

    elif current_screen == 'PlaySong':
        print('Playing Loaded Song')
        window_width, window_height, current_screen = PlaySong(window, window_width, window_height, Chosen_Song)

    elif current_screen == 'PortSelect':
        print('Select Port Menu Active')
        window_width, window_height, current_screen, Midi_Input = PortSelect(window, window_width, window_height)

    elif current_screen == 'CreateSong':
        print('Song Creation Menu Active')
        window_width, window_height, current_screen = PlayGround(window, window_width, window_height, Midi_Input)

    elif current_screen == 'LearnPianoMenu':
        print('Learn Piano Menu Active')
        window_width, window_height, current_screen = LearnPianoMenu(window, window_width, window_height)

    elif current_screen == 'LearnChords':
        print('Displayed LearnChords')
        window_width, window_height, current_screen = LearnScreen(window, window_width, window_height)





pygame.quit()


