﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed 26 Jul 2023 12:04:45 PM 
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'syllable_seqA1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/mflores/Documents/denoisingExp/syllable_seqA1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "trial"
trialClock = core.Clock()

# Initialize components for Routine "sa"
saClock = core.Clock()
text_26 = visual.TextStim(win=win, name='text_26',
    text='sa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ma"
maClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='ma',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fe"
feClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='fe',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ma"
maClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='ma',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bi"
biClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='bi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "me"
meClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='me',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ni"
niClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='ni',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fa"
faClock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='fa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "se"
seClock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='se',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "su"
suClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='su',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ne"
neClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='ne',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "be"
beClock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='be',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fi"
fiClock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='fi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mi"
miClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='mi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ne"
neClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='ne',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pi_2"
pi_2Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='pi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mu"
muClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='mu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pe"
peClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='pe',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "su"
suClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='su',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bo"
boClock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='bo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bu"
buClock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='bu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mu"
muClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='mu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "sa"
saClock = core.Clock()
text_26 = visual.TextStim(win=win, name='text_26',
    text='sa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bo"
boClock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='bo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "si"
siClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='si',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fu"
fuClock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='fu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fa"
faClock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='fa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pi_2"
pi_2Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='pi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pu"
puClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='pu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bu"
buClock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='bu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fo"
foClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='fo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "po"
poClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='po',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fu"
fuClock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='fu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "nu"
nuClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='nu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "si"
siClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='si',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "so"
soClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='so',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pu"
puClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='pu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "no"
noClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='no',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "se"
seClock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='se',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ni"
niClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='ni',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mo"
moClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='mo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fi"
fiClock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='fi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fe"
feClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='fe',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "me"
meClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='me',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ba"
baClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='ba',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "po"
poClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='po',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "be"
beClock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='be',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pa"
paClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='pa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "na"
naClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='na',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "no"
noClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='no',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "fo"
foClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='fo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "bi"
biClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='bi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "na"
naClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='na',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "ba"
baClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='ba',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pe"
peClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='pe',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mo"
moClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='mo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mi"
miClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='mi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "nu"
nuClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='nu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mo"
moClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='mo',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "mi"
miClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='mi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "nu"
nuClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='nu',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "so"
soClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='so',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "pa"
paClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='pa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
mic = sound.microphone.Microphone(
    device=None, channels=None, 
    sampleRateHz=44100, maxRecordingSize=80000.0
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = []
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
saComponents = [text_26]
for thisComponent in saComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
saClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = saClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=saClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    if text_26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_26.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_26.tStop = t  # not accounting for scr refresh
            text_26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
            text_26.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in saComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sa"-------
for thisComponent in saComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ma"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
maComponents = [text]
for thisComponent in maComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
maClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ma"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = maClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=maClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in maComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ma"-------
for thisComponent in maComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fe"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
feComponents = [text_22]
for thisComponent in feComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fe"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    if text_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_22.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_22.tStop = t  # not accounting for scr refresh
            text_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
            text_22.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fe"-------
for thisComponent in feComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ma"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
maComponents = [text]
for thisComponent in maComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
maClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ma"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = maClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=maClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in maComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ma"-------
for thisComponent in maComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
biComponents = [text_18]
for thisComponent in biComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
biClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = biClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=biClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    if text_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_18.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_18.tStop = t  # not accounting for scr refresh
            text_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
            text_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in biComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bi"-------
for thisComponent in biComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "me"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
meComponents = [text_2]
for thisComponent in meComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
meClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "me"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = meClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=meClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in meComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "me"-------
for thisComponent in meComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ni"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
niComponents = [text_8]
for thisComponent in niComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
niClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ni"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = niClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=niClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in niComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ni"-------
for thisComponent in niComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
faComponents = [text_21]
for thisComponent in faComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
faClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = faClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=faClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    if text_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_21.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_21.tStop = t  # not accounting for scr refresh
            text_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
            text_21.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in faComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fa"-------
for thisComponent in faComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "se"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
seComponents = [text_27]
for thisComponent in seComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
seClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "se"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = seClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=seClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    if text_27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_27.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_27.tStop = t  # not accounting for scr refresh
            text_27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_27, 'tStopRefresh')  # time at next scr refresh
            text_27.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in seComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "se"-------
for thisComponent in seComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "su"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
suComponents = [text_30]
for thisComponent in suComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
suClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "su"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = suClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=suClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in suComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "su"-------
for thisComponent in suComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ne"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
neComponents = [text_7]
for thisComponent in neComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ne"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = neClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ne"-------
for thisComponent in neComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "be"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
beComponents = [text_17]
for thisComponent in beComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "be"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = beClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    if text_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_17.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_17.tStop = t  # not accounting for scr refresh
            text_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
            text_17.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "be"-------
for thisComponent in beComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
fiComponents = [text_23]
for thisComponent in fiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_23* updates
    if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_23.frameNStart = frameN  # exact frame index
        text_23.tStart = t  # local t and not account for scr refresh
        text_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)
    if text_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_23.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_23.tStop = t  # not accounting for scr refresh
            text_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
            text_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fi"-------
for thisComponent in fiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
miComponents = [text_3]
for thisComponent in miComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
miClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = miClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=miClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in miComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mi"-------
for thisComponent in miComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ne"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
neComponents = [text_7]
for thisComponent in neComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ne"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = neClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ne"-------
for thisComponent in neComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pi_2"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
pi_2Components = [text_13]
for thisComponent in pi_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pi_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pi_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pi_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pi_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
            text_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pi_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pi_2"-------
for thisComponent in pi_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
muComponents = [text_5]
for thisComponent in muComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
muClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = muClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=muClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in muComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mu"-------
for thisComponent in muComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pe"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
peComponents = [text_12]
for thisComponent in peComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
peClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pe"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = peClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=peClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
            text_12.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in peComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pe"-------
for thisComponent in peComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "su"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
suComponents = [text_30]
for thisComponent in suComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
suClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "su"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = suClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=suClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in suComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "su"-------
for thisComponent in suComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
boComponents = [text_19]
for thisComponent in boComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
boClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = boClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=boClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    if text_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_19.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_19.tStop = t  # not accounting for scr refresh
            text_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
            text_19.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in boComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bo"-------
for thisComponent in boComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
buComponents = [text_20]
for thisComponent in buComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
buClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = buClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=buClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    if text_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_20.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_20.tStop = t  # not accounting for scr refresh
            text_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
            text_20.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bu"-------
for thisComponent in buComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
muComponents = [text_5]
for thisComponent in muComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
muClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = muClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=muClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in muComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mu"-------
for thisComponent in muComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "sa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
saComponents = [text_26]
for thisComponent in saComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
saClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = saClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=saClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    if text_26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_26.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_26.tStop = t  # not accounting for scr refresh
            text_26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
            text_26.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in saComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sa"-------
for thisComponent in saComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
boComponents = [text_19]
for thisComponent in boComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
boClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = boClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=boClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    if text_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_19.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_19.tStop = t  # not accounting for scr refresh
            text_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
            text_19.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in boComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bo"-------
for thisComponent in boComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "si"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
siComponents = [text_28]
for thisComponent in siComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
siClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "si"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = siClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=siClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    if text_28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_28.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_28.tStop = t  # not accounting for scr refresh
            text_28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_28, 'tStopRefresh')  # time at next scr refresh
            text_28.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in siComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "si"-------
