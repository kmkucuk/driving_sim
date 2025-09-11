import calendar
import random
from datetime import date
from datetime import datetime
import os
import pandas as pd
from pathlib import Path
import random
TEXT_WIDGETS_ENABLED = False
IMAGE_WIDGETS_ENABLED = True
SMALL_ICON_SIZE_RATIO = [0.5, 0.5]
LARGE_ICON_SIZE_RATIO = [0.5, 0.5]


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
                {"name": "maintenance_widget",
                "possible_regions": large_region_indices, 
                "region_index": 0,
                "text_components": {},
                 "image_components": 
                 {"engine": {"file":  getImageWithKeyword("./stimuli/clutter", "engine_1"), 
                               "position_percentage": [50, 25], "position_pixel": [],
                               "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []}, 
                  "oil": {"file":  getImageWithKeyword("./stimuli/clutter", "oil_1"), 
                           "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []},
                  "tirepressure": {"file":  getImageWithKeyword("./stimuli/clutter", "tirepressure_1"), 
                           "position_percentage": [50, 75], "position_pixel": [],
                               "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []}
                  },
                },
                
                {"name": "drive_widget",
                 "possible_regions": large_region_indices,
                 "region_index": 5,
                 "text_components": {},
                 "image_components": 
                 {"fuel": {"file":  getImageWithKeyword("./stimuli/clutter", "fuel_1"), 
                               "position_percentage": [50 , 25], "position_pixel": [],
                               "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []},
                    "ecosport": {"file":  getImageWithKeyword("./stimuli/clutter", "ecosport_1"), 
                                    "position_percentage": [50 , 50], "position_pixel": [],
                                    "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []},
                    "farlight": {"file":  getImageWithKeyword("./stimuli/clutter", "farlight_1"), 
                                    "position_percentage": [50 , 75], "position_pixel": [],
                                    "size_ratio": SMALL_ICON_SIZE_RATIO, "size_pixel": []}
                  },
                },
                
                {"name": "cardoor_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 1, 
                 "text_components": {},
                 "image_components": 
                 {"cardoor": {"file":  getImageWithKeyword("./stimuli/clutter", "cardoor_1"), 
                             "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": LARGE_ICON_SIZE_RATIO, "size_pixel": []}
                  },
                },

                {"name": "carheat_widget",
                "possible_regions": small_region_indices, 
                 "region_index": 3, 
                 "text_components": {},
                 "image_components": 
                 {"carheat": {"file":  getImageWithKeyword("./stimuli/clutter", "carheat_1"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": LARGE_ICON_SIZE_RATIO, "size_pixel": []}
                  },
                },

                {"name": "media_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 4, 
                 "text_components": {},
                 "image_components": 
                 {"media": {"file":  getImageWithKeyword("./stimuli/clutter", "media_1"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": LARGE_ICON_SIZE_RATIO, "size_pixel": []}
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
    widget_index = all_widgets[index]["region_index"]

    if TEXT_WIDGETS_ENABLED:
        curr_dyn_clutter = dynamic_clutter_values[index]
        for key, val in curr_dyn_clutter.items():
            all_widgets[index]["text_components"][key]["text"] = updateText(val, key)

        curr_text_comps = all_widgets[index]["text_components"]
        for key, val in curr_text_comps.items():
            all_widgets[index]["text_components"][key]["position_pixel"] = getPositions(widget_regions[widget_index], val["position_percentage"])

    if IMAGE_WIDGETS_ENABLED:
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

exp_version = "WITH_clutter"

# randomization
first_block = [1,2,3]
second_block = [5,6,7]
random.shuffle(first_block)
random.shuffle(second_block)
block_rows = [0] + first_block + [4] + second_block

if expInfo['monitor_cb'] == '1':
    pixPerCm = 36.974
elif expInfo['monitor_cb'] == '2':
    pixPerCm = 100
else:
    raise ValueError('Wrong MONITOR counterbalance group, it should be 1 or 2 (CHECK initalization > exp_init > line 281)')

stim_cm = 0.4349
stim_size = stim_cm * pixPerCm 

mask_imgs = getFilesInDir("./stimuli/masks")

frameRate = win.getActualFrameRate();
# convert to py float
frameRate = frameRate.item()
if frameRate == None:
    frameRate = 60    
secPerFrame = 1 / frameRate

scoreScreen = {}

scoreScreen["lexical_only"] = {"accuracy": [], "reaction_time": []}
scoreScreen["driving_lexical"] = {"accuracy": [], "reaction_time": []}

if expInfo["clutter_test"] == "yes":
    blocks_file = "blocks_final_express.xlsx"
else:
    blocks_file = "blocks_final.xlsx"