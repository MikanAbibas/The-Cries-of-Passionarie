# Save this as list_dirs_sorted.py

import os

# Get a list of all items in the current directory
all_items = os.listdir('.')

# Use a list comprehension to filter for directories only
subdirectories = [item for item in all_items if os.path.isdir(item)]

# Sort the list of subdirectories alphabetically
subdirectories.sort() # or use: for dir_name in sorted(subdirectories):

# Loop through the sorted list and print each directory name
for dir_name in subdirectories:
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_nsdap\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_nsdap.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_vup\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_vup.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_rsp\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_rsp.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_vaaf\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_vaaf.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_dap\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_dap.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_ler\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_ler.tga\"")
    print("}")
    print("spriteType = {")
    print("     name = \"GFX_"+dir_name+"_dg\"")
    print("     texturefile = \"gfx/interface/reichstag_gui/"+dir_name+"/"+dir_name+"_dg.tga\"")
    print("}")

