import calendar
import json
import math
import random
from datetime import date
from datetime import datetime
import os


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
                    "duration": {"text": "", "position_percentage": [12, 25], "position_pixel": []},  
                    "fuel": {"text": "", "position_percentage": [12, 50], "position_pixel": []}, 
                    "distance": {"text": "", "position_percentage": [12, 75], "position_pixel": []}
                    },
                 "image_components": 
                 {"duration": {"file":  getImageWithKeyword("./stimuli/clutter", "duration"), "position_percentage": [10, 25], "position_pixel": []}, 
                  "fuel": {"file":  getImageWithKeyword("./stimuli/clutter", "fuel"), "position_percentage": [10, 50], "position_pixel": []}, 
                  "distance": {"file":  getImageWithKeyword("./stimuli/clutter", "distance"), "position_percentage": [10, 75], "position_pixel": []}
                  },
                },

                {"name": "calendar_widget",
                 "possible_regions": large_region_indices,
                 "region_index": 5,
                 "text_components": 
                    {"date": {"text": "", "position_percentage": [15, 15], "position_pixel": []}
                     },
                 "image_components": 
                 {"calendar": {"file":  getImageWithKeyword("./stimuli/clutter", "calendar"), "position_percentage": [10 , 60], "position_pixel": []}
                  },
                },
                
                {"name": "garage_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 1, 
                 "text_components": 
                    {"garage_header": {"text": "My Home", "position_percentage": [10, 10], "position_pixel": []},
                     "garage_door": {"text": "", "position_percentage": [15, 50], "position_pixel": []}
                     },
                 "image_components": 
                 {"garage": {"file":  getImageWithKeyword("./stimuli/clutter", "garage"), "position_percentage": [10, 50], "position_pixel": []}
                  },
                },

                {"name": "temperature_widget",
                "possible_regions": small_region_indices, 
                 "region_index": 3, 
                 "text_components": 
                    {"temperature": {"text": "", "position_percentage": [40, 50], "position_pixel": []}                   
                     },
                 "image_components": 
                 {"temperature": {"file":  getImageWithKeyword("./stimuli/clutter", "garage"), "position_percentage": [50, 50], "position_pixel": []}
                  },
                },

                {"name": "battery_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 4, 
                 "text_components": 
                    {"battery": {"text": "", "position_percentage": [30, 30], "position_pixel": []},
                     "miles": {"text": "", "position_percentage": [60, 60], "position_pixel": []}
                     },
                 "image_components": 
                 {"temperature": {"file":  getImageWithKeyword("./stimuli/clutter", "garage"), "position_percentage": [50, 50], "position_pixel": []}
                  },
                }
        ] 

dynamic_clutter_values = [{"duration": 28, "fuel": 34, "distance": 78}, 
                          {"date": 0}, 
                          {"garage_door": 0},
                          {"temperature": 96},
                          {"battery": 24, "miles": 76}]

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



a=0

left_symbol_x = [2, 10]
symbol_y_parse = [0, 3]

centered_symbol_x = [1, 3]
centered_symbol_y = [1, 3]

# 
text_x_parse = [3, 10]
text_y_parse = [0, 3]


temp_text_x = [5, 20]
temp_text_y = [8, 20]

battery_text_x = [2, 20]
battery_text_y = [8, 20]

miles_text_x = [6, 20]
miles_text_y = [15, 20]

temperature_int = 96
battery_int = 24
miles_int = 78
temperature_text = ('').join([str(temperature_int), "F"])
battery_text = ('').join(["%", str(battery_int)])
miles_text = ('').join([str(miles_int), "mi"])

trip_widget = {"info": {"parse_symbol": [left_symbol_x, symbol_y_parse], "parse_text": [text_x_parse, text_y_parse], "widget_index": 0, "section_count": 4},                
               "components": {"header": "Current Trip",
                            "duration": "1 hr 53 min", 
                            "fuel": "34 mpg", 
                            "distance": "78 mi"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                            } # todo: add variable parameters to these text


garage_widget = {"info": {"parse_symbol": [left_symbol_x, symbol_y_parse], 
                          "parse_text": [text_x_parse, text_y_parse], 
                          "widget_index": 1, "section_count": 2}, 
                 "components": {"header": "My Home",
                                "garage": "Garage Door\nOpen"},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }


temperature_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [temp_text_x, temp_text_y], "widget_index": 3, "section_count": 1}, 
              "components": {"temperature": temperature_text},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
               }

battery_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [text_x_parse, text_y_parse], "widget_index": 4, "section_count": 1}, 
                 "components": {"battery": battery_text,
                                "miles": miles_text},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

day_widget = {"info": {"parse_symbol": [centered_symbol_x, centered_symbol_y], "parse_text": [text_x_parse, text_y_parse], "widget_index": 5, "section_count": 2}, 
                 "components": {"header": "day",
                                "calendar": None},
                "img_files": {},
                "sym_component_positions": {},
                "txt_component_positions": {}
                }

all_widgets = [trip_widget, garage_widget, temperature_widget, battery_widget, day_widget]

# first assume header to be the same size in terms of roi
# then we can adjust it to become something else (smaller then etc.)
def segment_roi(panel, roi, widget_dict):
    
    # garage widget (duration, fuel, distance)

    component_count = widget_dict["info"]["section_count"]
    component_regions = panel.panel_separator(roi[widget_dict["info"]["widget_index"]], component_count, "vertical")
    iteration = 0
    widget_dict["component_regions"] = component_regions
    # garage widget (duration, fuel, distance)

    for key, comp_val in widget_dict["components"].items():         
        placement_desc = None
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
                month_index = datetime.now().month
                month = calendar.month_name[month_index]
                text_x_header = [1, 10]
                text_y_header = [2, 7]
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
                
                date_text =  str_num_day + day_suffix + " " + month +"\n" + calendar.day_name[my_date.weekday()] # e.g. 'Wednesday'\nNumber         
                widget_dict["components"]["header"] =  str_num_day + day_suffix + " " + month +"\n" + calendar.day_name[my_date.weekday()] # e.g. 'Wednesday'\nNumber         
                
            # headers are more leftward than regular text, hence specific text parsing
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "horizontal", text_x_header), 
                                                           panel.get_clutter_coordinate(component_regions[iteration], 
                                                                                        "vertical", text_y_header)]
            
        elif key != "header" and isinstance(comp_val, str):
            placement_desc = 'bottom'
            if comp_val == "battery":
                text_x_parse = battery_text_x
                text_y_parse = battery_text_y
            elif comp_val == "miles":
                text_x_parse = miles_text_x
                text_y_parse = miles_text_y
            else:
                text_x_parse = widget_dict["info"]["parse_text"][0]
                text_y_parse = widget_dict["info"]["parse_text"][1]
            widget_dict["txt_component_positions"][key] = [panel.get_clutter_coordinate(component_regions[iteration], "horizontal", text_x_parse, placement_desc), 
            panel.get_clutter_coordinate(component_regions[iteration], "vertical", text_y_parse)]
        
        if component_count == len(widget_dict["components"].items()):
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

# letter size is dependent on the large panel's height
letter_size = temperature_widget["component_regions"][0]["height"] * 0.2
day_size = day_widget["component_regions"][0]["width"] * 0.125
header_size = trip_widget["component_regions"][0]["width"] * 0.1
temperature_size = temperature_widget["component_regions"][0]["width"] * 0.14
battery_size = battery_widget["component_regions"][0]["width"] * 0.12


header_wrap_width = 500