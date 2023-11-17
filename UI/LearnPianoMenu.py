#This menu is for the user to learn the piano.


import pygame
from pygame.locals import *
from Classes.Classes import Button
from Functions.Functions import CreateText
from Resources.Parameters import *

def LearnPianoMenu(window, window_width, window_height):

    #Background Image for the main menu
    background = pygame.image.load("Resources/Images/MainMenu.jpeg")
    scaled_background = pygame.transform.scale(background, (window_width, window_height))
    window.blit(scaled_background, (0,0))

    CreateText(window, window_width, window_width / 4, window_height / 5, 'Learn Piano', WHITE, None, 24)
    CreateText(window, window_width, window_width / 4 - 1, window_height / 5 - 1, 'Learn Piano', BLACK, None, 24)



    #Creating the different Main Menu Buttons:
    Chords = Button((window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16), 'Chords', WHITE, GRAY, font, 36, BLACK)
    Scales = Button((window_width / 40)*11, (window_height / 3), (window_width / 5), (window_height / 16), 'Scales', WHITE, GRAY, font, 36, BLACK)
    Something = Button((window_width / 40)*21, (window_height / 3), (window_width / 5), (window_height / 16), 'Something', WHITE, GRAY, font, 36, BLACK)
    AnotherSomething = Button(window_width - (window_width / 5 ) - (window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16), 'Something Else', WHITE, GRAY, font, 36, BLACK)
    Return = Button((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 36, BLACK)



    chill = True

    while chill:

        if Chords.draw(window):
            current_screen = 'LearnChords'
            chill = False

        elif Scales.draw(window):
            current_screen = 'TempMenu'
            chill = False

        elif Something.draw(window):
            current_screen = 'TempMenu'
            chill = False

        elif AnotherSomething.draw(window):
            current_screen = 'TempMenu'
            chill = False

        elif Return.draw(window):
            current_screen = 'MainMenu'
            chill = False




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']

                #Update the button sizes and background image size
                Chords.updateSize((window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16))
                Scales.updateSize((window_width / 40)*11, (window_height / 3), (window_width / 5), (window_height / 16))
                Something.updateSize((window_width / 40)*21, (window_height / 3), (window_width / 5), (window_height / 16))
                AnotherSomething.updateSize(window_width - (window_width / 5 ) - (window_width / 40), (window_height / 3), (window_width / 5), (window_height / 16))
                Return.updateSize((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25))

                scaled_background = pygame.transform.scale(background, (window_width, window_height))
                window.blit(scaled_background, (0,0))

                CreateText(window, window_width, window_width / 4, window_height / 5, 'Learn Piano', WHITE, None, 24)
                CreateText(window, window_width, window_width / 4 - 1, window_height / 5 - 1, 'Learn Piano', BLACK, None, 24)

        pygame.display.update()
    return window_width, window_height, current_screen






