#Created by Riley Livers

#Cycles through all the Midi files located in the Midi Song Folder, removes all of the 
#delay prior to the first note being played, and then creates a button for each song and 
#displays them on the Screen. Once the user presses a button, the Button pressed is returned from
#the function


import pygame
from pygame.locals import *
import os
import mido
from Classes.Classes import Button
from Resources.Parameters import *

def LoadSongMenu(window, window_width, window_height):
    Chosen_Song = 'Nothing Yet'
    #Code to search through the midi files folder to find all midi files
    #Get the current working directory 
    current_directory = os.getcwd()

    #Defines the subfolder name
    subfolder_name = "Resources/Midi_Files"

    #Constructs the full path to the subfolder
    subfolder_path = os.path.join(current_directory, subfolder_name)

    #Lists all files in the subfolder
    files_in_subfolder = os.listdir(subfolder_path)
    
    #creates a button for each song with the name of each song
    buttons = []
    songCount = 0
    ThreeCount = 1
    for filename in files_in_subfolder:
        BadFile = False
        #I need to make sure there is no quiet time before the first note is played.
        #This is necessary to sync the visual notes with the midi file
        mid_file_path = 'Resources/Midi_Files/' + filename
        print(mid_file_path)

        #In case a bad file is encountered of a midi is added with .ds_Store file
        #I encountered the problem and this is a general solution
        try:
            midi_file = mido.MidiFile(mid_file_path)
        except OSError as error:
            print("Bad File Encountered, Skipping File...")
            BadFile = True

        if not BadFile:
            FirstKeyFlag = False
            for track in midi_file.tracks:
                for msg in track:
                    if FirstKeyFlag == False:

                        msg.time = 0
                    if(msg.type == 'note_on' and msg.velocity > 0):
                        FirstKeyFlag = True
                        print("Delay Removed for File: ", filename)
                        break
            midi_file.save(mid_file_path)

            #Print each song name
            print(filename)

            songCount += 1
            #for every 3 songs, increment the three count
            #This scales the buttons to a new column to the right
            if(songCount > 3):
                ThreeCount += 10
                songCount = 1
            TempName = Button((window_width / 40) * ThreeCount, (window_height / 10) * 2 * songCount, (window_width / 5), (window_height / 16), filename.replace(".mid", ""), WHITE, GRAY, font, 36, BLACK)
            buttons.append(TempName)



    #BackGround Image
    background = pygame.image.load("Resources/Images/MainMenu.jpeg")
    scaled_background = pygame.transform.scale(background, (window_width, window_height))
    window.blit(scaled_background, (0,0))



    #Button Declarations
    BackButton = Button((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25), 'Return', WHITE, GRAY, font, 36, BLACK)
    chill = True

    while chill:

        if BackButton.draw(window):
            current_screen = 'MainMenu'
            chill = False

        for button in buttons:
            if button.draw(window):
                current_screen = 'PlaySong'
                Chosen_Song = button.text + ".mid"
                chill = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == pygame.VIDEORESIZE:
                #Update window width and height when the window is resized
                window_width, window_height = event.dict['size']

                BackButton.updateSize((window_width / 40), (window_height / 20) * 18, (window_width / 10), (window_height / 25))
                songCount = 0
                ThreeCount = 1
                for button in buttons:
                    songCount += 1

                    #for every 3 songs, increment the three count
                    #This scales the buttons to a new column to the right
                    if(songCount > 3):
                        ThreeCount += 10
                        songCount = 1
                    button.updateSize((window_width / 40) * ThreeCount, (window_height / 10) * 2 * songCount, (window_width / 5), (window_height / 16))

                scaled_background = pygame.transform.scale(background, (window_width, window_height))
                window.blit(scaled_background, (0,0))

        pygame.display.update()
    return window_width, window_height, current_screen, Chosen_Song


















