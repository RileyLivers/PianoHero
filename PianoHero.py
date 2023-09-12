import pygame
import random
import os
import mido
from pygame.locals import *
#Created by Riley Livers

#=================================================== ===================================================
#
#
#                                          Functions Section
#                                            Lines 13 : 96
#
#=================================================== ===================================================


def play_music(midi_filename):
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()



def is_black_key(key_number):
    adjusted_key_number = key_number - 12

    return (adjusted_key_number % 12) in [1, 3, 6, 8, 10]



def Note_Positions(key_number):

    if is_black_key(key_number):
        position = ((Note_Positions(key_number - 1) + Note_Positions(key_number + 1)) / 2) + 7.5

    else:
        x = 20
        count = 0
        while(x < key_number):
            x += 1
            if not (is_black_key(x)):
                count += 1
        position = (((window_width) / 52) * (count)) - 25
    return position



def DisplayBlacks():

    for disKey in range(21,109):
        black = is_black_key(disKey)
        if black:
            x = notePos[disKey-21]
            color = BLACK
            keyW = 15
            keyH = 120 
            y = (window_height - keyH) - 80
            pygame.draw.rect(window, color, (x, y, keyW, keyH))



def LightKey(key):

    black = is_black_key(key)
    if black:
        x = notePos[key-21]
        color = RED
        keyW = 15
        keyH = 120 
        y = (window_height - keyH) - 80
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
    else:
        x = notePos[key-21]
        color = RED
        keyW = 25
        keyH = 200
        y = (window_height - keyH)
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
        LayerKey(key-1, 1)
        LayerKey(key+1, 0)



def LayerKey(key, Direction):

    black = is_black_key(key)
    if black:
        x = notePos[key-21]
        color = BLACK
        keyW = 15
        keyH = 120 
        y = (window_height - keyH) - 80
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
    else:
        x = notePos[key-21]
        color = WHITE
        keyW = 25
        keyH = 200
        y = (window_height - keyH)
        pygame.draw.rect(window, color, (x, y, keyW, keyH))
        if (Direction == 0):
            LayerKey(key + 1, 0)
        else:
            LayerKey(key - 1, 1)


#=================================================== ===================================================
#
#
#                                            Classes Section
#
#
#=================================================== ===================================================
class DisNote:

    def __init__(self, note, duration, time):
        black = is_black_key(note)
        if black:
            self.width = 15
        else:
            self.width = 25
        self.note = note
        self.height = duration * 150
        self.x = notePos[note-21]
        self.y = -self.height
        self.speed = 10

        if black:
            self.color = BLACK
        else:
            self.color = WHITE

    def update(self):
        self.y += self.speed
    def updatePosition(self):
        self.x = self.x = (window_width / 88) * (note - self.width)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))




class Note:
    def __init__(self, note, duration, time):
        self.note = note
        self.duration = duration
        self.time = time
    
    def __str__(self):
        return f"Note: {self.note}, Durationo: {self.duration}, Time: {self.time}"




class TempNote:
    def __init__(self, note, time):
        self.note = note
        self.time = time
    def __str__(self):
        return f"Note: {self.note}, Time: {self.time}"
#=================================================== ===================================================





# Initialize Pygame
pygame.init()

# Set up the initial window size
window_width, window_height = 1440, 900
window = pygame.display.set_mode((window_width, window_height), RESIZABLE)
pygame.display.set_caption("Piano Hero")

notePos = []

for x in range(21,108):
    temp = Note_Positions(x)
    notePos.append(temp)

print(notePos[0])
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#--------------------------- Initial Prrogram Setup For User ----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

print("You have two song options because this is what I have after \nabout two days of coding... :) ")
print("Enter 1 for a suprise that I played myself :) \nEnter 2 for the song I used to test the program's ability for generic Midi")

SongChoice = input("Enter your choice (1 or 2): ")

# Check if the input is either 1 or 2
if SongChoice == "1":
    # Code to execute when user enters 1
    mid = mido.MidiFile('EndOfSeven.mid')
    midi_filename = 'EndOfSeven.mid'
    Delay = 0.75
    print("Enjoy me playing a bit of Light of the Seven, from game of thrones.")

elif SongChoice == "2":
    # Code to execute when user enters 2
    mid = mido.MidiFile('85263.mid')
    midi_filename = '85263.mid'
    Delay = 0.90
    print("Enjoy Pirates of the Carrabean")

elif SongChoice == "3":
    # Code to execute when user enters 2
    mid = mido.MidiFile('interstellar.mid')
    midi_filename = 'interstellar.mid'
    Delay = 0
    print("Time")

else:
    # Code to execute for invalid input
    print("Invalid input. Please enter either 1 or 2.")
    SongChoice = input("Enter your choice (1 or 2 or 3): ")


#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# mixer config
freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

clock = pygame.time.Clock()
tick_rate = 60

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
Five_Secs = 1000

purenotes = []
tempNotes = []
time=0


# Extract data from the MIDI file
for msg in mid:
	if msg.is_meta and msg.type == 'set_tempo':
			tempo = msg.tempo


for msg in mid:
	#print(msg)
	# tick = msg.time
	# notetime = mido.tick2second(tick, mid.ticks_per_beat, tempo)
	# #time += notetime
	time += msg.time

	#When a key is pressed down, take the time that it was pressed
	if(msg.type == 'note_on' and msg.velocity > 0):
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


# List to hold the falling notes
notes = []

last_note_time = 0

timer = 0
PlayFlag = 0
FirstKeyFlag = 0
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


#filler = pygame.Rect(0,0,window_width, window_height - 200)
# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    elapsed_time = clock.tick(tick_rate)  # Elapsed time in milliseconds
    elapsed_seconds = elapsed_time / 100000 * tick_rate  # Convert to seconds

    timer += elapsed_seconds
    seconds = timer * 1.6666666667
    #print("Timer:", timer , "Seconds: ", seconds)
    #print("Timer Value", timer)


    for infoNote in purenotes:
    	#print(infoNote.time)
    	if(seconds >= infoNote.time):
    		new_note = DisNote(infoNote.note, infoNote.duration, infoNote.time)

    		if PlayFlag == 0 and FirstKeyFlag == 0:
    			FirstKeyFlag = 1
    			TempSeconds = seconds

    		if FirstKeyFlag == 1 and PlayFlag == 0 and seconds >= Delay + TempSeconds:
    			play_music(midi_filename)
    			PlayFlag = 1
    		notes.append(new_note)
    		purenotes.remove(infoNote)

    window.fill(GRAY)
    pygame.draw.rect(window, WHITE, (0, window_height - 200, window_width, 200))
    DisplayBlacks()

    # Update falling notes position
    for note in notes:
        note.update()

        # Remove notes that have fallen off the screen
        if note.y + note.height > window_height - 200:
        	#delete the note as it falls into the piano so it doesnt overlap
        	note.height -= note.speed
        	LightKey(note.note)


        if note.height <= 0 :
            notes.remove(note)
    

    # Draw falling notes on the screen
    for note in notes:
        note.draw()


    # Refresh the display
    pygame.display.update()

# Cleanup
pygame.quit()