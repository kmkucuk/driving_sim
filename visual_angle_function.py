from fontTools.ttLib import TTFont

inch_vert_monitor_lab = 11.6875
cm_vert_monitor_lab = 29.21
cm_vert_monitor_mert = 33.5
monitor_res_lab = [1920, 1080]

pix_per_cm_lab = monitor_res_lab[1] / cm_vert_monitor_lab

pix_per_cm_mert = monitor_res_lab[1] / cm_vert_monitor_mert

distance_cm = 76.2

# pix_per_cm_lab = 36.381
# pix_per_cm_mert = 32.381
char_size_arc_min = 19.6
char_size_degree = 0.327

stim_cm = 0.4349
stim_pix = pix_per_cm_lab * stim_cm

print(pix_per_cm_lab)
print(pix_per_cm_mert)
print(stim_pix)

pix_for_required_inch = 31.21152

# get pixel size to x-height ratio.
# then use this ratio to multiply letter height in Psychopy. 
# then you get the desired x-height in real units (cm or inches). 
neueFont = TTFont('georgia.ttf')
x_height =((neueFont['glyf']['x'].yMax - neueFont['glyf']['x'].yMin )/ neueFont['head'].unitsPerEm ) * stim_pix
print(stim_pix / x_height)

neueFont = TTFont('robotoflex.ttf')
x_height =((neueFont['glyf']['x'].yMax - neueFont['glyf']['x'].yMin )/ neueFont['head'].unitsPerEm ) * stim_pix
print(stim_pix / x_height)

neueFont = TTFont('neuefrutigerworld.ttf')
x_height =((neueFont['glyf']['x'].yMax - neueFont['glyf']['x'].yMin )/ neueFont['head'].unitsPerEm ) * stim_pix
print(stim_pix / x_height)


a=0