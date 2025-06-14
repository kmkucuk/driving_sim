﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on June 13, 2025, at 16:21
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
    originPath='E:\\Backups\\All Files\\Genel\\Is\\2022\\Upwork\\LabX\\studies\\materials\\drivingSimulator\\repo\\car_panel_lexical_decision_no_clutter_v1_lastrun.py',
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
from pprint import pprint
import calendar
import json
import math
import random
from datetime import date
from datetime import datetime
import os

def getDateTimeText():
    # get current day for text display on calemdar widget
    my_date = date.today()
    today = datetime.now()
    month_index = datetime.now().month
    month = calendar.month_name[month_index]
    numeric_day = today.day # this is a integer
    str_num_day = str(numeric_day)
    if str_num_day[-1] == '1':
        day_suffix = 'st'
    elif str_num_day[-1] == '2':
        day_suffix = 'nd'
    elif str_num_day[-1] == '3':
        day_suffix = 'rd'
    elif int(str_num_day[-1]) >= 4:
        day_suffix = 'th'                
    
    return str_num_day + day_suffix + " " + month +"\n" + calendar.day_name[my_date.weekday()] # e.g. 'Wednesday'\nNumber   


def getImageWithKeyword(directory, keyword):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions) and keyword.lower() in file.lower():
                return "/".join([root, file])
                
def correctTextPosition(text_stim, text_position):
    if hasattr(text_stim, 'boundingBox'):
        print('HERE IS THE BOUNDING BOX ', text_stim.boundingBox)
        return [text_position[0] + text_stim.boundingBox[0]/2, text_position[1]]
    else:
        return text_position

def correctPosition(icon_size, icon_position):    
    return icon_position
#    return [icon_position[0] - icon_size[0]/2,
#    icon_position[1] - icon_size[1]/2] # math.copysign(icon_size[0], icon_position[0])/2, math.copysign(icon_size[1], icon_position[1])/2]
#    
    
def correctPositionSmall(icon_size, icon_position):    
    return icon_position
#    return [icon_position[0] + icon_size[0]/2, icon_position[1]]
# Run 'Begin Experiment' code from panel_initialization

# Example usage:
class Panel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.column_spacing = 0.03
        self.row_spacing = 0.03
        self.scale_ratios = [1, 2/3]
        self.scale_empty_part = "bottom"
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

    def panel_separator(self, panel, separation_count, separation_direction):
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
            isHorizontal = -1
        elif separation_direction == "horizontal":
            separation_axis = 'x'
            separation_size = 'width'
            isHorizontal = 1
        else:
            ValueError('f{separation_direction} is not a valid separation direction')    
        
        section_size = panel[separation_size] / separation_count
        section_origin = panel[separation_axis] + (panel[separation_size] / 2)      

        clutter_regions = []
        dummy_region = {}
        for i in range(0, separation_count):            
            dummy_region = dict(panel)

            
            start_border = isHorizontal * round(i*section_size)
            end_border = isHorizontal * round((i+1)*section_size)
                      

            section_start = round(section_origin + start_border) # find region's start
            section_end = round(section_origin + end_border)
            section_mid = round((section_start + section_end) / 2) # find midpoint between region's start and end                        

            dummy_region[separation_axis] = section_start
            dummy_region[separation_size] = section_size
            clutter_regions.append(dummy_region)           

        return clutter_regions

    def get_clutter_coordinate(self, clutter_region, direction, placement_index, placement_description=None):
        """ This function is used for obtaining axis coordinates for clutter placement

        :param clutter_region: (dict) enter the clutter's region dictionary obtained by clutter_separator (e.g. clutter[0] or clutter[target_clutter])

        :param placement_index: (int) List of 2 integers indicating the placement:
                - [place_index, place_range] > [1, 4] > [0, 1, 2, 3] > second element (1) is the coordinate
        :param placement_description: "top" or "mid" part of the segmented region
        :return: point in coordinate system (x, y)
        """
        if direction == "vertical":
            placement_axis = 'y'
            placement_size = 'height'
            isHorizontal = -1
            section_origin =  clutter_region[placement_axis]
        elif direction == "horizontal":
            placement_axis = 'x'
            placement_size = 'width'
            isHorizontal = 1
            section_origin =  clutter_region[placement_axis] - (clutter_region[placement_size] / 2)
        else:
            ValueError('f{separation_direction} is not a valid separation direction') 

        if placement_description == None:
            placement_description = "mid"
        
        section_count = placement_index[1]
        
        section_size = clutter_region[placement_size] / section_count

        for i in range(0, section_count):            
            start_border = isHorizontal * round(i*section_size)
            end_border = isHorizontal * round((i+1)*section_size)

            section_start = section_origin + start_border
            section_end = section_origin + end_border
            section_mid = round((section_start + section_end) / 2)

            if i == placement_index[0]:
                if placement_description == "mid":
                    return section_mid
                elif placement_description == "top":
                    if placement_axis == 'y':
                        print('selected top - section start', section_start)
                        print('selected top - section origin', section_origin)
                    return section_start
                elif placement_description == "bottom":
                    return section_end

    def getImageWithKeyword(self, directory, keyword):
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions) and keyword.lower() in file.lower():
                    return "/".join([root, file])

