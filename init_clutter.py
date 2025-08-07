clutter_icon_index_v = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [3, 0], [4, 0]]

dynamic_clutter_icons = [["duration", "fuel", "distance"], 
                          ["calendar"], 
                          ["garage"],
                          ["temperature"],
                          ["battery"]]
                          
                          
clutter_change_order_indices = getClutterOrderCounterbalanceGroup(cb_group = expInfo["clutter_cb"])
clutter_changed_icon_indices = getRandomChangingIconIndex(clutter_icon_index_v, 12)

clutter_changed_icon_indices_practice = getRandomChangingIconIndex(clutter_icon_index_v, 10)



