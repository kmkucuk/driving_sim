from pprint import pprint
import calendar
import json
import math
import random
from datetime import date
from datetime import datetime
import os
from staircasing import staircaseFunction
from masking import getFilesInDir, selectRandomMask
import pandas as pd
from pathlib import Path
import os
from PIL import Image

def getIconInfo(folder_path):

    if not folder_path:
        print("No folder selected.")
        return {}
    
    files_info = {}
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(file_name)
            ext = ext.lower().strip(".")
            
            file_data = {"extension": ext, "dimension": None}
            
            try:
                with Image.open(file_path) as img:
                    file_data["dimension"] = list(img.size) 
            except Exception:
                pass
            
            files_info[name] = file_data
    
    return files_info

def getClutterOrderCounterbalanceGroup(order_file = "clutter_change_order_cb.xlsx", cb_group = "1", practice_change_count = 5):
    if not isinstance(cb_group, str):
        raise ValueError(f"Counterbalance group is not entered as string {cb_group}, its type is instead {type(cb_group)}")

    xlsx_path = Path(order_file)

    df = pd.read_excel(xlsx_path)

    df.columns = [str(c).strip().lower() for c in df.columns]

    df.head(), df.columns.tolist()
    required = {"blocks", "block_trial_#", "gr1", "gr2", "gr3", "gr4"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    def block_num(s):
        try:
            return int(str(s).split()[-1])
        except Exception:
            return str(s)

    grouped = sorted(df.groupby("blocks"), key=lambda kv: block_num(kv[0]))

    gr_lists = {"gr1": [], "gr2": [], "gr3": [], "gr4": []}
    block_labels = []

    for block_label, g in grouped:
        block_labels.append(block_label)
        for gr in gr_lists.keys():
            idx = g.loc[g[gr].astype(int) == 1, "block_trial_#"].astype(int).tolist()
            gr_lists[gr].append(idx)

    # insert two randomly generated change index for the two clutter training parts
    random_practice_indices1 = random.sample(range(0, 20), practice_change_count)
    random_practice_indices2 = random.sample(range(0, 20), practice_change_count)
    random_practice_indices1.sort()
    random_practice_indices2.sort()
    gr_lists["gr" + cb_group].insert(0, random_practice_indices2)
    gr_lists["gr" + cb_group].insert(0, random_practice_indices1)
    
    selected_list = gr_lists["gr" + cb_group]
    print(f"Selected clutter change order group {cb_group} indices are: {selected_list}")
    return selected_list
    


def getRandomChangingIconIndex(clutter_change_v, number_of_changes):
    clutterIconChangeIndex = []
    while True:     
        for i in range(0, number_of_changes):
            clutterIconChangeIndex.extend(random.sample(clutter_change_v, 
                                        min(len(clutter_change_v), 
                                            number_of_changes - len(clutterIconChangeIndex))))
            if len(clutterIconChangeIndex) == number_of_changes:
                return clutterIconChangeIndex

def changeClutterIcon(all_widgets, dynamic_clutter_icons, clutter_index):
    cur_key = dynamic_clutter_icons[clutter_index[0]][clutter_index[1]]
    all_widgets[clutter_index[0]]["image_components"][cur_key]["file"] = getImageWithKeyword("./stimuli/clutter", cur_key + "_2")
    thisExp.addData('clutter_changed_icon', cur_key)


def revertClutterIcon(all_widgets, dynamic_clutter_icons, clutter_index):
    cur_key = dynamic_clutter_icons[clutter_index[0]][clutter_index[1]]
    all_widgets[clutter_index[0]]["image_components"][cur_key]["file"] = getImageWithKeyword("./stimuli/clutter", cur_key + "_1")


def getFrames(component_duration, secPerFrame):
    return round(component_duration / secPerFrame)

def trialSampling(vector, n):
    if n > len(vector):
        raise ValueError("n cannot be greater than the length of the vector.")
    
    return random.sample(vector, n)

def joinAndShuffle(vector1, vector2):
    combined = vector1 + vector2
    random.shuffle(combined)
    return combined

def removeElements(source_vector, elements_to_remove):
    result = [x for x in source_vector if x not in elements_to_remove]
    return result


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
        return [text_position[0] + text_stim.boundingBox[0]/2, text_position[1]]
    else:
        return text_position

def correctPosition(icon_size, icon_position):    
    """deprecated after update on positioning and sizes"""
    return icon_position
#    return [icon_position[0] - icon_size[0]/2,
#    icon_position[1] - icon_size[1]/2] # math.copysign(icon_size[0], icon_position[0])/2, math.copysign(icon_size[1], icon_position[1])/2]
#    
    
def correctPositionSmall(icon_size, icon_position):    
    """deprecated after update on positioning and sizes"""
    return icon_position
#    return [icon_position[0] + icon_size[0]/2, icon_position[1]]



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
            
            