for thisComponent in siComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
fuComponents = [text_25]
for thisComponent in fuComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fuClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fuClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    if text_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_25.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_25.tStop = t  # not accounting for scr refresh
            text_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
            text_25.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fu"-------
for thisComponent in fuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
faComponents = [text_21]
for thisComponent in faComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
faClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = faClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=faClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    if text_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_21.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_21.tStop = t  # not accounting for scr refresh
            text_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
            text_21.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in faComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fa"-------
for thisComponent in faComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pi_2"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
pi_2Components = [text_13]
for thisComponent in pi_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pi_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pi_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pi_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pi_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
            text_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pi_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pi_2"-------
for thisComponent in pi_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
puComponents = [text_15]
for thisComponent in puComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
puClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = puClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=puClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    if text_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_15.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_15.tStop = t  # not accounting for scr refresh
            text_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
            text_15.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in puComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pu"-------
for thisComponent in puComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
buComponents = [text_20]
for thisComponent in buComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
buClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = buClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=buClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    if text_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_20.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_20.tStop = t  # not accounting for scr refresh
            text_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
            text_20.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bu"-------
for thisComponent in buComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
foComponents = [text_24]
for thisComponent in foComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
foClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = foClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=foClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    if text_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_24.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_24.tStop = t  # not accounting for scr refresh
            text_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
            text_24.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in foComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fo"-------
