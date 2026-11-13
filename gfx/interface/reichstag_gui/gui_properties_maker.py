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
    print(f"""GER_{stateName}_party_popularity = {{
	image = "[ROOT.GER_reichstag_status_{stateName}]"
}}""")

