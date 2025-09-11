
all_widgets = [
                {"name": "trip_widget",
                "possible_regions": large_region_indices, 
                "region_index": 0,
                "text_components": 
                    {"trip_header": {"text": "Current Trip", "position_percentage": [15, 10], "position_pixel": []},
                    "duration": {"text": "", "position_percentage": [35, 25], "position_pixel": []},  
                    "fuel": {"text": "", "position_percentage": [35, 50], "position_pixel": []}, 
                    "distance": {"text": "", "position_percentage": [35, 75], "position_pixel": []}
                    },
                 "image_components": 
                 {"duration": {"file":  getImageWithKeyword("./stimuli/clutter", "duration_1"), 
                               "position_percentage": [20, 25], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}, 
                  "fuel": {"file":  getImageWithKeyword("./stimuli/clutter", "fuel_1"), 
                           "position_percentage": [20, 50], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}, 
                  "distance": {"file":  getImageWithKeyword("./stimuli/clutter", "distance_1"), 
                               "position_percentage": [20, 75], "position_pixel": [],
                               "size_ratio": [0.3125, 0.3125], "size_pixel": []}
                  },
                },

                {"name": "calendar_widget",
                 "possible_regions": large_region_indices,
                 "region_index": 5,
                 "text_components": 
                    {"date": {"text": "", "position_percentage": [20, 15], "position_pixel": []}
                     },
                 "image_components": 
                 {"calendar": {"file":  getImageWithKeyword("./stimuli/clutter", "calendar_1"), 
                               "position_percentage": [50 , 70], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                },
                
                {"name": "garage_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 1, 
                 "text_components": 
                    {"garage_header": {"text": "My Home", "position_percentage": [15, 20], "position_pixel": []},
                     "garage_door": {"text": "", "position_percentage": [35, 50], "position_pixel": []}
                     },
                 "image_components": 
                 {"garage": {"file":  getImageWithKeyword("./stimuli/clutter", "garage_1"), 
                             "position_percentage": [20, 50], "position_pixel": [],
                               "size_ratio": [0.35, 0.35], "size_pixel": []}
                  },
                },

                {"name": "temperature_widget",
                "possible_regions": small_region_indices, 
                 "region_index": 3, 
                 "text_components": 
                    {"temperature": {"text": "", "position_percentage": [30, 40], "position_pixel": []}                   
                     },
                 "image_components": 
                 {"temperature": {"file":  getImageWithKeyword("./stimuli/clutter", "temperature_1"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                },

                {"name": "battery_widget",
                 "possible_regions": small_region_indices, 
                 "region_index": 4, 
                 "text_components": 
                    {"battery": {"text": "", "position_percentage": [21, 45], "position_pixel": []},
                     "miles": {"text": "", "position_percentage": [55, 63], "position_pixel": []}
                     },
                 "image_components": 
                 {"battery": {"file":  getImageWithKeyword("./stimuli/clutter", "battery_1"), 
                                  "position_percentage": [50, 50], "position_pixel": [],
                               "size_ratio": [0.8, 0.8], "size_pixel": []}
                  },
                }
        ] 