for thisComponent in foComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "po"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
poComponents = [text_14]
for thisComponent in poComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
poClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "po"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = poClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=poClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    if text_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_14.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_14.tStop = t  # not accounting for scr refresh
            text_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
            text_14.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "po"-------
for thisComponent in poComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
fuComponents = [text_25]
for thisComponent in fuComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fuClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fuClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    if text_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_25.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_25.tStop = t  # not accounting for scr refresh
            text_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
            text_25.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fu"-------
for thisComponent in fuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "nu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
nuComponents = [text_10]
for thisComponent in nuComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = nuClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nuClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
            text_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nu"-------
for thisComponent in nuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "si"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
siComponents = [text_28]
for thisComponent in siComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
siClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "si"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = siClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=siClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    if text_28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_28.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_28.tStop = t  # not accounting for scr refresh
            text_28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_28, 'tStopRefresh')  # time at next scr refresh
            text_28.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in siComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "si"-------
for thisComponent in siComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "so"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
soComponents = [text_29]
for thisComponent in soComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
soClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "so"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = soClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=soClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    if text_29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_29.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_29.tStop = t  # not accounting for scr refresh
            text_29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_29, 'tStopRefresh')  # time at next scr refresh
            text_29.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in soComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "so"-------
for thisComponent in soComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
puComponents = [text_15]
for thisComponent in puComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
puClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = puClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=puClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    if text_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_15.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_15.tStop = t  # not accounting for scr refresh
            text_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
            text_15.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in puComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pu"-------
for thisComponent in puComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "no"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
noComponents = [text_9]
for thisComponent in noComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
noClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "no"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = noClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=noClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in noComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "no"-------
for thisComponent in noComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "se"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
seComponents = [text_27]
for thisComponent in seComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
seClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "se"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = seClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=seClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    if text_27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_27.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_27.tStop = t  # not accounting for scr refresh
            text_27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_27, 'tStopRefresh')  # time at next scr refresh
            text_27.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in seComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "se"-------
for thisComponent in seComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ni"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
niComponents = [text_8]
for thisComponent in niComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
niClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ni"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = niClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=niClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in niComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ni"-------
for thisComponent in niComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
moComponents = [text_4]
for thisComponent in moComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
moClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = moClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=moClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in moComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mo"-------
for thisComponent in moComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
fiComponents = [text_23]
for thisComponent in fiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_23* updates
    if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_23.frameNStart = frameN  # exact frame index
        text_23.tStart = t  # local t and not account for scr refresh
        text_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)
    if text_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_23.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_23.tStop = t  # not accounting for scr refresh
            text_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
            text_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fi"-------
for thisComponent in fiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fe"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
feComponents = [text_22]
for thisComponent in feComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fe"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    if text_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_22.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_22.tStop = t  # not accounting for scr refresh
            text_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
            text_22.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fe"-------
for thisComponent in feComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "me"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
meComponents = [text_2]
for thisComponent in meComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
meClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "me"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = meClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=meClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in meComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "me"-------
for thisComponent in meComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ba"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
baComponents = [text_16]
for thisComponent in baComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
baClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ba"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=baClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    if text_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_16.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_16.tStop = t  # not accounting for scr refresh
            text_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
            text_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ba"-------
for thisComponent in baComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "po"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
poComponents = [text_14]
for thisComponent in poComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
poClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "po"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = poClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=poClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    if text_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_14.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_14.tStop = t  # not accounting for scr refresh
            text_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
            text_14.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in poComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "po"-------
for thisComponent in poComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "be"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
beComponents = [text_17]
for thisComponent in beComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "be"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = beClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    if text_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_17.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_17.tStop = t  # not accounting for scr refresh
            text_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
            text_17.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "be"-------
for thisComponent in beComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
paComponents = [text_11]
for thisComponent in paComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
paClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = paClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=paClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
            text_11.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in paComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pa"-------
for thisComponent in paComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "na"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
naComponents = [text_6]
for thisComponent in naComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
naClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "na"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = naClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=naClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in naComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "na"-------
for thisComponent in naComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "no"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
noComponents = [text_9]
for thisComponent in noComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
noClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "no"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = noClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=noClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in noComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "no"-------
for thisComponent in noComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "fo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
foComponents = [text_24]
for thisComponent in foComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
foClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = foClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=foClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    if text_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_24.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_24.tStop = t  # not accounting for scr refresh
            text_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
            text_24.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in foComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fo"-------