# Run 'Begin Experiment' code from exp_init

def getGarageText(boolean):
    if boolean == 0:
        return "Garage Door\nClosed"
    elif boolean == 1:
        return "Garage Door\nOpen"
    else:
        ValueError("Garage door clutter value is not valid.")

def getDateTimeText(value):
    """
    param day_shift: used for changing the day display on the panel for changing clutter
    condition. adding or subtracting int value from day of the month (13 +- day_shift ) 
    """
    
    # get current day for text display on calemdar widget
    my_date = date.today()
    today = datetime.now()
    month_index = datetime.now().month
    month = calendar.month_name[month_index]
    numeric_day = today.day # this is a integer
    if numeric_day + value <= 0 or numeric_day + value > 31:
        ValueError("Unacceptable day of the month after subtracting the clutter change value.")
    else:
        str_num_day = str(numeric_day + value)
        if str_num_day[-1] == '1':
            day_suffix = 'st'
        elif str_num_day[-1] == '2':
            day_suffix = 'nd'
        elif str_num_day[-1] == '3':
            day_suffix = 'rd'
        elif int(str_num_day[-1]) >= 4:
            day_suffix = 'th'    

        return str_num_day + day_suffix + " " + month +"\n" + calendar.day_name[my_date.weekday()] # e.g. 'Wednesday'\nNumber   

def updateText(value, key):

    if key == "duration":
        return ('').join(["1 hr ", str(value), " min"])
    elif key == "fuel":
        return ('').join([str(value) , " mpg"])
    elif key == "distance":
        return ('').join([str(value) , " mi"])
    elif key == "date":
        return getDateTimeText(value)
    elif key == "garage_door":
        return getGarageText(value)
    elif key == "battery":
        return ('').join(["%", str(value)])
    elif key == "miles":
        return ('').join([str(value), "mi"])
    elif key == "temperature":
        return ('').join([str(value), "F"])
    else:
        KeyError('Widget was not found [', key,']')


def getImageWithKeyword(directory, keyword):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions) and keyword.lower() in file.lower():
                return "/".join([root, file])



def getPositions(widget_regions, position_percentage):
    """ This function is used for obtaining axis coordinates for clutter placement

    :param clutter_region: (dict) enter the clutter's region dictionary obtained by clutter_separator (e.g. clutter[0] or clutter[target_clutter])

    :param position_percentages: (int) List of 2 integers indicating the placement in percentage of the clutter region size:
             [25, 50] => [width * 25/100, height * 50/100]
    :return: point in coordinate system (x, y)
    """

    y_origin = widget_regions['y'] + (widget_regions['height']/2)
    x_origin = widget_regions['x'] - (widget_regions['width']/2)

    return [round(x_origin + widget_regions['width']*(position_percentage[0]/100)), 
            round(y_origin - widget_regions['height']*(position_percentage[1]/100))]


def getIconSize(widget_regions, size_ratio):
    """ This function is used for obtaining axis coordinates for clutter placement

    :param widget_regions: (dict) enter the clutter's region dictionary obtained by clutter_separator (e.g. clutter[0] or clutter[target_clutter])

    :param size_ratio: (int) List of 2 integers indicating the ratio of icon size relative to the widget region's width
    :return: size in pixels (w, h)
    """
    return [round(widget_regions['width']*(size_ratio[0])), 
            round(widget_regions['width']*(size_ratio[1]))]
    
