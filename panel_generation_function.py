import os

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


