#Created by Riley Livers

#FIlE used to hold general functions used throughout the program
import pygame
import random
import os
import mido
from pygame.locals import *
from Resources.Parameters import *
#=================================================== ===================================================
#
#
#                                          Functions Section
#                                        
#
#=================================================== ===================================================

#This function is used to create notes that will be displayed in real time as the user pressed keys on a midi keyboard.
#once a message is detected, a livenote object is created and stored in the passed array. Once the nots is done being pressed, 
#a realeased flag is set to true within the respective livenote object.
def handleMessage(message, notePos, notes, window_height):
    from Classes.Classes import LiveNote

    if message.type == 'note_on' and message.velocity > 0:
        #Make a new live note to display
        note = LiveNote(message.note, notePos, window_height)
        notes.append(note)
        print(len(notes))

        #print the note number and velocity of keys pressed
        print(f"Note {message.note} played with velocity {message.velocity}")

    #check to see if the key has been released
    elif message.type == 'note_on' and message.velocity == 0:
        for note in notes:
            if(message.note == note.note):
                note.released = True
    return notes


#This is a general function for creating text and displaying it on the screen. 
#The font size is a ratio so that it can be adjusted with changes in the width and height of the 
#application
def CreateText(window, window_width, x, y, text, color, font, fontsize):
    size = window_width * fontsize // 200
    font = pygame.font.Font(font, size)
    surface = font.render(text, True, color)

    rect = surface.get_rect()

    window.blit(surface, (x - (rect.width / 2), y - (rect.height / 2)))



#simple function to play the midi file that is passed through the function
def play_music(midi_filename):
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()


#this is used to determine if the midikey number that is passed through the function represents a black key on the 
#keyboard. There are 12 unique notes on the piano, and 5 of those are black. I used the mod to return the remainder
#after dividing by 12, and if it was equal to the position of black keys within the 12 white keys, it would return true.
#Since the piano stars on note A, and the midi numbers dont start at 0, the algorithm had to be shifted left by 12. 
def is_black_key(key_number):
    adjusted_key_number = key_number - 12

    return (adjusted_key_number % 12) in [1, 3, 6, 8, 10]


#this determines the x coordinate of the key that is passed through the function. If the passed key is black, then the 
#position will be in the middle of the key to the right and key to the left, so recursion is used to redetermine the positon
#of the notes to the right and left, and then take the average of those two values which gives the black note position. 
#if its not black, a counter is used to count the number of white keys are to the left of the passed white key, and it moves 
#the note's x position to the right by the product of count and the width of one white key. 
def Note_Positions(key_number, window_width):

    if is_black_key(key_number):
        position = ((Note_Positions(key_number - 1, window_width) + Note_Positions(key_number + 1, window_width)) / 2) + (window_width / 192)

    else:
        x = 20
        count = 0
        while(x < key_number):
            x += 1
            if not (is_black_key(x)):
                count += 1
        position = (((window_width) / 52) * (count)) - (window_width / 57.6)
    return position


#this function is used to display all of the black keys on the botton of the program that are stagnant and used only to represent
#the piano. 
def DisplayBlacks(notePos, window, window_width, window_height):

    for disKey in range(21,109):
        black = is_black_key(disKey)
        if black:
            x = notePos[disKey-21]
            color = BLACK
            keyW = window_width / 96
            keyH = window_height / 7.5                    #Distance up from white key
            y = (window_height - (window_height / 7.5)) - window_height / 11.25
            pygame.draw.rect(window, color, (x, y, keyW, keyH))

#this function displays all of the white keys at the bottom of the screen, which represents the piano at the buttom. It is always
#called before the white keys so that the black keys are placed on top of the whites. 
def DisplayWhites(notePos, window, window_width, window_height):
    
    for disKey in range(21,109):
        white = not is_black_key(disKey)
        if white:
            x = notePos[disKey-21]
            color = WHITE
            keyW = window_width / 57.6
            keyH = window_height / 4.5
            y = (window_height - keyH)
            pygame.draw.rect(window, color, (x, y, keyW, keyH))




#This function "lights the key" that is passed through. What it does is draw a red key over the existing key, to make it appear as 
#though it has been lit up. 
def LightKey(window, key, notePos, window_width, window_height):

    black = is_black_key(key)
    if black:
        x = notePos[key-21]
        color = RED
        keyW = window_width / 96
        keyH = window_height / 7.5  
        y = (window_height - keyH) - window_height / 11.25
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
    else:
        x = notePos[key-21]
        color = RED
        keyW = window_width / 57.6
        keyH = window_height / 4.5
        y = (window_height - keyH)
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
        LayerKey(window, key, notePos, window_width, window_height)
        LayerKey(window, key, notePos, window_width, window_height)

def Light_Name_Key(window, window_width, key, notePos, window_height, note):
    note_name = note[:-1]
    black = is_black_key(key)
    if black:
        x = notePos[key-21]
        color = RED
        keyW = window_width / 96
        keyH = window_height / 7.5  
        y = (window_height - keyH) - window_height / 11.25
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
        CreateText(window, window_width, x + (window_width / 192), (y - (window_height / 30)), note_name, RED, font, 5)
    else:
        x = notePos[key-21]
        color = RED
        keyW = window_width / 57.6
        keyH = window_height / 4.5
        y = (window_height - keyH)
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
        LayerKey(window, key, notePos, window_width, window_height)
        LayerKey(window, key, notePos, window_width, window_height)
        CreateText(window, window_width, x + (window_width / 115.2), (y - (window_height / 30)), note_name, RED, font, 5)



#the layer key function is used to redisplay black keys to the right and left of a white key that has been pressed (if there is a black key).
#since the lightkey is called after the piano is displayed, the red key will overlap the black keys, so this must be called to redisplay the 
#key that has been covered unintentionally. 
def LayerKey(window, key, notePos, window_width, window_height):
    color = BLACK
    keyW = window_width / 96
    keyH = window_height / 7.5  
    y = (window_height - keyH) - window_height / 11.25

    #used as flags to represent the existence of a black key to the right or left of the white key passed
    left = False
    right = False

    #had to predefine left and right since the leftmost and rightmost keys wont have
    #neighbors
    if key > 21:
        left = is_black_key(key-1)
    if key < 108:
        right = is_black_key(key+1)
    if left:
        x = notePos[key-22]
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
    if right:
        x = notePos[key-20]
        pygame.draw.rect(window, color, (x, y, keyW, keyH))



#Function used to convert the note name to the midi number, using the note to midi dictionary for the note's number, 
#and then scaling the by the octave
def note_to_midi_number(note):

#parses the name and octave from the input and splits into separate variables
#Converts the octave to into to use within mathematical calculation for scaling
    note_name = note[:-1]
    octave = int(note[-1])

    midi_number = 12 * (octave + 1) + note_to_midi[note_name]

    return midi_number


def DisChordButtons(window_width, window_height, names, buttons):
    from Classes.Classes import Button

    x = 1
    y = 3
    Right = 0
    for name in names:
        name = name.replace('_', ' ')
        Right += 1
        TempName = Button((window_width / 12) * x, (window_height / 20) * y, window_width / 8, window_height / 20, name, WHITE, GRAY, font, 30, BLACK)
        buttons.append(TempName)
        x += 2
        if Right == 4:
            Right = 0
            x = 1
            y += 4
    Done = True

    return buttons, Done, names












