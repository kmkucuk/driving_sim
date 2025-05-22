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

left_symbol_x = [2, 10]
symbol_y_parse = [0, 3]

centered_symbol_x = [1, 3]
centered_symbol_y = [1, 3]



# trip widget (duration, fuel, distance)
text_x_parse = [3, 10]
text_y_parse = [0, 3]

trip_widget = {"info": {"parse_symbol": [left_symbol_x, symbol_y_parse], "parse_text": [text_x_parse, text_y_parse], "widget_index": 0},                
               "components": {"header": "Current Trip",
                            "duration": "1 hr 53 min", 
                            "fuel": "34 mpg", 
                            "distance": "78 mi"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                            } # todo: add variable parameters to these text


garage_widget = {"info": {"parse_symbol": [left_symbol_x, symbol_y_parse], "parse_text": [text_x_parse, text_y_parse], "widget_index": 1}, 
                 "components": {"header": "My Home",
                                "garage": "Garage Door\nOpen"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

temperature_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [text_x_parse, text_y_parse], "widget_index": 3}, 
              "components": {"temperature": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
               }

battery_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [text_x_parse, text_y_parse], "widget_index": 4}, 
                 "components": {"battery": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

day_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [text_x_parse, text_y_parse], "widget_index": 5}, 
                 "components": {"header": "day",
                                "calendar": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }


all_widgets = [trip_widget, garage_widget, temperature_widget, battery_widget, day_widget]

placement_desc = "mid"



# first assume header to be the same size in terms of roi
# then we can adjust it to become something else (smaller then etc.)
def segment_roi(panel, roi, widget_dict):
    
    # garage widget (duration, fuel, distance)

    component_count = len(widget_dict["components"].keys())
    component_regions = panel.panel_separator(roi[widget_dict["info"]["widget_index"]], component_count, "vertical")
    iteration = 0
    widget_dict["component_regions"] = component_regions
    # garage widget (duration, fuel, distance)

    for key, comp_val in widget_dict["components"].items():         

        if key != "header":
            # get symbol positions             
            widget_dict["sym_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse_symbol"][0]), 
            panel.get_clutter_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse_symbol"][1])]
            widget_dict["img_files"][key] = panel.getImageWithKeyword("./stimuli/clutter", key)
           
        if key == "header":
            text_x_header = [1, 10]
            text_y_header = [2, 7]     
            
            if comp_val == "day":
                # get current day for text display on calemdar widget
                my_date = date.today()
                today = datetime.now()
                text_x_header = [2, 10]
                text_y_header = [3, 7]
                numeric_day = today.day # this is a integer
                widget_dict["components"]["header"] = calendar.day_name[my_date.weekday()] +"\n" +str(numeric_day) # e.g. 'Wednesday'\nNumber         
            # headers are more leftward than regular text, hence specific text parsing
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "horizontal", text_x_header), 
                                                           panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "vertical", text_y_header)]
            
        elif key != "header" and isinstance(comp_val, str):
            placement_desc = 'bottom'
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], "horizontal", widget_dict["info"]["parse_text"][0], placement_desc), 
            panel.get_clutter_coordinate(component_regions[iteration], "vertical", widget_dict["info"]["parse_text"][1])]

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





garage_icon_size = [garage_widget["component_regions"][1]["width"] * 0.35, garage_widget["component_regions"][1]["width"] * 0.35]
onethird_icon_size = [trip_widget["component_regions"][0]["width"] * 0.3125, trip_widget["component_regions"][0]["width"] * 0.3125]
half_icon_size = [day_widget["component_regions"][1]["width"] * 0.8, day_widget["component_regions"][1]["width"] * 0.8]
full_icon_size = [temperature_widget["component_regions"][0]["width"] * 0.8, temperature_widget["component_regions"][0]["width"] * 0.8]


textFont = "./stimuli/font/robotoflex.ttf"

text_size = trip_widget["component_regions"][0]["width"]/12
# choose a targel panel (1 to 10)
# Panel Numbers: [1, [2/3], [4/5], 6]
target_panel = 3

# letter size is dependent on the large panel's height
letter_size = temperature_widget["component_regions"][0]["height"] * 0.2
day_size = day_widget["component_regions"][0]["width"] * 0.125
header_size = trip_widget["component_regions"][0]["width"] * 0.1



header_wrap_width = 500