#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on May 13, 2025, at 12:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""


# --- Import packages ---
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
psychopyVersion = '2022.2.3'
expName = 'car_panel_lexical_decision'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='E:\\Backups\\All Files\\Genel\\Is\\2022\\Upwork\\LabX\\studies\\driving_simulator_panel\\car_panel_lexical_decision_v11.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "initialization" ---
# Run 'Begin Experiment' code from function_definitions
import os
import math

def getImageWithKeyword(directory, keyword):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions) and keyword.lower() in file.lower():
                return "/".join([root, file])
                
def correctTextPosition(text_stim, text_position):
    bounding_box = [100, 100]
    return [text_position[0] + bounding_box[1]/2,
    text_position[1]]


def correctPosition(icon_size, icon_position):    
    
    return [icon_position[0] - math.copysign(icon_size[0], icon_position[0])/2,
    icon_position[1] - math.copysign(icon_size[1], icon_position[1])/2]
    
    
def correctPositionSmall(icon_size, icon_position):    
    return [icon_position[0] + icon_size[0]/2, icon_position[1]]
# Run 'Begin Experiment' code from panel_initialization
import os

# Example usage:
class Panel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.column_spacing = 0.03
        self.row_spacing = 0.03
        self.scale_ratios = [1, 2/3]
        self.scale_empty_part = "top"
        self.panel_x_size = round(x * self.scale_ratios[0])
        self.panel_y_size = round(y * self.scale_ratios[1])
        self.panel_position = self.estimate_panel_position()

    def estimate_panel_position(self):

        if self.scale_empty_part == "top":
            y_axis_shift = -1
        elif self.scale_empty_part == "bottom":
            y_axis_shift = 1
        else:
            y_axis_shift = 0

        if self.scale_empty_part == "left":
            x_axis_shift = 1
        elif self.scale_empty_part == "right":
            x_axis_shift = -1
        else:
            x_axis_shift = 0
        
        return [round(0.5 * x_axis_shift * (self.x * (1 - self.scale_ratios[0]))), 
                    round(0.5 * y_axis_shift * (self.y * (1 - self.scale_ratios[1])))]
        
    def generate_panel_layout(self, config):
        """
        Generates panel regions based on input config list.
        :param config: list of 4 integers, each 0 or 1
                       1 = single full-height panel in the column
                       0 = two half-height panels in the column
        :param win: object with win.x and win.y for screen width and height
        :return: list of panel region dictionaries with x, y, width, height
        """
        assert len(config) == 4, "Config must have exactly 4 elements (one per column)"
        assert all(c in (0, 1) for c in config), "Each config entry must be 0 or 1"
        
        window_origin_x = -self.x / 2 
        window_origin_y = self.y / 2 

        if self.scale_empty_part == "top":
            window_origin_y = window_origin_y - self.panel_y_size / 2        
        
        panel_width = self.panel_x_size
        panel_height = self.panel_y_size

        col_spacing_ratio = self.column_spacing 
        row_spacing_ratio = self.row_spacing

        num_col_spacings = 5  # 3 between + 2 sides
        
        col_spacing = panel_width * col_spacing_ratio
        row_spacing = panel_height * row_spacing_ratio

        region_width = (panel_width - (col_spacing * num_col_spacings)) / 4

        regions = []

        for col in range(4):
            x = window_origin_x + col_spacing * (col + 1) + region_width * col + region_width / 2

            if config[col] == 1:
                # Single full-height panel (minus top & bottom spacing)
                height = panel_height - 2*row_spacing
                y = window_origin_y - row_spacing - height / 2
                regions.append({
                    "x": int(x),
                    "y": int(y),
                    "width": int(region_width),
                    "height": int(height)
                })
            else:
                # Two half-height panels
                height = (panel_height - 3 * row_spacing) / 2
                for row in range(2):
                    y = window_origin_y - (row_spacing * (row + 1) + height * row) - height / 2 
                    regions.append({
                        "x": int(x),
                        "y": int(y),
                        "width": int(region_width),
                        "height": int(height)
                    })

        return regions

    def roi_separator(self, panel, separation_count, separation_direction):
        """ This function is used for separating individual panels into regions.
        Purpose is to add clutter based on these regions. 

        :param panel: (dict) enter the panel's dictionary (e.g. r[0] or r[target_panel])
        :param separation_count: (int) how many panels you want it to be separated into 
        :param separation_direction: (str) direction of separation "vertical" or "horizontal"

        :return: a list of dictionaries of the separated region values (x, y, width, height)
        """

        assert isinstance(separation_direction, str), 'separation_direction must be a string.'

        if separation_direction == "vertical":
            separation_axis = 'y'
            separation_size = 'height'
        elif separation_direction == "horizontal":
            separation_axis = 'x'
            separation_size = 'width'
        else:
            ValueError('f{separation_direction} is not a valid separation direction')    

        clutter_regions = []

        

        for i in range(0, separation_count):
            dummy_region = []
            dummy_region = dict(panel)

            panel_size = panel[separation_size] / separation_count

            start_border = -round(i*panel_size)
            end_border = -round((i+1)*panel_size)           
      
            section_origin = panel[separation_axis] + (panel[separation_size] / 2)
                

            section_start = round(section_origin + start_border) # find region's start
            section_end = round(section_origin + end_border)
            section_mid = round((section_start + section_end) / 2) # find midpoint between region's start and end                        
            section_size = abs(end_border - start_border)

            dummy_region[separation_axis] = section_start
            dummy_region[separation_size] = section_size
            
            clutter_regions.append(dummy_region)
            

        return clutter_regions
    
    def get_region_coordinate(self, clutter, direction, placement_index, section_description=None):
        """ This function is used for obtaining axis coordinates for clutter placement

        :param clutter: (dict) enter the clutter's dictionary (e.g. clutter[0] or clutter[target_clutter])

        :param placement_index: (int) List of 2 integers indicating the placement:
                - [place_index, place_range] > [1, 4] > [0, 1, 2, 3] > second element (1) is the coordinate
        :param section_description: "top" or "mid" part of the segmented region
        :return: point in coordinate system (x, y)
        """
        if direction == "vertical":
            placement_axis = 'y'
            placement_size = 'height'
        elif direction == "horizontal":
            placement_axis = 'x'
            placement_size = 'width'
        else:
            ValueError('f{separation_direction} is not a valid separation direction') 

        if section_description == None:
            section_description = "mid"

        section_count = placement_index[1]
        for i in range(0, section_count):

            section_size = clutter[placement_size] / section_count
            start_border = round(i*section_size)
            end_border = round((i+1)*section_size)
            if clutter[placement_axis] >= 0:
                start_border = -start_border
                end_border = -end_border
                section_origin = clutter[placement_axis] + (clutter[placement_size] / 2)
            else:
                start_border = -start_border
                end_border = -end_border                
                section_origin = clutter[placement_axis] + (clutter[placement_size] / 2)
    #   "x": 698,
    #   "y": 508,
    #   "width": 408,
    #   "height": 508
            
            section_start = section_origin + start_border
            section_end = section_origin + end_border
            section_mid = round((section_start + section_end) / 2)
            print('start border, end border', [start_border, end_border])            
            print('section start,mid,end', [section_start, section_mid, section_end])
            # print(f'section origin: {section_origin}, section start :{section_start}, section mid: {section_mid}')
            if i == placement_index[0]:
                if section_description == "mid":
                    return section_mid 
                elif section_description == "top":
                    return section_start
                elif section_description == "bottom":
                    return section_end


    def getImageWithKeyword(self, directory, keyword):
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions) and keyword.lower() in file.lower():
                    return "/".join([root, file])


