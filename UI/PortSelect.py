#Created by Riley Livers

#This FILE searches through the user's ports and displays each of the potential midi's connected as 
#a button. The user then selecs the midi they would like to use as the input, and then returns the 
#name of the midi. 

#If no midi input is found, the program displays "midi not fouond" to the user.

import mido
import pygame
from pygame.locals import *
from Classes.Classes import Button
from Resources.Parameters import *

def PortSelect(window, window_width, window_height):
    Midi_Input = 'Nothing Found'
    buttons = []

    try:
        inputs = mido.get_input_names()

    except OSError as error:
        print("Error:", error)

    if len(inputs) > 0:
        NoInputsFound = False

    else:
        NoInputsFound = True



    if NoInputsFound == False:
        portCount = 0
        for port in inputs:

            #Print each input name
            print(port)

            portCount += 1
            TempName = Button((window_width / 40), (window_height / 10) * 2 * portCount, (window_width / 5), (window_height / 16), port, WHITE, GRAY, font, 36, BLACK)
            buttons.append(TempName)

        #Button Declarations
        
        
        #BackGround Image
        background = pygame.image.load("Resources/Images/MainMenu.jpeg")
        scaled_background = pygame.transform.scale(background, (window_width, window_height))
        window.blit(scaled_background, (0,0))


    else:

        #BackGround Image
        background = pygame.image.load("Resources/Images/MainMenu.jpeg")
        scaled_background = pygame.transform.scale(background, (window_width, window_height))
        window.blit(scaled_background, (0,0))


        #Button Declarations
        NoInputs = Button((window_width / 2) - (window_width / 8) , (window_height / 2) - (window_height / 8), (window_width / 4), (window_height / 4), 'Midi not Found', TRANS, GRAY, font, 77, RED)
    BackButton = Button((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 20, BLACK)

    chill = True

    while chill:

        if NoInputsFound:
            if BackButton.draw(window) or NoInputs.draw(window):
                current_screen = 'MainMenu'
                chill = False
        else:

            for button in buttons:
                if button.draw(window):
                    current_screen = 'CreateSong'
                    Midi_Input = button.text
                    chill = False
            if BackButton.draw(window):
                current_screen = 'MainMenu'
                chill = False


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']

                if NoInputsFound == False:
                    BackButton.updateSize((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25))
                    songCount = 0
                    for button in buttons:
                        songCount += 1
                        button.updateSize((window_width / 40), (window_height / 10) * 2 * songCount, (window_width / 5), (window_height / 16))
                else:
                    NoInputs.updateSize((window_width / 2) - (window_width / 8) , (window_height / 2) - (window_height / 8), (window_width / 4), (window_height / 4))

                scaled_background = pygame.transform.scale(background, (window_width, window_height))
                window.blit(scaled_background, (0,0))

        pygame.display.update()
    return window_width, window_height, current_screen, Midi_Input


