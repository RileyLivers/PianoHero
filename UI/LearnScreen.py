#Created by Riley Livers

import mido
import pygame
from pygame.locals import *

from Functions.Functions import Note_Positions, handleMessage, DisplayWhites, DisplayBlacks, note_to_midi_number, Light_Name_Key, CreateText, DisChordButtons
from Classes.Classes import Button
from Resources.Parameters import *

def LearnScreen(window, window_width, window_height):
    #Bool used to determine if the first thing has been displayed
    Hot = False

    #Used to know if the user clicked one of the chord category buttons
    Depth = False

    #Used to determine if the buttons have already been created
    ButtonsDone = False

    notePos = []
    for x in range(21,109):
        temp = Note_Positions(x, window_width)
        notePos.append(temp)


    buttons = []

    MajorChords = Button((window_width / 20) * 2, (window_height / 20) * 8, (window_width / 5), (window_height / 15), 'Major Chords', WHITE, GRAY, font, 30, BLACK)
    MinorChords = Button((window_width / 20) * 7, (window_height / 20) * 8, (window_width / 5), (window_height / 15), 'Minor Chords', WHITE, GRAY, font, 30, BLACK)
    DiminishedChords = Button((window_width / 20) * 12, (window_height / 20) * 8, (window_width / 5), (window_height / 15), 'Diminished Chords', WHITE, GRAY, font, 30, BLACK)
    BackButt = Button((window_width / 12) * 10, (window_height / 20) * 7, window_width / 8, window_height / 20, 'Back', WHITE, GRAY, font, 30, BLACK)

    BackButton = Button(window_width - (window_width / 10) - (window_width / 40), (window_height / 20) * 1, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 36, BLACK)

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

        




        window.fill((0,100,100))
        #pygame.draw.rect(window, WHITE, (0, window_height - 200, window_width, 200))


        DisplayWhites(notePos, window, window_width, window_height)
        DisplayBlacks(notePos, window, window_width, window_height)

        if(Hot):
            DisChord = Category[Chord]
            CreateText(window, window_width, (window_width / 10) * 3 , (window_height / 20) * 14 , Chord.replace('_',' '), BLACK, font, 10)
            for note in DisChord:

                note = note + '4'
                Light_Name_Key(window, window_width, note_to_midi_number(note), notePos, window_height, note)



        if not Depth:
            CreateText(window, window_width, window_width / 4, window_height / 5, 'Chords', WHITE, None, 24)
            CreateText(window, window_width, window_width / 4 - 1, window_height / 5 - 1, 'Chords', BLACK, None, 24)

            if BackButton.draw(window):
                current_screen = 'LearnPianoMenu'
                chill = False

            elif MajorChords.draw(window):
                Category = Major_Chords
                Depth = True

            elif MinorChords.draw(window):
                Category = Minor_Chords
                Depth = True

            elif DiminishedChords.draw(window):
                Category = Diminished_Chords
                Depth = True
        else:
            if Category == Major_Chords:
                CreateText(window, window_width, (window_width / 24) * 7, (window_height / 40) * 3 , 'Major Chords', BLACK, font, 13)
                names = Major_Chords.keys()

                #Create and display buttons for each major chord
                if not ButtonsDone:
                    buttons, ButtonsDone, names = DisChordButtons(window_width, window_height, names, buttons)

                for button in buttons:
                    if button.draw(window):
                        Hot = True
                        Chord = button.text.replace(' ', '_')

                    elif BackButt.draw(window):
                        buttons = []
                        ButtonsDone = False
                        Depth = False
                        Hot = False

            elif Category == Minor_Chords:
                CreateText(window, window_width, (window_width / 24) * 7, (window_height / 40) * 3 , 'Minor Chords', BLACK, font, 13)
                names = Minor_Chords.keys()

                #Create and display buttons for each major chord
                if not ButtonsDone:
                    buttons, ButtonsDone, names = DisChordButtons(window_width, window_height, names, buttons)
                    

                for button in buttons:
                    if button.draw(window):
                        Hot = True
                        Chord = button.text.replace(' ', '_')

                    elif BackButt.draw(window):
                        buttons = []
                        ButtonsDone = False
                        Depth = False
                        Hot = False

            elif Category == Diminished_Chords:
                CreateText(window, window_width, (window_width / 24) * 7, (window_height / 40) * 3 , 'Diminished Chords', BLACK, font, 13)
                names = Diminished_Chords.keys()

                #Create and display buttons for each major chord
                if not ButtonsDone:
                    buttons, ButtonsDone, names = DisChordButtons(window_width, window_height, names, buttons)
                    

                for button in buttons:
                    if button.draw(window):
                        Hot = True
                        Chord = button.text.replace(' ', '_')

                    elif BackButt.draw(window):
                        buttons = []
                        ButtonsDone = False
                        Depth = False
                        Hot = False

        #Refresh the display
        pygame.display.update()


    return window_width, window_height, current_screen