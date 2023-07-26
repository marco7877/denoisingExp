#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Wed 26 Jul 2023 01:47:01 PM 
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
    originPath='syllable_seqA1_lastrun.py',
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
mic = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0
)
text_32 = visual.TextStim(win=win, name='text_32',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ma"
maClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='ma',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fe"
feClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='fe',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ma"
maClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='ma',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "bi"
biClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='bi',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "me"
meClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='me',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ni"
niClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='ni',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fa"
faClock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='fa',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "se"
seClock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='se',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "su"
suClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='su',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ne"
neClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='ne',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "be"
beClock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='be',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "xx"
xxClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text='xx',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

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
# keep track of which components have finished
ISIComponents = [mic, text_32]
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
    
    # mic updates
    if mic.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
# tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
# this will also update mic.lastClip and mic.lastScript
mic.stop()
tag = data.utils.getDateStr()
micClip = mic.bank(
    tag=tag, transcribe='None',
    config=None
)
thisExp.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
thisExp.addData('mic.started', mic.tStart)
thisExp.addData('mic.stopped', mic.tStop)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))

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

# ------Prepare to start Routine "ISI2"-------
continueRoutine = True
routineTimer.add(5.800000)
# update component parameters for each repeat
mic_q1 = sound.microphone.Microphone(
    device=0, channels=1, 
    sampleRateHz=44100, maxRecordingSize=24000.0)
# keep track of which components have finished
ISI2Components = [text_33]
for thisComponent in ISI2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + 5.8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
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
            mic_q1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI2"-------
for thisComponent in ISI2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
mic_q1.stop()
tag_q1 = data.utils.getDateStr()
micClip = mic_q1.bank(tag=tag, transcribe='None',config=None)
q1_trials.addData('mic_q1.clip', os.path.join('./recording_mic_%s.wav' % tag_q1))
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
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)
for tag_q1 in mic_q1.clips:
    for i, clip in enumerate(mic_q1.clips[tag_q1]):
        clipFilename = 'recording_mic_%s.wav' % tag_q1
        if i > 0:
            clipFilename += '_%s' % i
            clip.save(clipFilename)

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
