#Temporary FILE holding the place of future Application Updates which are in development

import pygame
from pygame.locals import *
from Classes.Classes import Button
from Resources.Parameters import *

def TempMenu(window, window_width, window_height):
    TempButton = Button((window_width / 2 ) - (window_width / 10), (window_height / 2) - (window_height / 32), (window_width / 5), (window_height / 16), 'In Development', WHITE, GRAY, font, 36, BLACK)
    window.fill((0, 0, 0))

    chill = True

    while chill:

        if TempButton.draw(window):
            current_screen = 'MainMenu'
            chill = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']
                TempButton.updateSize((window_width / 2 ), (window_height / 2), (window_width / 5), (window_height / 16))

        pygame.display.update()
    return window_width, window_height, current_screen