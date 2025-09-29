# Example usage:
class Panel:
    def __init__(self, x, y, scale_ratiosV = [1, 2/3], scale_empty_partV = ["", "bottom"]):
        self.x = x
        self.y = y
        self.column_spacing = 0.03
        self.row_spacing = 0.03
        self.scale_ratios = scale_ratiosV
        self.scale_empty_part = scale_empty_partV
        self.panel_x_size = round(x * self.scale_ratios[0])
        self.panel_y_size = round(y * self.scale_ratios[1])
        self.panel_position = self.estimate_panel_position()

    def estimate_panel_position(self):

        if self.scale_empty_part[0] == "left":
            x_axis_shift = 1
        elif self.scale_empty_part[0] == "right":
            x_axis_shift = -1
        else:
            x_axis_shift = 0

        if self.scale_empty_part[1] == "top":
            y_axis_shift = -1
        elif self.scale_empty_part[1] == "bottom":
            y_axis_shift = 1
        else:
            y_axis_shift = 0            

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

        window_origin_x = self.panel_position[0] - self.panel_x_size / 2
        window_origin_y = self.panel_position[1] + self.panel_y_size / 2  

        if self.scale_empty_part[1] == "top":
            window_origin_y = window_origin_y - self.panel_y_size / 2        
        
        if self.scale_empty_part[0] == "left":
            window_origin_x = window_origin_x - self.panel_x_size / 2   
        elif self.scale_empty_part[0] == "right":
            window_origin_x = window_origin_x - self.panel_x_size / 2   

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

    