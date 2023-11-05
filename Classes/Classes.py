#Created by Riley Livers

#FIlE used to define general Classes used throughout the program
import pygame
import random
import os
import mido
from pygame.locals import *
from Functions.Functions import is_black_key
from Functions.Functions import LightKey
from Resources.Parameters import *

#=================================================== ===================================================
#
#
#                                            Classes Section
#
#
#=================================================== ===================================================

#A class that holds the parameters for notes that are going to be displayed on the screen.
class DisNote:

    def __init__(self, note, duration, time, notePos):
        black = is_black_key(note)
        if black:
            self.width = 15
        else:
            self.width = 25
        self.note = note
        self.height = duration * 150
        self.x = notePos[note-21]
        self.y = -self.height
        self.speed = 7

        if black:
            self.color = BLACK
        else:
            self.color = WHITE

#updates the position depending on the speed variable, which is how many pixels down the object will move on the next frame
    def update(self):
        self.y += self.speed

#draws the object on whatever surface is passed through the window input parameter
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))



#A note class which holds the information for notes that will be displayed, but are not visible yet
class Note:
    def __init__(self, note, duration, time):
        self.note = note
        self.duration = duration
        self.time = time

    def __str__(self):
        return f"Note: {self.note}, Duration: {self.duration}, Time: {self.time}"



#This is used to store the time the note is pressed (turned on). When the note is again detected, but with no velocity (turned off),
#then a Note class object is created, with duration being the difference between tempnote's time, and the current time when 
#the note is turned off. 
class TempNote:
    def __init__(self, note, time):
        self.note = note
        self.time = time
    def __str__(self):
        return f"Note: {self.note}, Time: {self.time}"


#This class is used to live Piano displaying. An object of Livenote is created in the playground section of the PainoHero application. 
#Once a key is pressed, a livenote object is created and stored within an array of LiveNotes. They are constantly updated until
#the note's position is off of the screen, where they are then removed. 
class LiveNote:

    def __init__(self, note, notePos, window_height):
        black = is_black_key(note)
        if black:
            self.width = 15
        else:
            self.width = 25
        self.note = note
        self.released = False
        self.height = 0
        self.x = notePos[note-21]
        self.y = window_height - 200
        self.speed = 7

        if black:
            self.color = BLACK
        else:
            self.color = WHITE

    #updates the position of the note to give the appearance it is moving. 
    def update(self, note):
        if(note.released == False):
            self.height += self.speed
        if(self.y > 0):
            self.y -= self.speed

    #function for drawing the note onto whatever surface is passed as window
    def draw(self, window, note, notePos, window_height):

        #Lights the key that is pressed as long as the note hasn't been released. 
        if(note.released == False):
            LightKey(window, self.note, notePos, window_height)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))



#This is the Button class used to create all of the buttons shown within the program. The size, location, and text is
#all modifiable. 
class Button:

    def __init__(self, x, y, width, height, text, color, hover, font, fontsize, fontcolor):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover = hover
        self.fontsize = fontsize
        self.size = int(width * self.fontsize // 250)
        self.font = pygame.font.Font(font, self.size)
        self.text = text
        self.fontcolor = fontcolor
        self.text_surface = self.font.render(text, True, self.fontcolor)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (x + width / 2, y + height / 2)

        #Insures that transitions from previous menus Reset
        if pygame.mouse.get_pressed()[0] == 0:
            self.Pressed = False
        else:
            self.Pressed = True

    #updates the size and position of the button if the user resizes the screen
    def updateSize(self, x, y, width, height):
        self.size = int(width * self.fontsize // 250)
        self.font = pygame.font.Font(font, self.size)
        self.text_surface = self.font.render(self.text, True, self.fontcolor)
        self.rect = pygame.Rect(x, y, width, height)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (x + width / 2, y + height / 2)

    #draws the button on the screen, and returns if the user has clicked the button. 
    def draw(self, window):

        press = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.Pressed == False:
                self.Pressed = True
                print("Clicked")
                press = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.Pressed = False

        #Gives the option to have the button be invisible and use only the text for reference
        if self.color != 'transparent':
            if self.rect.collidepoint(pos):
                pygame.draw.rect(window, self.hover, self.rect)
            else:
                pygame.draw.rect(window, self.color, self.rect)

        window.blit(self.text_surface, self.text_rect)

        return press





