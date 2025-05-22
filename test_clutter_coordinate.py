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
    from panel_generation_function import Panel
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
text_x_parse = [7, 8]
text_y_parse = [1, 3]

garage_widget = {"info": {"parse_symbol": [symbol_x_parse, symbol_y_parse], "parse_text": [text_x_parse, text_y_parse], "widget_index": 1}, 
                 "components": {"header": "My Home",
                                "garage": "Garage Door\nOpen"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

day_widget = {"info": {"parse_symbol": [symbol_x_parse, symbol_y_parse], "parse_text": [text_x_parse, text_y_parse], "widget_index": 5}, 
                 "components": {"header": "day",
                                "calendar": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }


# first assume header to be the same size in terms of roi
# then we can adjust it to become something else (smaller then etc.)
def segment_roi(panel, roi, widget_dict):
    
    # garage widget (duration, fuel, distance)

    component_count = len(widget_dict["components"].keys())
    component_regions = panel.panel_separator(roi[widget_dict["info"]["widget_index"]], component_count, "vertical")
    iteration = 0
    widget_dict["component_regions"] = component_regions
    # garage widget (duration, fuel, distance)
    text_x_header = [1, 7]
    text_y_header = [0, 3]
    for key, comp_val in widget_dict["components"].items():        
        

        if key != "header":
            # get symbol positions 
            placement_desc = "top"
            widget_dict["sym_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse_symbol"][0], placement_desc), 
            panel.get_clutter_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse_symbol"][1])]
            widget_dict["img_files"][key] = panel.getImageWithKeyword("./stimuli/clutter", key)

           
        if key == "header":
            text_x_header = [1, 3]
            placement_desc = "top"
            # headers are more leftward than regular text, hence specific text parsing
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "horizontal", text_x_header), 
                                                           panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "vertical", text_y_header, placement_desc)]
            if comp_val == "day":
                # get current day for text display on calemdar widget
                my_date = date.today()
                today = datetime.now()
                numeric_day = today.day # this is a integer
                widget_dict["components"]["header"] = calendar.day_name[my_date.weekday()] #+"\n" +str(numeric_day) # e.g. 'Wednesday'\nNumber
            
        elif key != "header" and isinstance(comp_val, str):
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse_text"][0]), 
            panel.get_clutter_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse_text"][1])]

            


        iteration = iteration + 1

    return widget_dict




text_x_header = [1, 7]
# print('panel itself: ', widget_regions[day_widget["info"]["widget_index"]])

i = 0
print('text position: ', i)

day_widget = segment_roi(panel_layout, widget_regions, day_widget, [i, 3])
print('DAY roi: ', panel_layout.panel_separator(widget_regions[day_widget["info"]["widget_index"]], 2, "vertical"))
print('\n\nheader position\n',json.dumps(day_widget["txt_component_positions"], indent=2))
print('\n\ncomponent regions\n',json.dumps(day_widget["component_regions"], indent=2))


garage_widget = segment_roi(panel_layout, widget_regions, garage_widget, [i, 3])
print('GARAGE roi: ', panel_layout.panel_separator(widget_regions[garage_widget["info"]["widget_index"]], 2, "vertical"))
print('\n\nheader position\n',json.dumps(garage_widget["txt_component_positions"], indent=2))
print('\n\ncomponent regions\n',json.dumps(garage_widget["component_regions"], indent=2))

header_wrap_width = 500