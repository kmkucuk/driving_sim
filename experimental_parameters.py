import calendar
import json
import math
import random
from datetime import date
from datetime import datetime
import os



def getChangeIndex(dyn_values, chang_indx):
    change_order = []
    # chang_indx represents the len(keys) in dynamic_clutter_values
    
    while True:
        rand_indx = random.randint(0, len(chang_indx) - 1)
        if chang_indx[rand_indx] != 0:
            cur_clut = dyn_values[rand_indx]
            keys = list(cur_clut.keys())
            selectAgain = False
            while True:
                rand_keyi = random.randint(0, len(keys) - 1)
                selected_key = keys[rand_keyi]                    
                for ki in range(0, len(change_order)):
                    lookup_key = change_order[ki][1]
                    if selected_key == lookup_key:
                        selectAgain = True
                if selectAgain:
                    break
                else:
                    change_order.append([rand_indx, selected_key])
                    chang_indx[rand_indx] = chang_indx[rand_indx] - 1
                    break
        elif sum(chang_indx) == 0:
            break
    return change_order

def generateChangeSequence():
    return random.sample(range(1, 12), 8)

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

        return str_num_day + " " + month +"\n" + calendar.day_name[my_date.weekday()] # e.g. 'Wednesday'\nNumber   

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
# 12 trials, 8 total widgets, how many clutter change?
# 8?

# select 1 index, che


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