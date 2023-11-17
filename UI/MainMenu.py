#Created by Riley Livers

#The first GUI screen the user sees. This displays buttons for the user to choose. 

import pygame
from pygame.locals import *
from Classes.Classes import Button
from Functions.Functions import CreateText
from Resources.Parameters import *

def MainMenu(window, window_width, window_height):

    #Background Image for the main menu
    background = pygame.image.load("Resources/Images/MainMenu.jpeg")
    scaled_background = pygame.transform.scale(background, (window_width, window_height))
    window.blit(scaled_background, (0,0))

    CreateText(window, window_width, window_width / 4, window_height / 5, 'Piano Hero', WHITE, None, 24)
    CreateText(window, window_width, window_width / 4 - 1, window_height / 5 - 1, 'Piano Hero', BLACK, None, 24)



    #Creating the different Main Menu Buttons:
    PianoHero = Button((window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16), 'Play', WHITE, GRAY, font, 36, BLACK)
    VisualPG = Button((window_width / 40)*11, (window_height / 3), (window_width / 5), (window_height / 16), 'Create a Song', WHITE, GRAY, font, 36, BLACK)
    SongLib = Button((window_width / 40)*21, (window_height / 3), (window_width / 5), (window_height / 16), 'Load Song', WHITE, GRAY, font, 36, BLACK)
    LearnPiano = Button(window_width - (window_width / 5 ) - (window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16), 'Learn Piano', WHITE, GRAY, font, 36, BLACK)
    Exit = Button((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25), 'Exit', WHITE, GRAY, font, 36, BLACK)



    chill = True

    while chill:

        if PianoHero.draw(window):
            current_screen = 'TempMenu'
            chill = False

        elif VisualPG.draw(window):
            current_screen = 'PortSelect'
            chill = False

        elif SongLib.draw(window):
            current_screen = 'LoadSong'
            chill = False

        elif LearnPiano.draw(window):
            current_screen = 'LearnPianoMenu'
            chill = False

        elif Exit.draw(window):
            pygame.quit()




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']

                #Update the button sizes and background image size
                PianoHero.updateSize((window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16))
                VisualPG.updateSize((window_width / 40)*11, (window_height / 3), (window_width / 5), (window_height / 16))
                SongLib.updateSize((window_width / 40)*21, (window_height / 3), (window_width / 5), (window_height / 16))
                LearnPiano.updateSize(window_width - (window_width / 5 ) - (window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16))
                Exit.updateSize((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25))

                scaled_background = pygame.transform.scale(background, (window_width, window_height))
                window.blit(scaled_background, (0,0))

                CreateText(window, window_width, window_width / 4, window_height / 5, 'Piano Hero', WHITE, None, 24)
                CreateText(window, window_width, window_width / 4 - 1, window_height / 5 - 1, 'Piano Hero', BLACK, None, 24)

        pygame.display.update()
    return window_width, window_height, current_screen



