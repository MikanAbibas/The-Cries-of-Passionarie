# Save this as list_dirs_sorted.py

import os

def lineManip(nameLine):
    location=nameLine.index("_")
    stateName=nameLine[location+1:]
    return stateName

# Get a list of all items in the current directory
all_items = os.listdir('.')

# Use a list comprehension to filter for directories only
subdirectories = [item for item in all_items if os.path.isdir(item)]

# Sort the list of subdirectories alphabetically
subdirectories.sort() # or use: for dir_name in sorted(subdirectories):

# Loop through the sorted list and print each directory name
for dir_name in subdirectories:
    stateName=lineManip(dir_name)
    print(f"""iconType = {{
    name = "GER_{stateName}_party_popularity"
    position = {{ x=0 y=0 }}
    scale = 0.7
    orientation = center
    alwaystransparent = yes
}}""")
    print(f"""buttonType = {{
    name = "{stateName}_outline"
    spriteType = "GFX_{dir_name}"
    position = {{ x=0 y=0 }}
    pdx_tooltip = "TNO_world_hegemon_tt"
	scale = 0.7
	orientation = center
	clicksound = click_ok
	oversound = ui_menu_over
}}""")

