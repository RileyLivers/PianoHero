#Created by Riley Livers

#At the moment, the file takes the selected midi input chosen by the user, and displays the keys which are pressed live. 

#I am currently developing a record feature so that whatever they press can be saved as a midi file and used in either the 
#piano hero game, or can be simply played using the load song feature of the application. 

import mido
import pygame
from pygame.locals import *

from Functions.Functions import Note_Positions, handleMessage, DisplayWhites, DisplayBlacks
from Classes.Classes import Button
from Resources.Parameters import *

def PlayGround(window, window_width, window_height, Midi_Input):

    portName = Midi_Input

    inputPort = mido.open_input(portName)


    clock = pygame.time.Clock()
    tick_rate = 60
    timer = 0

    #Predeterrmine all of the note positions so that you dont have to use more CPU computation power
    notePos = []

    for x in range(21,109):
        temp = Note_Positions(x, window_width)
        notePos.append(temp)


    notes = []

    BackButton = Button(window_width - (window_width / 10) - (window_width / 40), (window_height / 20) * 1, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 20, BLACK)
    #main Loop for real time keyboard sampling
    chill = True
    while chill:

        #Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                chill = False

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']
                BackButton.updateSize(window_width - (window_width / 10) - (window_width / 40), (window_height / 20) * 1, (window_width / 10), (window_height / 25))


        elapsed_time = clock.tick(tick_rate)  #Elapsed time in milliseconds
        elapsed_seconds = elapsed_time / 100000 * tick_rate  #Convert to seconds

        timer += elapsed_seconds
        seconds = timer * 1.6666666667 #constant scaler for Pygame Clock



        for message in inputPort.iter_pending():
            notes = handleMessage(message, notePos, notes, window_height)

        window.fill(GRAY)
        #pygame.draw.rect(window, WHITE, (0, window_height - 200, window_width, 200))
        DisplayWhites(notePos, window, window_height)
        DisplayBlacks(notePos, window, window_height)

        # Update falling notes position
        for note in notes:
            note.update(note)

            #Remove notes that have fallen off the screen
            if note.y <= 0:
                #delete the note as it climbs into the top 
                note.height -= note.speed


            if note.height <= 0 :
                notes.remove(note)
                print(len(notes))
        

        #Draw falling notes on the screen
        for note in notes:
            note.draw(window, note, notePos, window_height)

        if BackButton.draw(window):
            current_screen = 'PortSelect'
            chill = False


        #Refresh the display
        pygame.display.update()


    return window_width, window_height, current_screen
