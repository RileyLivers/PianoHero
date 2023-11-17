#File containing colors and fonts
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN= (0, 128, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (128, 0, 128)
BLOOD_ORANGE = (255, 69, 0)  
YELLOW_ORANGE = (255, 215, 0)  
LIME_GREEN = (50, 205, 50)  
AQUA_BLUE = (0, 255, 255)  
BLUE_INDIGO = (37, 0, 130)  
PURPLE_VIOLET = (128, 0, 179)  
SILVER = (192, 192, 192)
NAVY = (0, 0, 128)
OLIVE = (128, 128, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
hover_color = (200, 200, 200)
TRANS = 'transparent'

#Font Parameters
font = None

#Note names to midi numbers 
note_to_midi = {
    'C':  0, 'C#': 1, 'Db': 1,
    'D':  2, 'D#': 3, 'Eb': 3,
    'E':  4, 'Fb': 4, 'E#': 5,
    'F':  5, 'F#': 6, 'Gb': 6,
    'G':  7, 'G#': 8, 'Ab': 8,
    'A':  9, 'A#': 10, 'Bb': 10,
    'B':  11, 'Cb': 11, 'B#': 0
}


#Chord definitions

Major_Chords = {
	'C_Major' : ['C', 'E', 'G'],
	'C_Sharp_Major' : ['C#', 'E#', 'G#'],
	'D_Major' : ['D', 'F#', 'A'],
	'E_Flat_Major' : ['Eb', 'G', 'Bb'],
	'E_Major' : ['E', 'G#', 'B'],
	'F_Major' : ['F', 'A', 'C'],
	'F_Sharp_Major' : ['F#', 'A#', 'C#'],
	'G_Major' :['G', 'B', 'D'],
	'A_Flat_Major' : ['Ab', 'C', 'Eb'],
	'A_Major' : ['A', 'C#', 'E'],
	'B_Flat_Major' : ['Bb', 'D', 'F'],
	'B_Major' : ['B', 'D#', 'F#'] }

#Minor Chords
Minor_Chords = {
	'C_Minor' : ['C', 'Eb', 'G'],
	'C_Sharp_Minor' : ['C#', 'E', 'G#'],
	'D_Minor' : ['D', 'F', 'A'],
	'E_Flat_Minor' : ['Eb', 'Gb', 'Bb'],
	'E_Minor' : ['E', 'G', 'B'],
	'F_Minor' : ['F', 'Ab', 'C'],
	'F_Sharp_Minor' : ['F#', 'A', 'C#'],
	'G_Minor' :['G', 'Bb', 'D'],
	'A_Flat_Minor' : ['Ab', 'Cb', 'Eb'],
	'A_Minor' : ['A', 'C', 'E'],
	'B_Flat_Minor' : ['Bb', 'Db', 'F'],
	'B_Minor' : ['B', 'D', 'F#'] }

#Minor Chords
Diminished_Chords = {
	'C_Diminished' : ['C', 'Eb', 'Gb'],
	'C_Sharp_Diminished' : ['C#', 'E', 'G'],
	'D_Diminished' : ['D', 'F', 'Ab'],
	'E_Flat_Diminished' : ['Eb', 'Gb', 'A'],
	'E_Diminished' : ['E', 'G', 'Bb'],
	'F_Diminished' : ['F', 'Ab', 'Cb'],
	'F_Sharp_Diminished' : ['F#', 'A', 'C'],
	'G_Diminished' :['G', 'Bb', 'Db'],
	'A_Flat_Diminished' : ['Ab', 'Cb', 'D'],
	'A_Diminished' : ['A', 'C', 'Eb'],
	'B_Flat_Diminished' : ['Bb', 'Db', 'E'],
	'B_Diminished' : ['B', 'D', 'F'] }









#Major 7th Chords