if 'win' not in locals():
    from panel_generation_function import Panel
    class win:
        def __init__(self):
            self.size = [1920, 1080]
    window = win()
    panel_layout = Panel(window.size[0], window.size[1])

else:
    panel_layout = Panel(win.size[0], win.size[1])

widget_regions = panel_layout.generate_panel_layout([1, 0, 0, 1]) 

target_panel = 2
large_region_indices = [0, 5]
small_region_indices = [1, 2, 3, 4]
if target_panel in large_region_indices:
    large_region_indices.remove(target_panel)
elif target_panel in small_region_indices:
    small_region_indices.remove(target_panel)
 
all_widgets = [
                {"name": "trip_widget",
                "possible_regions": large_region_indices, 
                "region_index": 0,
                "text_components": 
                    {"trip_header": {"text": "Current Trip", "position_percentage": [15, 10], "position_pixel": []},
                    "duration": {"text": "", "position_percentage": [35, 25], "position_pixel": []},  
                    "fuel": {"text": "", "position_percentage": [35, 50], "position_pixel": []}, 
                    "distance": {"text": "", "position_percentage": [35, 75], "position_pixel": []}
                    },
                 "image_components": 
                 {"duration": {"file":  getImageWithKeyword("./stimuli/clutter", "duration"), 
                               "position_percentage": [20, 25], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}, 
                  "fuel": {"file":  getImageWithKeyword("./stimuli/clutter", "fuel"), 
                           "position_percentage": [20, 50], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}, 
                  "distance": {"file":  getImageWithKeyword("./stimuli/clutter", "distance"), 
                               "position_percentage": [20, 75], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}
                  },
                },

                {"name": "calendar_widget",
                 "possible_regions": large_region_indices,
                 "region_index": 5,
                 "text_components": 
                    {"date": {"text": "", "position_percentage": [20, 15], "position_pixel": []}
                     },
                 "image_components": 
                 {"calendar": {"file":  getImageWithKeyword("./stimuli/clutter", "calendar"), 
                               "position_percentage": [50 , 70], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                },
                
                {"name": "garage_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 1, 
                 "text_components": 
                    {"garage_header": {"text": "My Home", "position_percentage": [15, 20], "position_pixel": []},
                     "garage_door": {"text": "", "position_percentage": [35, 50], "position_pixel": []}
                     },
                 "image_components": 
                 {"garage": {"file":  getImageWithKeyword("./stimuli/clutter", "garage"), 
                             "position_percentage": [20, 50], "position_pixel": [],
                               "size_ratio": [0.35, 0.35], "size_pixel": []}
                  },
                },

                {"name": "temperature_widget",
                "possible_regions": small_region_indices, 
                 "region_index": 3, 
                 "text_components": 
                    {"temperature": {"text": "", "position_percentage": [30, 40], "position_pixel": []}                   
                     },
                 "image_components": 
                 {"temperature": {"file":  getImageWithKeyword("./stimuli/clutter", "temperature"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                },

                {"name": "battery_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 4, 
                 "text_components": 
                    {"battery": {"text": "", "position_percentage": [21, 45], "position_pixel": []},
                     "miles": {"text": "", "position_percentage": [55, 63], "position_pixel": []}
                     },
                 "image_components": 
                 {"battery": {"file":  getImageWithKeyword("./stimuli/clutter", "battery"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                }
        ] 

dynamic_clutter_values = [{"duration": 28, "fuel": 34, "distance": 78}, 
                          {"date": 0}, 
                          {"garage_door": 0},
                          {"temperature": 96},
                          {"battery": 24, "miles": 76}]

# TODO: function to change order of elements in each data strct. to do what?
all_data_structures = [all_widgets, dynamic_clutter_values]

for index in range(0, len(all_widgets)):
    curr_dyn_clutter = dynamic_clutter_values[index]
    for key, val in curr_dyn_clutter.items():
        all_widgets[index]["text_components"][key]["text"] = updateText(val, key)

for index in range(0, len(all_widgets)):
    curr_text_comps = all_widgets[index]["text_components"]
    widget_index = all_widgets[index]["region_index"]
    for key, val in curr_text_comps.items():
        all_widgets[index]["text_components"][key]["position_pixel"] = getPositions(widget_regions[widget_index], val["position_percentage"])

    curr_img_comps = all_widgets[index]["image_components"]
    for key, val in curr_img_comps.items():
        all_widgets[index]["image_components"][key]["position_pixel"] = getPositions(widget_regions[widget_index], val["position_percentage"])
        all_widgets[index]["image_components"][key]["size_pixel"] = getIconSize(widget_regions[widget_index], val["size_ratio"])


# letter size is dependent on the large panel's height
letter_size = widget_regions[1]["height"] * 0.2
day_size = widget_regions[1]["width"] * 0.125
header_size = widget_regions[1]["width"]  * 0.1
temperature_size = widget_regions[1]["width"]  * 0.14
battery_size = widget_regions[1]["width"] * 0.085

textFont = "./stimuli/font/robotoflex.ttf"

text_size = widget_regions[1]["width"]/12
header_wrap_width = 500


exp_version = "no_clutter"

# --- Initialize components for Routine "screen_display_images" ---
# Run 'Begin Experiment' code from estimate_frame_durations_2
exp_clock = core.Clock()
stim_duration = 10
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "initialization" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
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
    
    
    print('is it working first')
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
    lexical_text_2.setPos((widget_regions[target_panel]['x'], widget_regions[target_panel]['y']))
    lexical_text_2.setText(text)
    lexical_text_2.setFont(currentFont)
    lexical_text_2.setHeight(letter_size)
    keybaord_input_2.keys = []
    keybaord_input_2.rt = []
    _keybaord_input_2_allKeys = []
    # keep track of which components have finished
    screen_display_imagesComponents = [background_panel, panel1, panel2, panel3, panel4, panel5, panel6, lexical_text_2, keybaord_input_2]
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
        if background_panel.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_panel.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                background_panel.tStop = t  # not accounting for scr refresh
                background_panel.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_panel.stopped')
                background_panel.setAutoDraw(False)
        
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
        if panel1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel1.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel1.tStop = t  # not accounting for scr refresh
                panel1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel1.stopped')
                panel1.setAutoDraw(False)
        
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
        if panel2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel2.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel2.tStop = t  # not accounting for scr refresh
                panel2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel2.stopped')
                panel2.setAutoDraw(False)
        
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
        if panel3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel3.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel3.tStop = t  # not accounting for scr refresh
                panel3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel3.stopped')
                panel3.setAutoDraw(False)
        
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
        if panel4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel4.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel4.tStop = t  # not accounting for scr refresh
                panel4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel4.stopped')
                panel4.setAutoDraw(False)
        
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
        if panel5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel5.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel5.tStop = t  # not accounting for scr refresh
                panel5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel5.stopped')
                panel5.setAutoDraw(False)
        
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
        if panel6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > panel6.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                panel6.tStop = t  # not accounting for scr refresh
                panel6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'panel6.stopped')
                panel6.setAutoDraw(False)
        
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
        if lexical_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lexical_text_2.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                lexical_text_2.tStop = t  # not accounting for scr refresh
                lexical_text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'lexical_text_2.stopped')
                lexical_text_2.setAutoDraw(False)
        
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
        if keybaord_input_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keybaord_input_2.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                keybaord_input_2.tStop = t  # not accounting for scr refresh
                keybaord_input_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keybaord_input_2.stopped')
                keybaord_input_2.status = FINISHED
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
    thisExp.addData('current_time', datetime.now().strftime("%H:%M:%S"));
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
    # Run 'Begin Routine' code from estimate_frame_durations
    t_start_time = exp_clock.getTime()
    t_frame_time = []
    iti_duration = random.randint(2000,5000)/1000 # duration in msec units
     
        
    background_panel_2.setPos([panel_layout.panel_position])
    background_panel_2.setSize((panel_layout.panel_x_size, panel_layout.panel_y_size))
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
    # keep track of which components have finished
    inter_trial_intervalComponents = [background_panel_2, panel1_2, panel2_2, panel3_2, panel4_2, panel5_2, panel6_2]
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
        # Run 'Each Frame' code from estimate_frame_durations
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
    # Run 'End Routine' code from estimate_frame_durations
    thisExp.addData('trial_frame_durations', t_frame_time);
    thisExp.addData('current_time', datetime.now().strftime("%H:%M:%S"));
    print('is it working second end routine')
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