for thisComponent in foComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "bi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
biComponents = [text_18]
for thisComponent in biComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
biClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = biClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=biClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    if text_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_18.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_18.tStop = t  # not accounting for scr refresh
            text_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
            text_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in biComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bi"-------
for thisComponent in biComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "na"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
naComponents = [text_6]
for thisComponent in naComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
naClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "na"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = naClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=naClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in naComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "na"-------
for thisComponent in naComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "ba"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
baComponents = [text_16]
for thisComponent in baComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
baClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ba"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=baClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    if text_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_16.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_16.tStop = t  # not accounting for scr refresh
            text_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
            text_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ba"-------
for thisComponent in baComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pe"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
peComponents = [text_12]
for thisComponent in peComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
peClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pe"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = peClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=peClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
            text_12.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in peComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pe"-------
for thisComponent in peComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
moComponents = [text_4]
for thisComponent in moComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
moClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = moClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=moClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in moComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mo"-------
for thisComponent in moComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
miComponents = [text_3]
for thisComponent in miComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
miClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = miClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=miClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in miComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mi"-------
for thisComponent in miComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "nu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
nuComponents = [text_10]
for thisComponent in nuComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = nuClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nuClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
            text_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nu"-------
for thisComponent in nuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mo"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
moComponents = [text_4]
for thisComponent in moComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
moClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mo"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = moClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=moClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in moComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mo"-------
for thisComponent in moComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "mi"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
miComponents = [text_3]
for thisComponent in miComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
miClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mi"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = miClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=miClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in miComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mi"-------
for thisComponent in miComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "nu"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
nuComponents = [text_10]
for thisComponent in nuComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nuClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nu"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = nuClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nuClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
            text_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nu"-------
for thisComponent in nuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "so"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
soComponents = [text_29]
for thisComponent in soComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
soClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "so"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = soClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=soClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    if text_29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_29.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_29.tStop = t  # not accounting for scr refresh
            text_29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_29, 'tStopRefresh')  # time at next scr refresh
            text_29.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in soComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "so"-------
for thisComponent in soComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "pa"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
paComponents = [text_11]
for thisComponent in paComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
paClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pa"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = paClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=paClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
            text_11.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in paComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pa"-------
for thisComponent in paComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))


# ------Prepare to start Routine "xx"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
# keep track of which components have finished
xxComponents = [text_31]
for thisComponent in xxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
xxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "xx"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = xxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=xxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in xxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "xx"-------
for thisComponent in xxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)

# ------Prepare to start Routine "ISI"-------
continueRoutine = True
routineTimer.add(5.700000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=8, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISIComponents = [text_32, mic]
for thisComponent in ISIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # mic updates
    if mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mic.frameNStart = frameN  # exact frame index
        mic.tStart = t  # local t and not account for scr refresh
        mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
        # start recording with mic
        mic.start()
        mic.status = STARTED
    if mic.status == STARTED:
        # update recorded clip for mic
        mic.poll()
    if mic.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic.tStartRefresh + 5.7-frameTolerance:
            # keep track of stop time/frame for later
            mic.tStop = t  # not accounting for scr refresh
            mic.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
            # stop recording with mic
            mic.stop()
            mic.status = FINISHED
    if mic_q1.status == NOT_STARTED and t >= 0.4-frameTolerance:
        # keep track of start time/frame for later
        mic_q1.frameNStart = frameN  # exact frame index
        mic_q1.tStart = t  # local t and not account for scr refresh
        mic_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mic_q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mic_q1.started', t)
        # start recording with mic
        mic_q1.start()
        mic_q1.status = STARTED
    if mic_q1.status == STARTED:
        # update recorded clip for mic
        mic_q1.poll()
    if mic_q1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mic_q1.tStartRefresh + 4.55-frameTolerance:
            # keep track of stop time/frame for later
            mic_q1.tStop = t  # not accounting for scr refresh
            mic_q1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mic_q1.stopped', t)
            # stop recording with mic
            mic_q1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI"-------
for thisComponent in ISIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStartRefresh)
thisExp.addData('mic.stopped', mic.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, 
    transcribe='None',
    config=None)   
q1_trials.addData('mic_q1.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag_q1))

# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```
# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        print(i)
        print(clip)
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))```

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