# --- Initialize components for Routine "screen_display_images" ---
# Run 'Begin Experiment' code from estimate_frame_durations_2
exp_clock = core.Clock()
class placeholder:
    def __init__(self):
        self.boundingBox = [200, 200]
        
        
placeholder_boundingbox = placeholder()

background_panel = visual.ImageStim(
    win=win,
    name='background_panel', 
    image='stimuli/panels/background_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
panel1 = visual.ImageStim(
    win=win,
    name='panel1', 
    image='stimuli/panels/large_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
panel2 = visual.ImageStim(
    win=win,
    name='panel2', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
panel3 = visual.ImageStim(
    win=win,
    name='panel3', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
panel4 = visual.ImageStim(
    win=win,
    name='panel4', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
panel5 = visual.ImageStim(
    win=win,
    name='panel5', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
panel6 = visual.ImageStim(
    win=win,
    name='panel6', 
    image='stimuli/panels/large_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
lexical_text_2 = visual.TextStim(win=win, name='lexical_text_2',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
widget1_symbol1 = visual.ImageStim(
    win=win,
    name='widget1_symbol1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
widget1_symbol2 = visual.ImageStim(
    win=win,
    name='widget1_symbol2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
widget1_symbol3 = visual.ImageStim(
    win=win,
    name='widget1_symbol3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
widget1_text1 = visual.TextStim(win=win, name='widget1_text1',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
widget1_text2 = visual.TextStim(win=win, name='widget1_text2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
widget1_text3 = visual.TextStim(win=win, name='widget1_text3',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
widget1_text4 = visual.TextStim(win=win, name='widget1_text4',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
widget2_symbol1 = visual.ImageStim(
    win=win,
    name='widget2_symbol1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
widget2_text1 = visual.TextStim(win=win, name='widget2_text1',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
widget2_text2 = visual.TextStim(win=win, name='widget2_text2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
widget3_symbol1 = visual.ImageStim(
    win=win,
    name='widget3_symbol1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
widget4_symbol1 = visual.ImageStim(
    win=win,
    name='widget4_symbol1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
widget5_text1 = visual.TextStim(win=win, name='widget5_text1',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=200.0, ori=1.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
widget5_symbol1 = visual.ImageStim(
    win=win,
    name='widget5_symbol1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
keybaord_input_2 = keyboard.Keyboard()

# --- Initialize components for Routine "inter_trial_interval" ---
background_panel_2 = visual.ImageStim(
    win=win,
    name='background_panel_2', 
    image='stimuli/panels/background_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
panel1_2 = visual.ImageStim(
    win=win,
    name='panel1_2', 
    image='stimuli/panels/large_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
panel2_2 = visual.ImageStim(
    win=win,
    name='panel2_2', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
panel3_2 = visual.ImageStim(
    win=win,
    name='panel3_2', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
panel4_2 = visual.ImageStim(
    win=win,
    name='panel4_2', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
panel5_2 = visual.ImageStim(
    win=win,
    name='panel5_2', 
    image='stimuli/panels/small_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
panel6_2 = visual.ImageStim(
    win=win,
    name='panel6_2', 
    image='stimuli/panels/large_panel.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
widget1_symbol1_2 = visual.ImageStim(
    win=win,
    name='widget1_symbol1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
widget1_symbol2_2 = visual.ImageStim(
    win=win,
    name='widget1_symbol2_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
widget1_symbol3_2 = visual.ImageStim(
    win=win,
    name='widget1_symbol3_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
widget1_text1_2 = visual.TextStim(win=win, name='widget1_text1_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
widget1_text2_2 = visual.TextStim(win=win, name='widget1_text2_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
widget1_text3_2 = visual.TextStim(win=win, name='widget1_text3_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
widget1_text4_2 = visual.TextStim(win=win, name='widget1_text4_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
widget2_symbol1_2 = visual.ImageStim(
    win=win,
    name='widget2_symbol1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
widget2_text1_2 = visual.TextStim(win=win, name='widget2_text1_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
widget2_text2_2 = visual.TextStim(win=win, name='widget2_text2_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
widget3_symbol1_2 = visual.ImageStim(
    win=win,
    name='widget3_symbol1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
widget4_symbol1_2 = visual.ImageStim(
    win=win,
    name='widget4_symbol1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
widget5_text1_2 = visual.TextStim(win=win, name='widget5_text1_2',
    text='',
    font='Times',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
widget5_symbol1_2 = visual.ImageStim(
    win=win,
    name='widget5_symbol1_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "initialization" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from exp_init
import calendar
import json
import math
import random
from datetime import date
from datetime import datetime
# select a panel for the large clutter 1 (duration, fuel, distance)
# select from 0 to 6.
clutter_panel = 0


if 'win' not in locals():
    class win:
        def __init__(self):
            self.size = [1920, 1080]
    window = win()
    panel_layout = Panel(window.size[0], window.size[1])

else:
    panel_layout = Panel(win.size[0], win.size[1])

widget_regions = panel_layout.generate_panel_layout([1, 0, 0, 1]) 

# parse manual: panel is sliced based on the second element.  
# [1,3] > segments the panel into three and retrieves the second segment's midpoint.
# [0,5] > segments the panel into five and retrieves the first segment's midpoint.  

symbol_x_parse = [0, 10]
symbol_y_parse = [1, 3]

# trip widget (duration, fuel, distance)
text_x_parse = [4, 5]
text_y_parse = [1, 3]

trip_widget = {"info": {"parse": {"symbol": [symbol_x_parse, symbol_y_parse], "text": [text_x_parse, text_y_parse]}, "widget_index": 0},                
               "components": {"header": "Current Trip",
                            "duration": "1 hr 53 min", 
                            "fuel": "34 mpg", 
                            "distance": "78 mi"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                            } # todo: add variable parameters to these text


garage_widget = {"info": {"parse": {"symbol": [symbol_x_parse, symbol_y_parse], "text": [text_x_parse, text_y_parse]}, "widget_index": 1}, 
                 "components": {"header": "My Home",
                                "garage": "Garage Door\nClosed"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

temperature_widget = {"info": {"parse": {"symbol": [symbol_x_parse, symbol_y_parse], "text": [text_x_parse, text_y_parse]}, "widget_index": 3}, 
               "components": {"temperature": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
               }



battery_widget = {"info": {"parse": {"symbol": [symbol_x_parse, symbol_y_parse], "text": [text_x_parse, text_y_parse]}, "widget_index": 4}, 
                 "components": {"battery": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

day_widget = {"info": {"parse": {"symbol": [symbol_x_parse, symbol_y_parse], "text": [text_x_parse, text_y_parse]} , "widget_index": 5}, 
                 "components": {"header": "day",
                                "calendar": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }


section_desc = "mid"
# first assume header to be the same size in terms of roi
# then we can adjust it to become something else (smaller then etc.)
def segment_roi(panel, roi, widget_dict):
    section_desc = "mid"
    # garage widget (duration, fuel, distance)
    text_x_header = [4, 7]
    text_y_header = [2, 3]

    component_count = len(widget_dict["components"].keys())
    component_regions = panel.roi_separator(roi[widget_dict["info"]["widget_index"]], component_count, "vertical")
    iteration = 0
    widget_dict["component_regions"] = component_regions
    for key, comp_val in widget_dict["components"].items():
        
        if key != "header":
            # get symbol positions 
            widget_dict["sym_component_positions"][key] = [panel.get_region_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse"]["symbol"][0]), 
            panel.get_region_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse"]["symbol"][1])]

        # get current day for text display on widget
        if comp_val == "day":
            my_date = date.today()
            
            today = datetime.now()
            numeric_day = today.day # this is a integer
            widget_dict["components"]["header"] = calendar.day_name[my_date.weekday()] +"\n" +str(numeric_day) # e.g. 'Wednesday'\nNumber         
            section_desc = "mid"   
        
        if comp_val == None:
            pass

        elif key == "header":
            # headers are more leftward than regular text, hence specific text parsing
            widget_dict["txt_component_positions"][key] = [panel.get_region_coordinate(component_regions[iteration], "horizontal", text_x_header), 
            panel.get_region_coordinate(component_regions[iteration], "vertical", text_y_header, section_desc)]

        else:
            widget_dict["txt_component_positions"][key] = [panel.get_region_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse"]["text"][0]), 
            panel.get_region_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse"]["text"][1])]

        # load in image
        if key == "header" or key == "text":
            pass
        else:
            widget_dict["img_files"][key] = panel.getImageWithKeyword("./stimuli/clutter", key)
            print("added img file: ", panel.getImageWithKeyword("./stimuli/clutter", key))

        iteration = iteration + 1

    return widget_dict




trip_widget = segment_roi(panel_layout, widget_regions, trip_widget)
garage_widget = segment_roi(panel_layout, widget_regions, garage_widget)
day_widget = segment_roi(panel_layout, widget_regions, day_widget)
temperature_widget = segment_roi(panel_layout, widget_regions, temperature_widget)
battery_widget = segment_roi(panel_layout, widget_regions, battery_widget)

trip_widget["sym_component_positions"]["duration"]
trip_widget["sym_component_positions"]["fuel"]
trip_widget["sym_component_positions"]["distance"]


print(widget_regions)
print('trip_widget\n', json.dumps(trip_widget, indent=2))
# print('\n\ngarage_widget\n',json.dumps(garage_widget, indent=2))
# print('\n\ntemperature_widget\n',json.dumps(temperature_widget, indent=2))
# print('\n\nbattery_widget',json.dumps(battery_widget, indent=2))
print('\n\nday_widget\n',json.dumps(day_widget, indent=2))





garage_icon_size = [garage_widget["component_regions"][1]["width"]*2/5, garage_widget["component_regions"][1]["width"]*2/5]
onethird_icon_size = [trip_widget["component_regions"][0]["width"]/3, trip_widget["component_regions"][0]["width"]/3]
half_icon_size = [day_widget["component_regions"][1]["width"]/1.1, day_widget["component_regions"][1]["height"]/1.1]
full_icon_size = [temperature_widget["component_regions"][0]["width"]/1.1, temperature_widget["component_regions"][0]["height"]/1.1]


text_size = trip_widget["component_regions"][0]["width"]/10
# choose a targel panel (1 to 10)
# Panel Numbers: [1, [2/3], [4/5], 6]
target_panel = 3

# letter size is dependent on the large panel's height
letter_size = temperature_widget["component_regions"][0]["height"]/5
day_size = day_widget["component_regions"][0]["width"]/7
header_size = trip_widget["component_regions"][0]["width"]/10
# keep track of which components have finished
initializationComponents = []
for thisComponent in initializationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "initialization" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initializationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "initialization" ---
for thisComponent in initializationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initialization" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimulus_sheet.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "screen_display_images" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from estimate_frame_durations_2
    t_start_time = exp_clock.getTime()
    t_frame_time = []
    
    background_panel.setPos([panel_layout.panel_position])
    background_panel.setSize((panel_layout.panel_x_size, panel_layout.panel_y_size))
    panel1.setPos((widget_regions[0]['x'], widget_regions[0]['y']))
    panel1.setSize((widget_regions[0]['width'], widget_regions[0]['height']))
    panel2.setPos((widget_regions[1]['x'], widget_regions[1]['y']))
    panel2.setSize((widget_regions[1]['width'], widget_regions[1]['height']))
    panel3.setPos((widget_regions[2]['x'], widget_regions[2]['y']))
    panel3.setSize((widget_regions[2]['width'], widget_regions[2]['height']))
    panel4.setPos((widget_regions[3]['x'], widget_regions[3]['y']))
    panel4.setSize((widget_regions[3]['width'], widget_regions[3]['height']))
    panel5.setPos((widget_regions[4]['x'], widget_regions[4]['y']))
    panel5.setSize((widget_regions[4]['width'], widget_regions[4]['height']))
    panel6.setPos((widget_regions[5]['x'], widget_regions[5]['y']))
    panel6.setSize((widget_regions[5]['width'], widget_regions[5]['height']))
    lexical_text_2.setPos((widget_regions[target_panel-1]['x'], widget_regions[target_panel-1]['y']))
    lexical_text_2.setText(text)
    lexical_text_2.setFont(currentFont)
    lexical_text_2.setHeight(letter_size)
    widget1_symbol1.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["duration"])])
    widget1_symbol1.setSize(onethird_icon_size)
    widget1_symbol1.setImage(trip_widget["img_files"]["duration"])
    widget1_symbol2.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["fuel"])])
    widget1_symbol2.setSize(onethird_icon_size)
    widget1_symbol2.setImage(trip_widget["img_files"]["fuel"])
    widget1_symbol3.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["distance"])])
    widget1_symbol3.setSize(onethird_icon_size)
    widget1_symbol3.setImage(trip_widget["img_files"]["distance"])
    widget1_text1.setPos([correctTextPosition(widget1_text1, trip_widget["txt_component_positions"]["duration"])])
    widget1_text1.setText(trip_widget["components"]["duration"])
    widget1_text1.setHeight(text_size)
    widget1_text2.setPos([correctTextPosition(widget1_text2,trip_widget["txt_component_positions"]["fuel"])])
    widget1_text2.setText(trip_widget["components"]["fuel"])
    widget1_text2.setHeight(text_size)
    widget1_text3.setPos([correctTextPosition(widget1_text3, trip_widget["txt_component_positions"]["distance"])])
    widget1_text3.setText(trip_widget["components"]["distance"])
    widget1_text3.setHeight(text_size)
    widget1_text4.setPos([correctTextPosition(widget1_text4,trip_widget["txt_component_positions"]["header"])])
    widget1_text4.setText(trip_widget["components"]["header"])
    widget1_text4.setHeight(header_size)
    widget2_symbol1.setPos([correctPositionSmall(garage_icon_size, garage_widget["sym_component_positions"]["garage"])])
    widget2_symbol1.setSize(garage_icon_size)
    widget2_symbol1.setImage(garage_widget["img_files"]["garage"])
    widget2_text1.setPos([correctTextPosition(widget2_text1,garage_widget["txt_component_positions"]["header"])])
    widget2_text1.setText(garage_widget["components"]["header"])
    widget2_text1.setHeight(header_size)
    widget2_text2.setPos([correctTextPosition(widget2_text2, garage_widget["txt_component_positions"]["garage"])])
    widget2_text2.setText(garage_widget["components"]["garage"])
    widget2_text2.setHeight(text_size)
    widget3_symbol1.setPos([correctPosition(full_icon_size, temperature_widget["sym_component_positions"]["temperature"])])
    widget3_symbol1.setSize(full_icon_size)
    widget3_symbol1.setImage(temperature_widget["img_files"]["temperature"])
    widget4_symbol1.setPos([correctPosition(full_icon_size, battery_widget["sym_component_positions"]["battery"])])
    widget4_symbol1.setSize(full_icon_size)
    widget4_symbol1.setImage(battery_widget["img_files"]["battery"])
    widget5_text1.setPos([correctTextPosition(widget5_text1, day_widget["txt_component_positions"]["header"])])
    widget5_text1.setOri(0.0)
    widget5_text1.setText(day_widget["components"]["header"])
    widget5_text1.setHeight(day_size)
    widget5_text1.setFlip('None')
    widget5_symbol1.setPos([correctPosition(half_icon_size, day_widget["sym_component_positions"]["calendar"])])
    widget5_symbol1.setSize(half_icon_size)
    widget5_symbol1.setImage(day_widget["img_files"]["calendar"])
    keybaord_input_2.keys = []
    keybaord_input_2.rt = []
    _keybaord_input_2_allKeys = []
    # Run 'Begin Routine' code from align_text
    alignment_var = "left"
    
    
    widget1_text1.alignText = alignment_var
    widget1_text2.alignText = alignment_var
    widget1_text3.alignText = alignment_var
    widget1_text4.alignText = alignment_var
    
    widget2_text1.alignText = alignment_var
    widget2_text2.alignText = alignment_var
    
    widget5_text1.alignText = alignment_var
    
    widget1_text4.bold = True
    widget2_text1.bold = True
    widget5_text1.bold = True
    
    
    # keep track of which components have finished
    screen_display_imagesComponents = [background_panel, panel1, panel2, panel3, panel4, panel5, panel6, lexical_text_2, widget1_symbol1, widget1_symbol2, widget1_symbol3, widget1_text1, widget1_text2, widget1_text3, widget1_text4, widget2_symbol1, widget2_text1, widget2_text2, widget3_symbol1, widget4_symbol1, widget5_text1, widget5_symbol1, keybaord_input_2]
    for thisComponent in screen_display_imagesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "screen_display_images" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from estimate_frame_durations_2
        t_frame_time.append(round((exp_clock.getTime() - t_start_time)*1000,2))
        
        t_start_time = exp_clock.getTime()
        
        # *background_panel* updates
        if background_panel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_panel.frameNStart = frameN  # exact frame index
            background_panel.tStart = t  # local t and not account for scr refresh
            background_panel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_panel, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_panel.started')
            background_panel.setAutoDraw(True)
        
        # *panel1* updates
        if panel1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel1.frameNStart = frameN  # exact frame index
            panel1.tStart = t  # local t and not account for scr refresh
            panel1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel1.started')
            panel1.setAutoDraw(True)
        
        # *panel2* updates
        if panel2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel2.frameNStart = frameN  # exact frame index
            panel2.tStart = t  # local t and not account for scr refresh
            panel2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel2.started')
            panel2.setAutoDraw(True)
        
        # *panel3* updates
        if panel3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel3.frameNStart = frameN  # exact frame index
            panel3.tStart = t  # local t and not account for scr refresh
            panel3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel3.started')
            panel3.setAutoDraw(True)
        
        # *panel4* updates
        if panel4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel4.frameNStart = frameN  # exact frame index
            panel4.tStart = t  # local t and not account for scr refresh
            panel4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel4.started')
            panel4.setAutoDraw(True)
        
        # *panel5* updates
        if panel5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel5.frameNStart = frameN  # exact frame index
            panel5.tStart = t  # local t and not account for scr refresh
            panel5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel5.started')
            panel5.setAutoDraw(True)
        
        # *panel6* updates
        if panel6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel6.frameNStart = frameN  # exact frame index
            panel6.tStart = t  # local t and not account for scr refresh
            panel6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel6.started')
            panel6.setAutoDraw(True)
        
        # *lexical_text_2* updates
        if lexical_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lexical_text_2.frameNStart = frameN  # exact frame index
            lexical_text_2.tStart = t  # local t and not account for scr refresh
            lexical_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lexical_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lexical_text_2.started')
            lexical_text_2.setAutoDraw(True)
        
        # *widget1_symbol1* updates
        if widget1_symbol1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol1.frameNStart = frameN  # exact frame index
            widget1_symbol1.tStart = t  # local t and not account for scr refresh
            widget1_symbol1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol1.started')
            widget1_symbol1.setAutoDraw(True)
        
        # *widget1_symbol2* updates
        if widget1_symbol2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol2.frameNStart = frameN  # exact frame index
            widget1_symbol2.tStart = t  # local t and not account for scr refresh
            widget1_symbol2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol2.started')
            widget1_symbol2.setAutoDraw(True)
        
        # *widget1_symbol3* updates
        if widget1_symbol3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol3.frameNStart = frameN  # exact frame index
            widget1_symbol3.tStart = t  # local t and not account for scr refresh
            widget1_symbol3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol3.started')
            widget1_symbol3.setAutoDraw(True)
        
        # *widget1_text1* updates
        if widget1_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text1.frameNStart = frameN  # exact frame index
            widget1_text1.tStart = t  # local t and not account for scr refresh
            widget1_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text1.started')
            widget1_text1.setAutoDraw(True)
        
        # *widget1_text2* updates
        if widget1_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text2.frameNStart = frameN  # exact frame index
            widget1_text2.tStart = t  # local t and not account for scr refresh
            widget1_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text2.started')
            widget1_text2.setAutoDraw(True)
        
        # *widget1_text3* updates
        if widget1_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text3.frameNStart = frameN  # exact frame index
            widget1_text3.tStart = t  # local t and not account for scr refresh
            widget1_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text3.started')
            widget1_text3.setAutoDraw(True)
        
        # *widget1_text4* updates
        if widget1_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text4.frameNStart = frameN  # exact frame index
            widget1_text4.tStart = t  # local t and not account for scr refresh
            widget1_text4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text4.started')
            widget1_text4.setAutoDraw(True)
        
        # *widget2_symbol1* updates
        if widget2_symbol1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_symbol1.frameNStart = frameN  # exact frame index
            widget2_symbol1.tStart = t  # local t and not account for scr refresh
            widget2_symbol1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_symbol1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_symbol1.started')
            widget2_symbol1.setAutoDraw(True)
        
        # *widget2_text1* updates
        if widget2_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_text1.frameNStart = frameN  # exact frame index
            widget2_text1.tStart = t  # local t and not account for scr refresh
            widget2_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_text1.started')
            widget2_text1.setAutoDraw(True)
        
        # *widget2_text2* updates
        if widget2_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_text2.frameNStart = frameN  # exact frame index
            widget2_text2.tStart = t  # local t and not account for scr refresh
            widget2_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_text2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_text2.started')
            widget2_text2.setAutoDraw(True)
        
        # *widget3_symbol1* updates
        if widget3_symbol1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget3_symbol1.frameNStart = frameN  # exact frame index
            widget3_symbol1.tStart = t  # local t and not account for scr refresh
            widget3_symbol1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget3_symbol1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget3_symbol1.started')
            widget3_symbol1.setAutoDraw(True)
        
        # *widget4_symbol1* updates
        if widget4_symbol1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget4_symbol1.frameNStart = frameN  # exact frame index
            widget4_symbol1.tStart = t  # local t and not account for scr refresh
            widget4_symbol1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget4_symbol1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget4_symbol1.started')
            widget4_symbol1.setAutoDraw(True)
        
        # *widget5_text1* updates
        if widget5_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget5_text1.frameNStart = frameN  # exact frame index
            widget5_text1.tStart = t  # local t and not account for scr refresh
            widget5_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget5_text1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget5_text1.started')
            widget5_text1.setAutoDraw(True)
        
        # *widget5_symbol1* updates
        if widget5_symbol1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget5_symbol1.frameNStart = frameN  # exact frame index
            widget5_symbol1.tStart = t  # local t and not account for scr refresh
            widget5_symbol1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget5_symbol1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget5_symbol1.started')
            widget5_symbol1.setAutoDraw(True)
        
        # *keybaord_input_2* updates
        waitOnFlip = False
        if keybaord_input_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keybaord_input_2.frameNStart = frameN  # exact frame index
            keybaord_input_2.tStart = t  # local t and not account for scr refresh
            keybaord_input_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keybaord_input_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keybaord_input_2.started')
            keybaord_input_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keybaord_input_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keybaord_input_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keybaord_input_2.status == STARTED and not waitOnFlip:
            theseKeys = keybaord_input_2.getKeys(keyList=['y','n'], waitRelease=False)
            _keybaord_input_2_allKeys.extend(theseKeys)
            if len(_keybaord_input_2_allKeys):
                keybaord_input_2.keys = _keybaord_input_2_allKeys[-1].name  # just the last key pressed
                keybaord_input_2.rt = _keybaord_input_2_allKeys[-1].rt
                # was this correct?
                if (keybaord_input_2.keys == str(correct_ans)) or (keybaord_input_2.keys == correct_ans):
                    keybaord_input_2.corr = 1
                else:
                    keybaord_input_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in screen_display_imagesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "screen_display_images" ---
    for thisComponent in screen_display_imagesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from estimate_frame_durations_2
    thisExp.addData('trial_frame_durations', t_frame_time);
    # check responses
    if keybaord_input_2.keys in ['', [], None]:  # No response was made
        keybaord_input_2.keys = None
        # was no response the correct answer?!
        if str(correct_ans).lower() == 'none':
           keybaord_input_2.corr = 1;  # correct non-response
        else:
           keybaord_input_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('keybaord_input_2.keys',keybaord_input_2.keys)
    trials.addData('keybaord_input_2.corr', keybaord_input_2.corr)
    if keybaord_input_2.keys != None:  # we had a response
        trials.addData('keybaord_input_2.rt', keybaord_input_2.rt)
    # the Routine "screen_display_images" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inter_trial_interval" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from randomize_iti
    t_start_time = exp_clock.getTime()
    t_frame_time = []
    
    iti_duration = random.randint(1000,3000)/1000 # duration in msec units
    
    print(iti_duration)
    print('printed boundingbox', widget5_text1.boundingBox)
    
    background_panel_2.setPos([panel_layout.panel_position])
    background_panel_2.setSize((panel_layout.panel_x, panel_layout.panel_y))
    panel1_2.setPos((widget_regions[0]['x'], widget_regions[0]['y']))
    panel1_2.setSize((widget_regions[0]['width'], widget_regions[0]['height']))
    panel2_2.setPos((widget_regions[1]['x'], widget_regions[1]['y']))
    panel2_2.setSize((widget_regions[1]['width'], widget_regions[1]['height']))
    panel3_2.setPos((widget_regions[2]['x'], widget_regions[2]['y']))
    panel3_2.setSize((widget_regions[2]['width'], widget_regions[2]['height']))
    panel4_2.setPos((widget_regions[3]['x'], widget_regions[3]['y']))
    panel4_2.setSize((widget_regions[3]['width'], widget_regions[3]['height']))
    panel5_2.setPos((widget_regions[4]['x'], widget_regions[4]['y']))
    panel5_2.setSize((widget_regions[4]['width'], widget_regions[4]['height']))
    panel6_2.setPos((widget_regions[5]['x'], widget_regions[5]['y']))
    panel6_2.setSize((widget_regions[5]['width'], widget_regions[5]['height']))
    widget1_symbol1_2.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["duration"])])
    widget1_symbol1_2.setSize(onethird_icon_size)
    widget1_symbol1_2.setImage(trip_widget["img_files"]["duration"])
    widget1_symbol2_2.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["fuel"])])
    widget1_symbol2_2.setSize(onethird_icon_size)
    widget1_symbol2_2.setImage(trip_widget["img_files"]["fuel"])
    widget1_symbol3_2.setPos([correctPositionSmall(onethird_icon_size, trip_widget["sym_component_positions"]["distance"])])
    widget1_symbol3_2.setSize(onethird_icon_size)
    widget1_symbol3_2.setImage(trip_widget["img_files"]["distance"])
    widget1_text1_2.setPos([trip_widget["txt_component_positions"]["duration"]])
    widget1_text1_2.setText(trip_widget["components"]["duration"])
    widget1_text1_2.setHeight(text_size)
    widget1_text2_2.setPos([trip_widget["txt_component_positions"]["fuel"]])
    widget1_text2_2.setText(trip_widget["components"]["fuel"])
    widget1_text2_2.setHeight(text_size)
    widget1_text3_2.setPos([trip_widget["txt_component_positions"]["distance"]])
    widget1_text3_2.setText(trip_widget["components"]["distance"])
    widget1_text3_2.setHeight(text_size)
    widget1_text4_2.setPos([trip_widget["txt_component_positions"]["header"]])
    widget1_text4_2.setText(trip_widget["components"]["header"])
    widget1_text4_2.setHeight(header_size)
    widget2_symbol1_2.setPos([correctPositionSmall(garage_icon_size, garage_widget["sym_component_positions"]["garage"])])
    widget2_symbol1_2.setSize(garage_icon_size)
    widget2_symbol1_2.setImage(garage_widget["img_files"]["garage"])
    widget2_text1_2.setPos([garage_widget["txt_component_positions"]["header"]])
    widget2_text1_2.setText(garage_widget["components"]["header"])
    widget2_text1_2.setHeight(header_size)
    widget2_text2_2.setPos([garage_widget["txt_component_positions"]["garage"]])
    widget2_text2_2.setText(garage_widget["components"]["garage"])
    widget2_text2_2.setHeight(text_size)
    widget3_symbol1_2.setPos([correctPosition(full_icon_size, temperature_widget["sym_component_positions"]["temperature"])])
    widget3_symbol1_2.setSize(full_icon_size)
    widget3_symbol1_2.setImage(temperature_widget["img_files"]["temperature"])
    widget4_symbol1_2.setPos([correctPosition(full_icon_size, battery_widget["sym_component_positions"]["battery"])])
    widget4_symbol1_2.setSize(full_icon_size)
    widget4_symbol1_2.setImage(battery_widget["img_files"]["battery"])
    widget5_text1_2.setPos([day_widget["txt_component_positions"]["header"]])
    widget5_text1_2.setText(day_widget["components"]["header"])
    widget5_text1_2.setHeight(day_size)
    widget5_symbol1_2.setPos([correctPosition(half_icon_size, day_widget["sym_component_positions"]["calendar"])])
    widget5_symbol1_2.setSize(half_icon_size)
    widget5_symbol1_2.setImage(day_widget["img_files"]["calendar"])
    # Run 'Begin Routine' code from align_text_2
    alignment_var = "left"
    
    
    widget1_text1_2.alignText = alignment_var
    widget1_text2_2.alignText = alignment_var
    widget1_text3_2.alignText = alignment_var
    widget1_text4_2.alignText = alignment_var
    
    widget2_text1_2.alignText = alignment_var
    widget2_text2_2.alignText = alignment_var
    
    widget5_text1_2.alignText = alignment_var
    
    widget1_text4_2.bold = True
    widget2_text1_2.bold = True
    widget5_text1_2.bold = True
    
    
    # keep track of which components have finished
    inter_trial_intervalComponents = [background_panel_2, panel1_2, panel2_2, panel3_2, panel4_2, panel5_2, panel6_2, widget1_symbol1_2, widget1_symbol2_2, widget1_symbol3_2, widget1_text1_2, widget1_text2_2, widget1_text3_2, widget1_text4_2, widget2_symbol1_2, widget2_text1_2, widget2_text2_2, widget3_symbol1_2, widget4_symbol1_2, widget5_text1_2, widget5_symbol1_2]
    for thisComponent in inter_trial_intervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "inter_trial_interval" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from randomize_iti
        t_frame_time.append(round((exp_clock.getTime() - t_start_time)*1000,2))
        
        t_start_time = exp_clock.getTime()
        
        # *background_panel_2* updates
        if background_panel_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background_panel_2.frameNStart = frameN  # exact frame index
            background_panel_2.tStart = t  # local t and not account for scr refresh
            background_panel_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_panel_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_panel_2.started')
            background_panel_2.setAutoDraw(True)
        if background_panel_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_panel_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                background_panel_2.tStop = t  # not accounting for scr refresh
                background_panel_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_panel_2.stopped')
                background_panel_2.setAutoDraw(False)
        
        # *panel1_2* updates
        if panel1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel1_2.frameNStart = frameN  # exact frame index
            panel1_2.tStart = t  # local t and not account for scr refresh
            panel1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel1_2.started')
            panel1_2.setAutoDraw(True)
        if panel1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel1_2.tStop = t  # not accounting for scr refresh
                panel1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel1_2.stopped')
                panel1_2.setAutoDraw(False)
        
        # *panel2_2* updates
        if panel2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel2_2.frameNStart = frameN  # exact frame index
            panel2_2.tStart = t  # local t and not account for scr refresh
            panel2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel2_2.started')
            panel2_2.setAutoDraw(True)
        if panel2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel2_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel2_2.tStop = t  # not accounting for scr refresh
                panel2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel2_2.stopped')
                panel2_2.setAutoDraw(False)
        
        # *panel3_2* updates
        if panel3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel3_2.frameNStart = frameN  # exact frame index
            panel3_2.tStart = t  # local t and not account for scr refresh
            panel3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel3_2.started')
            panel3_2.setAutoDraw(True)
        if panel3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel3_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel3_2.tStop = t  # not accounting for scr refresh
                panel3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel3_2.stopped')
                panel3_2.setAutoDraw(False)
        
        # *panel4_2* updates
        if panel4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel4_2.frameNStart = frameN  # exact frame index
            panel4_2.tStart = t  # local t and not account for scr refresh
            panel4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel4_2.started')
            panel4_2.setAutoDraw(True)
        if panel4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel4_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel4_2.tStop = t  # not accounting for scr refresh
                panel4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel4_2.stopped')
                panel4_2.setAutoDraw(False)
        
        # *panel5_2* updates
        if panel5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel5_2.frameNStart = frameN  # exact frame index
            panel5_2.tStart = t  # local t and not account for scr refresh
            panel5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel5_2.started')
            panel5_2.setAutoDraw(True)
        if panel5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel5_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel5_2.tStop = t  # not accounting for scr refresh
                panel5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel5_2.stopped')
                panel5_2.setAutoDraw(False)
        
        # *panel6_2* updates
        if panel6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            panel6_2.frameNStart = frameN  # exact frame index
            panel6_2.tStart = t  # local t and not account for scr refresh
            panel6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(panel6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'panel6_2.started')
            panel6_2.setAutoDraw(True)
        if panel6_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel6_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel6_2.tStop = t  # not accounting for scr refresh
                panel6_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel6_2.stopped')
                panel6_2.setAutoDraw(False)
        
        # *widget1_symbol1_2* updates
        if widget1_symbol1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol1_2.frameNStart = frameN  # exact frame index
            widget1_symbol1_2.tStart = t  # local t and not account for scr refresh
            widget1_symbol1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol1_2.started')
            widget1_symbol1_2.setAutoDraw(True)
        if widget1_symbol1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_symbol1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_symbol1_2.tStop = t  # not accounting for scr refresh
                widget1_symbol1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_symbol1_2.stopped')
                widget1_symbol1_2.setAutoDraw(False)
        
        # *widget1_symbol2_2* updates
        if widget1_symbol2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol2_2.frameNStart = frameN  # exact frame index
            widget1_symbol2_2.tStart = t  # local t and not account for scr refresh
            widget1_symbol2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol2_2.started')
            widget1_symbol2_2.setAutoDraw(True)
        if widget1_symbol2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_symbol2_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_symbol2_2.tStop = t  # not accounting for scr refresh
                widget1_symbol2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_symbol2_2.stopped')
                widget1_symbol2_2.setAutoDraw(False)
        
        # *widget1_symbol3_2* updates
        if widget1_symbol3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_symbol3_2.frameNStart = frameN  # exact frame index
            widget1_symbol3_2.tStart = t  # local t and not account for scr refresh
            widget1_symbol3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_symbol3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_symbol3_2.started')
            widget1_symbol3_2.setAutoDraw(True)
        if widget1_symbol3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_symbol3_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_symbol3_2.tStop = t  # not accounting for scr refresh
                widget1_symbol3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_symbol3_2.stopped')
                widget1_symbol3_2.setAutoDraw(False)
        
        # *widget1_text1_2* updates
        if widget1_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text1_2.frameNStart = frameN  # exact frame index
            widget1_text1_2.tStart = t  # local t and not account for scr refresh
            widget1_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text1_2.started')
            widget1_text1_2.setAutoDraw(True)
        if widget1_text1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_text1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_text1_2.tStop = t  # not accounting for scr refresh
                widget1_text1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_text1_2.stopped')
                widget1_text1_2.setAutoDraw(False)
        
        # *widget1_text2_2* updates
        if widget1_text2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text2_2.frameNStart = frameN  # exact frame index
            widget1_text2_2.tStart = t  # local t and not account for scr refresh
            widget1_text2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text2_2.started')
            widget1_text2_2.setAutoDraw(True)
        if widget1_text2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_text2_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_text2_2.tStop = t  # not accounting for scr refresh
                widget1_text2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_text2_2.stopped')
                widget1_text2_2.setAutoDraw(False)
        
        # *widget1_text3_2* updates
        if widget1_text3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text3_2.frameNStart = frameN  # exact frame index
            widget1_text3_2.tStart = t  # local t and not account for scr refresh
            widget1_text3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text3_2.started')
            widget1_text3_2.setAutoDraw(True)
        if widget1_text3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_text3_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_text3_2.tStop = t  # not accounting for scr refresh
                widget1_text3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_text3_2.stopped')
                widget1_text3_2.setAutoDraw(False)
        
        # *widget1_text4_2* updates
        if widget1_text4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget1_text4_2.frameNStart = frameN  # exact frame index
            widget1_text4_2.tStart = t  # local t and not account for scr refresh
            widget1_text4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget1_text4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget1_text4_2.started')
            widget1_text4_2.setAutoDraw(True)
        if widget1_text4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget1_text4_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget1_text4_2.tStop = t  # not accounting for scr refresh
                widget1_text4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget1_text4_2.stopped')
                widget1_text4_2.setAutoDraw(False)
        
        # *widget2_symbol1_2* updates
        if widget2_symbol1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_symbol1_2.frameNStart = frameN  # exact frame index
            widget2_symbol1_2.tStart = t  # local t and not account for scr refresh
            widget2_symbol1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_symbol1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_symbol1_2.started')
            widget2_symbol1_2.setAutoDraw(True)
        if widget2_symbol1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget2_symbol1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget2_symbol1_2.tStop = t  # not accounting for scr refresh
                widget2_symbol1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget2_symbol1_2.stopped')
                widget2_symbol1_2.setAutoDraw(False)
        
        # *widget2_text1_2* updates
        if widget2_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_text1_2.frameNStart = frameN  # exact frame index
            widget2_text1_2.tStart = t  # local t and not account for scr refresh
            widget2_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_text1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_text1_2.started')
            widget2_text1_2.setAutoDraw(True)
        if widget2_text1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget2_text1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget2_text1_2.tStop = t  # not accounting for scr refresh
                widget2_text1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget2_text1_2.stopped')
                widget2_text1_2.setAutoDraw(False)
        
        # *widget2_text2_2* updates
        if widget2_text2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget2_text2_2.frameNStart = frameN  # exact frame index
            widget2_text2_2.tStart = t  # local t and not account for scr refresh
            widget2_text2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget2_text2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget2_text2_2.started')
            widget2_text2_2.setAutoDraw(True)
        if widget2_text2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget2_text2_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget2_text2_2.tStop = t  # not accounting for scr refresh
                widget2_text2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget2_text2_2.stopped')
                widget2_text2_2.setAutoDraw(False)
        
        # *widget3_symbol1_2* updates
        if widget3_symbol1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget3_symbol1_2.frameNStart = frameN  # exact frame index
            widget3_symbol1_2.tStart = t  # local t and not account for scr refresh
            widget3_symbol1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget3_symbol1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget3_symbol1_2.started')
            widget3_symbol1_2.setAutoDraw(True)
        if widget3_symbol1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget3_symbol1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget3_symbol1_2.tStop = t  # not accounting for scr refresh
                widget3_symbol1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget3_symbol1_2.stopped')
                widget3_symbol1_2.setAutoDraw(False)
        
        # *widget4_symbol1_2* updates
        if widget4_symbol1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget4_symbol1_2.frameNStart = frameN  # exact frame index
            widget4_symbol1_2.tStart = t  # local t and not account for scr refresh
            widget4_symbol1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget4_symbol1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget4_symbol1_2.started')
            widget4_symbol1_2.setAutoDraw(True)
        if widget4_symbol1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget4_symbol1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget4_symbol1_2.tStop = t  # not accounting for scr refresh
                widget4_symbol1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget4_symbol1_2.stopped')
                widget4_symbol1_2.setAutoDraw(False)
        
        # *widget5_text1_2* updates
        if widget5_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget5_text1_2.frameNStart = frameN  # exact frame index
            widget5_text1_2.tStart = t  # local t and not account for scr refresh
            widget5_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget5_text1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget5_text1_2.started')
            widget5_text1_2.setAutoDraw(True)
        if widget5_text1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget5_text1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget5_text1_2.tStop = t  # not accounting for scr refresh
                widget5_text1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget5_text1_2.stopped')
                widget5_text1_2.setAutoDraw(False)
        
        # *widget5_symbol1_2* updates
        if widget5_symbol1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            widget5_symbol1_2.frameNStart = frameN  # exact frame index
            widget5_symbol1_2.tStart = t  # local t and not account for scr refresh
            widget5_symbol1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(widget5_symbol1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'widget5_symbol1_2.started')
            widget5_symbol1_2.setAutoDraw(True)
        if widget5_symbol1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > widget5_symbol1_2.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                widget5_symbol1_2.tStop = t  # not accounting for scr refresh
                widget5_symbol1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'widget5_symbol1_2.stopped')
                widget5_symbol1_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inter_trial_intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inter_trial_interval" ---
    for thisComponent in inter_trial_intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from randomize_iti
    thisExp.addData('trial_frame_durations', t_frame_time);
    # the Routine "inter_trial_interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
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
