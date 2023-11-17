#Created by Riley Livers

#Plays the user selected loaded song. Displays a piano on the bottom, and lights up the keys as they fall into the
#piano. Also displays a return button if the user wishes to stop the playing song earlier. 

import pygame
import random
import os
import mido
from pygame.locals import *

from Classes.Classes import TempNote, Note, Button, DisNote
from Functions.Functions import Note_Positions, is_black_key, DisplayWhites, DisplayBlacks, play_music, LightKey
from Resources.Parameters import *

def PlaySong(window, window_width, window_height, Chosen_Song):

    #frame and nextframe are surfaces used as buffers for displaying the keys. This is used to hopefully reduce ghosting
    #effect and make for a smoother display of the keys.
    Frame = pygame.Surface((window_width, window_height))
    NextFrame = pygame.Surface((window_width, window_height))

    #this is a variable used to represent the speed at which the background color changes
    colorChange = 0

    #parameters for holding 
    red = 0
    green = 45
    blue = 45

    redDown = False
    greenDown = False
    blueDown = True 

    direct = 'Resources/Midi_Files/'
    songPath = direct + Chosen_Song

    notePos = []

    for x in range(21,109):
        temp = Note_Positions(x, window_width)
        notePos.append(temp)

    mid = mido.MidiFile(songPath)
    midi_filename = songPath

    #mixer config
    freq = 44100  #audio CD quality
    bitsize = -16   #unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024   #number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    clock = pygame.time.Clock()
    tick_rate = 60

    purenotes = []
    tempNotes = []
    time=0
    FirstKeyFlag = 0

    for msg in mid:
        print(msg)
        # tick = msg.time
        # notetime = mido.tick2second(tick, mid.ticks_per_beat, tempo)
        # time += notetime
        time += msg.time

        #When a key is pressed down, take the time that it was pressed
        if(msg.type == 'note_on' and msg.velocity > 0):
            if FirstKeyFlag == 0:
                msg.time = 0
                FirstKeyFlag = 1
            tempNote = TempNote(msg.note, time)
            tempNotes.append(tempNote)
            
        #when a key is released, take the time that it was released
        elif(msg.type == 'note_on' and msg.velocity == 0):
            for temp in tempNotes:
                if(msg.note == temp.note):
                    duration = time - temp.time
                    tempNotes.remove(temp)
                    purenote = Note(msg.note , duration, time - duration)
                    purenotes.append(purenote)

    notes = []

    last_note_time = 0

    timer = 0
    PlayFlag = 0
    TempSeconds = 0

    #sort the black and white keys to display them in order
    blacks = []
    whites = []
    for disKey in range(21,109):
            black = is_black_key(disKey)
            if(black):
                blacks.append(disKey)
            else:
                whites.append(disKey)

    #Button Declarations
    BackButton = Button(window_width - (window_width / 10) - (window_width / 40), (window_height / 20) * 1, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 36, BLACK)

    #filler = pygame.Rect(0,0,window_width, window_height - 200)
    # Game loop
    running = True
    while running:

        #Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']
                BackButton.updateSize(window_width - (window_width / 10) - (window_width / 40), (window_height / 20) * 1, (window_width / 10), (window_height / 25))
                for note in notes:
                    note.windowUpdate(notePos, window_width, window_height)

        elapsed_time = clock.tick(tick_rate)  # Elapsed time in milliseconds
        elapsed_seconds = elapsed_time / 100000 * tick_rate  # Convert to seconds

        timer += elapsed_seconds
        seconds = timer * 1.6666666667
        #print("Timer:", timer , "Seconds: ", seconds)
        #print("Timer Value", timer)


        for infoNote in purenotes:
            #print(infoNote.time)
            if(seconds >= infoNote.time):
                new_note = DisNote(window_width, window_height, infoNote.note, infoNote.duration, infoNote.time, notePos)
                notes.append(new_note)
                purenotes.remove(infoNote)


        #Quick algorithm to vary to background color each iteration of the program to have the folor fade
        #throughout the rainbow
        colorChange += 1
        if (colorChange > 2):
            colorChange = 0
            # if redDown:
            #     red -= 1
            # else:
            #     red += 1

            if greenDown:
                green -= 1
            else:
                green += 1

            if blueDown:
                blue -= 1
            else:
                blue += 1


            # if(red < 0):
            #     red = 0
            #     redDown = False
            # elif(red > 175):
            #     red = 175
            #     redDown = True
            if(green < 45):
                green = 45
                greenDown = False
            elif(green > 175):
                green = 175
                greenDown = True

            if(blue < 45):
                blue = 45
                blueDown = False
            elif(blue > 175):
                blue = 175
                blueDown = True


        NextFrame.fill((red, green, blue))





        #pygame.draw.rect(window, WHITE, (0, window_height - 200, window_width, 200))
        DisplayWhites(notePos, NextFrame, window_width, window_height)
        DisplayBlacks(notePos, NextFrame, window_width, window_height)

        #Update falling notes position
        for note in notes:
            note.update()

            #Remove notes that have fallen off the screen
            if note.y + note.height > window_height - (window_height / 4.5):
                if PlayFlag == 0:
                    play_music(midi_filename)
                    PlayFlag = 1
                #delete the note as it falls into the piano so it doesnt overlap
                note.height -= note.speed
                LightKey(NextFrame, note.note, notePos, window_width, window_height)

            if note.height <= 0 :
                notes.remove(note)
        

        #Draw falling notes on the screen
        for note in notes:
            note.draw(NextFrame)

        if BackButton.draw(NextFrame):
            current_screen = 'LoadSong'
            running = False
            pygame.mixer.music.stop()

        #Refresh the display
        Frame, NextFrame = NextFrame, Frame
        window.blit(Frame, (0,0))
        pygame.display.flip()

    return window_width, window_height, current_screen








