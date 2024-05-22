#10/04/24 - RUGGERI Randy - Project PROG201 - Stroop task
#Ce code permet de modeliser l'experience de Stroop : celle-ci consiste a presenter differents mots de couleurs differentes

import random
import expyriment
from expyriment import design, control, stimuli

WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

N_TRIALS = 24
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 10000

exp = design.Experiment(name="Stroop Task", text_size=40)
control.initialize(exp)

DICT = {"RED":RED, "YELLOW": YELLOW,"GREEN":GREEN,"BLUE":BLUE}
WORDSLIST = list(DICT.keys())

#Ici, on cree deux listes : une liste coherente contenant les stimuli dont le mot correspond a la couleur du mot, par exemple red ecrit en red
#Et une liste incoherente dont les mots ne correspondent pas a la couleur du mot, par exemple red ecrit en green
LISTECOHERENT = []
LISTEINCOHERENT = []
for i in WORDSLIST:
    for j in WORDSLIST:
        if i == j:
            LISTECOHERENT.append((i,j))
        else:
            LISTEINCOHERENT.append((i,j))

LISTE1 = []
for i, j in LISTEINCOHERENT:
    z = stimuli.TextLine(i,position=(0,0),text_size=50,text_colour=DICT[j])
    LISTE1.append((z, i, j))

LISTE2 = []
for i, j in LISTECOHERENT:
    w = stimuli.TextLine(i,position=(0,0),text_size=50,text_colour=DICT[j])
    LISTE2.append((w, i, j))

LISTE2 = LISTE2 * 3
LISTETOTAL = LISTE1 + LISTE2
random.shuffle(LISTETOTAL)

blankscreen = stimuli.BlankScreen()

#Voila les instructions presentees aux sujets avant d'effectuer l'experience
instruction_text = f'''Words of differents colors will appear on the screen. 
    Your task is to recognize the color of the word as quickly as possible.
    We measure the reaction time.
    Press the key : 
    - b for the color blue
    - g for the color green
    - r for the color red
    - y for the color yellow
    There will be {N_TRIALS} trials in total.
    Press the spacebar to start.'''

exp.add_data_variable_names(['trial', 'TARGET','Colour de la target','respkey', 'RT'])

keyboard = expyriment.io.Keyboard()

control.start(skip_ready_screen=True)
instruction_screen = expyriment.stimuli.TextScreen("Instructions", instruction_text, text_size=27)
instruction_screen.present()
exp.keyboard.wait_char(" ")

for i, (stimulus, mot, couleur) in enumerate(LISTETOTAL):
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    stimulus.present()
    key, rt = exp.keyboard.wait([expyriment.misc.constants.K_b, expyriment.misc.constants.K_g,expyriment.misc.constants.K_r,expyriment.misc.constants.K_y],duration=MAX_RESPONSE_DELAY)
    exp.data.add([i, mot, couleur,key,rt])

control.end()