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

N_TRIALS = 40
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 10000

exp = design.Experiment(name="Stroop Task", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

WORDSLIST = ["YELLOW", "RED", "BLUE", "GREEN"]
WORDSLIST5 = WORDSLIST * 5
COLORLIST = [YELLOW,RED,BLUE,GREEN]
COLORLIST5 = COLORLIST * 5

COHERENTLIST = []
for i in range (20):
    i = stimuli.TextLine(WORDSLIST5[i],position=(0,0),text_size=50,text_colour=COLORLIST5[i])
    COHERENTLIST.append(i)

INCOHERENTLIST = []
for k in range (20) :
    a = random.randint(0,19)
    if a%4 == k%4 :
        a = a + 1
    k = stimuli.TextLine(WORDSLIST5[k],position=(0,0),text_size=50,text_colour=COLORLIST5[a])
    INCOHERENTLIST.append(k)

TARGETLIST = COHERENTLIST + INCOHERENTLIST
random.shuffle(TARGETLIST)

blankscreen = stimuli.BlankScreen()

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

for i_trial in range(N_TRIALS):
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    TARGETLIST[i_trial].present()
    key, rt = exp.keyboard.wait([expyriment.misc.constants.K_b, expyriment.misc.constants.K_g,expyriment.misc.constants.K_r,expyriment.misc.constants.K_y],duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial,TARGETLIST[i_trial].text, TARGETLIST[i_trial].text_colour,key,rt])

control.end()