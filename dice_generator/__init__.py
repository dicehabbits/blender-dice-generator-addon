

bl_info = {
    "name": "Dice Generator",
    "description": "Generates different game dice and allows numbers to be stamped on faces",
    "author": "userKosho, dicehabbits",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "View3d &gt; UI &gt; Dice (side tabs below View tab",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/dicehabbits/blender-dice-generator-addon",
    "tracker_url": "https://github.com/dicehabbits/blender-dice-generator-addon/issues",
    "category": "Add Mesh"
    }

import bpy


if "bpy" in locals():
    import importlib
    if "dice_panel" in locals():
        importlib.reload(dice_panel)

from . import dice_panel

def register():
    dice_panel.register()

def unregister():
    dice_panel.unregister()