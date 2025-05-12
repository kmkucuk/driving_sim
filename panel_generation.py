
# Samsung G9 Odyssey
# 5120 
# 1440
# 123.8 cm / 49 inç
win = {"size": [5120 , 1440]}

# Panel dimensions
panel_width = win['size'][0] * 0.6
panel_height = win['size'][1]

# Spacing ratios
col_spacing_ratio = 0.03  # 3% of panel width
row_spacing_ratio = 0.05  # 5% of screen height

# Number of spacing sections
num_col_spacings = 6  # 5 between + 2 sides
num_row_spacings = 3  # 1 between + 2 sides

# Actual spacing in pixels
col_spacing = panel_width * col_spacing_ratio
row_spacing = win['size'][1] * row_spacing_ratio

# Region dimensions
region_width = (panel_width - (col_spacing * num_col_spacings)) / 5
region_height = (win['size'][1] - (row_spacing * num_row_spacings)) / 2

# Panel's top-left corner (centered horizontally)
panel_origin_x = (win['size'][0] - panel_width) / 2
panel_origin_y = 0  # top-aligned

# Store region data as (x, y, width, height)
regions = []

for row in range(2):
    for col in range(5):
        x = panel_origin_x + col_spacing * (col + 1) + region_width * col
        y = row_spacing * (row + 1) + region_height * row
        regions.append({
            "x": int(x),
            "y": int(y),
            "width": int(region_width),
            "height": int(region_height)
        })

# Display the results
for i, r in enumerate(regions):
    print(f"Region {i+1}: x={r['x']}, y={r['y']}, width={r['width']}, height={r['height']}")
