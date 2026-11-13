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
    print(f"""GER_reichstag_status_{stateName} = {{
	name = GER_reichstag_status_{stateName}
	text = {{
		trigger = {{ GER_reichstag_nsdap_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_nsdap\"
	}}
	text = {{
		trigger = {{ GER_reichstag_vup_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_vup\"
	}}
	text = {{
		trigger = {{ GER_reichstag_rsp_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_rsp\"
	}}
	text = {{
		trigger = {{ GER_reichstag_vaaf_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_vaaf\"
	}}
	text = {{
		trigger = {{ GER_reichstag_dg_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_dg\"
	}}
	text = {{
		trigger = {{ GER_reichstag_dap_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_dap\"
	}}
	text = {{
		trigger = {{ GER_reichstag_ler_most_popular_state = yes }}
		localization_key = \"GFX_reichstag_{stateName}_ler\"
	}}
}}""")

