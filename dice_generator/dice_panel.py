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
# import sys
# import os

# # we get blend file path
# filepath = bpy.data.filepath

# ## we get the directory relative to the blend file path
# dir = os.path.dirname(filepath)

# ## we append our path to blender modules path
# ## we use if not statement to do this one time only
# if not dir in sys.path:
#    sys.path.append(dir )

# from d4 import D4
# from d6 import D6
# from d8 import D8
# from d10 import D10
# from d12 import D12
# from d20 import D20
# from d100 import D100

from . import (
    d4,
    d6,
    d8,
    d10,
    d12,
    d20,
    d100
)

#import imp
#import D4
#import D6
#imp.reload(D4)
#imp.reload(D6)

dice_d4 = d4.D4()
dice_d6 = d6.D6()
dice_d8 = d8.D8()
dice_d10 = d10.D10()
dice_d12 = d12.D12()
dice_d20 = d20.D20()
dice_d100 = d100.D100()

class Data_Holder():
    def __init__(self):
        self.current_dice = None

data_holder = Data_Holder()

def update_enum(self, context):
    if self.dice == "d4":
        bpy.context.scene.active_dice = dice_d4.dice
        for x in range(1,5):
            if f'number{str(x)}' in dice_d4.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d4.face_objects[f'number{str(x)}'])
    elif self.dice == "d6":
        bpy.context.scene.active_dice = dice_d6.dice
        for x in range(1,7):
            if f'number{str(x)}' in dice_d6.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d6.face_objects[f'number{str(x)}'])
    elif self.dice == "d8":
        bpy.context.scene.active_dice = dice_d8.dice
        for x in range(1,9):
            if f'number{str(x)}' in dice_d8.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d8.face_objects[f'number{str(x)}'])
    elif self.dice == "d10":
        bpy.context.scene.active_dice = dice_d10.dice
        for x in range(0,10):
            if f'number{str(x)}' in dice_d10.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d10.face_objects[f'number{str(x)}'])
    elif self.dice == "d12":
        bpy.context.scene.active_dice = dice_d12.dice
        for x in range(1,13):
            if f'number{str(x)}' in dice_d12.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d12.face_objects[f'number{str(x)}'])
    elif self.dice == "d20":
        bpy.context.scene.active_dice = dice_d20.dice
        for x in range(1,21):
            if f'number{str(x)}' in dice_d20.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}', dice_d20.face_objects[f'number{str(x)}'])
    elif self.dice == "d100":
        bpy.context.scene.active_dice = dice_d100.dice
        for x in range(0,10):
            if f'number{str(x)}0' in dice_d100.face_objects:
                setattr(bpy.context.scene, f'number{str(x)}0', dice_d100.face_objects[f'number{str(x)}0'])
    # self = current scene in an EnumProperty callback!
    data_holder.current_dice = self.dice
    print(self.dice)



class CreateDiceButtonOperator(bpy.types.Operator):
    bl_idname = "scene.create_dice_button_operator"
    bl_label = "Create Dice"

    def execute(self, context):
        scene = context.scene
        if scene.dice == "d4":
            bpy.context.scene.active_dice = dice_d4.create_d4()
        elif scene.dice == "d6":
            bpy.context.scene.active_dice = dice_d6.create_d6()
        elif scene.dice == "d8":
            bpy.context.scene.active_dice = dice_d8.create_d8()
        elif scene.dice == "d10":
            bpy.context.scene.active_dice = dice_d10.create_d10()
        elif scene.dice == "d12":
            bpy.context.scene.active_dice = dice_d12.create_d12()
        elif scene.dice == "d20":
            bpy.context.scene.active_dice = dice_d20.create_d20()
        elif scene.dice == "d100":
            bpy.context.scene.active_dice = dice_d100.create_d100()
        return {'FINISHED'}
    
class StampDiceButtonOperator(bpy.types.Operator):
    bl_idname = "scene.stamp_dice_button_operator"
    bl_label = "Stamp Dice"
    
    

    def execute(self, context):
        scene = context.scene
        context.view_layer.objects.active = bpy.context.scene.active_dice
        context.view_layer.objects.active.select_set(state=True)
        if scene.dice == "d4":
            for x in range(1, 5):
                key = f'number{x}'
                if key in dice_d4.face_objects and dice_d4.face_objects[key] is not None:
                    print(dice_d4.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d4.stamp()
        elif scene.dice == "d6":
            for x in range(1, 7):
                key = f'number{x}'
                if key in dice_d6.face_objects and dice_d6.face_objects[key] is not None:
                    print(dice_d6.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d6.stamp()
        elif scene.dice == "d8":
            for x in range(1, 9):
                key = f'number{x}'
                if key in dice_d8.face_objects and dice_d8.face_objects[key] is not None:
                    print(dice_d8.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d8.stamp()
        elif scene.dice == "d10":
            for x in range(0, 10):
                key = f'number{x}'
                if key in dice_d10.face_objects and dice_d10.face_objects[key] is not None:
                    print(dice_d10.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d10.stamp()
        elif scene.dice == "d12":
            for x in range(1, 13):
                key = f'number{x}'
                if key in dice_d12.face_objects and dice_d12.face_objects[key] is not None:
                    print(dice_d12.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d12.stamp()
        elif scene.dice == "d20":
            for x in range(1, 21):
                key = f'number{x}'
                if key in dice_d20.face_objects and dice_d20.face_objects[key] is not None:
                    print(dice_d20.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d20.stamp()
        elif scene.dice == "d100":
            for x in range(0, 9):
                key = f'number{x}0'
                if key in dice_d100.face_objects and dice_d100.face_objects[key] is not None:
                    print(dice_d100.face_objects[key].name)
                    continue
                else:
                    print(key)
                    print("not valid face object numbers detected")
                    return {'FINISHED'}
                
            dice_d100.stamp()
        
        return {'FINISHED'}     


class ApplyCollectionOfFacesButtonOperator(bpy.types.Operator):
    bl_idname = "scene.apply_collection_of_faces_button_operator"
    bl_label = "Use collection to fill faces"

    def execute(self, context):
        pass

# https://blender.stackexchange.com/questions/75185/limit-prop-search-to-specific-types-of-objects
class OBJECT_PT_TextTool(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "OBJECT_PT_TextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'dice'
    
    dice : bpy.props.EnumProperty(
            name = "My enum2",
            description = "My enum description",
            items = [
                ("d4", "D4 (Tetrahedron)", "Create a d4"),
                ("d6", "D6 (Cube)", "Create a Sphere"),
                ("d8", "D8 (Octahedron)", "Create a Sphere"), 
                ("d10", "D10 (Pentagonal trapezohedron)", "Create a Sphere"),
                ("d12", "D12 (Dodecahedron)", "Create a Sphere"),
                ("d20", "D20 (Icosahedron)", "Create a Sphere"),
                ("d100", "D100 (Pentagonal trapezohedron)", "Create a Sphere")           
            ],
            update=update_enum
        )
    
    
    
    

    def draw(self, context):
        layout = self.layout
        row = layout.row()


        scene = context.scene

        layout.prop(scene, "dice")
        layout.prop(scene, "active_dice")
        col = layout.column()
        row.operator("scene.create_dice_button_operator")
        row.operator("scene.stamp_dice_button_operator")
        if scene.dice == "d4":
            for x in range(1,5):
                layout.prop(scene, "number"+ str(x))

        elif scene.dice == "d6":
            for x in range(1,7):
                layout.prop(scene, "number"+ str(x))
        elif scene.dice == "d8":
            for x in range(1,9):
                layout.prop(scene, "number"+ str(x))
        elif scene.dice == "d10":
            for x in range(0,10):
                layout.prop(scene, "number"+ str(x))
        elif scene.dice == "d12":
            for x in range(1,13):
                layout.prop(scene, "number"+ str(x))
        elif scene.dice == "d20":
            for x in range(1,21):
                layout.prop(scene, "number"+ str(x))
        elif scene.dice == "d100":
            for x in range(0,10):
                layout.prop(scene, "number"+ str(x) + "0")
        #TODO eventually collection support
#        layout.prop(scene, "collection_faces")
        

def scene_mychosenobject_poll(self, object):
    return object.type == 'MESH'

def current_dice_object(self, context):
    if self.dice == "d4":
        dice_d4.dice = bpy.context.scene.active_dice
    elif self.dice == "d6":
        dice_d6.dice = bpy.context.scene.active_dice
    elif self.dice == "d8":
        dice_d8.dice = bpy.context.scene.active_dice
    elif self.dice == "d10":
        dice_d10.dice = bpy.context.scene.active_dice
    elif self.dice == "d12":
        dice_d12.dice = bpy.context.scene.active_dice
    elif self.dice == "d20":
        dice_d20.dice = bpy.context.scene.active_dice
    elif self.dice == "d100":
        dice_d100.dice = bpy.context.scene.active_dice
     
def create_selected_dice_box(selected_item=None):
    if selected_item:
        bpy.types.Scene.active_dice = bpy.props.PointerProperty(
            item=selected_item,
            name="Dice Object",
            type=bpy.types.Object,
            poll=scene_mychosenobject_poll
        )
        
    else:
        bpy.types.Scene.active_dice = bpy.props.PointerProperty(
            name="Dice Object",
            type=bpy.types.Object,
            poll=scene_mychosenobject_poll,
            update=current_dice_object
        )
        
def collection_face_selection_box():
    bpy.types.Scene.collection_faces = bpy.props.PointerProperty(
            name="Face Collection",
            type=bpy.types.Object
        )

def register():
    bpy.utils.register_class(OBJECT_PT_TextTool)
    bpy.utils.register_class(CreateDiceButtonOperator)
    bpy.utils.register_class(StampDiceButtonOperator)
    bpy.utils.register_class(ApplyCollectionOfFacesButtonOperator)
#    bpy.utils.register_class(MESH_OT_dropdownexample)

    create_selected_dice_box()
    
    collection_face_selection_box()
    
    reg_dice_select()
    
    bpy.types.Scene.dice = bpy.props.EnumProperty(
            name = "My enum",
            description = "My enum description",
            items = [
                ("d4", "D4 (Tetrahedron)", "Create a d4"),
                ("d6", "D6 (Cube)", "Create a Sphere"),
                ("d8", "D8 (Octahedron)", "Create a Sphere"), 
                ("d10", "D10 (Pentagonal trapezohedron)", "Create a Sphere"),
                ("d12", "D12 (Dodecahedron)", "Create a Sphere"),
                ("d20", "D20 (Icosahedron)", "Create a Sphere"),
                ("d100", "D100 (Pentagonal trapezohedron)", "Create a Sphere")           
            ],
            update=update_enum
            
        )


def closure(prop):
    return lambda a,b: update_face(a,b,prop)

def update_face(self, context, origin=""):
    if self.dice == "d4":
        dice_d4.face_objects[origin] = getattr(bpy.context.scene, origin)
    elif self.dice == "d6":
        dice_d6.face_objects[origin] = getattr(bpy.context.scene, origin)        
    elif self.dice == "d8":
        dice_d8.face_objects[origin] = getattr(bpy.context.scene, origin)   
    elif self.dice == "d10":
        dice_d10.face_objects[origin] = getattr(bpy.context.scene, origin)   
    elif self.dice == "d12":
        dice_d12.face_objects[origin] = getattr(bpy.context.scene, origin)   
    elif self.dice == "d20":
        dice_d20.face_objects[origin] = getattr(bpy.context.scene, origin)   
    elif self.dice == "d100":
        dice_d100.face_objects[origin] = getattr(bpy.context.scene, origin)   
    
    
class SceneDiceFace(bpy.types.PropertyGroup):
    face : bpy.props.PointerProperty(
        name="face",
        type=bpy.types.Object,
        poll=scene_mychosenobject_poll
    )
    
    def add(self, face):
        self.face = face
        return self.face
    
    
def reg_dice_select():
    bpy.types.Scene.number00 = bpy.props.PointerProperty(
        name="face 00",
        type=bpy.types.Object,
        poll=scene_mychosenobject_poll
    )
    
    bpy.utils.register_class(SceneDiceFace)
    
    bpy.types.Scene.faces_v2 = bpy.props.CollectionProperty(type=SceneDiceFace)
    
#    test_value = bpy.props.PointerProperty(
#        name="face 200",
#        type=bpy.types.Object,
#        poll=scene_mychosenobject_poll
#    )
#    temp = bpy.props.PointerProperty(
#        name="face 200",
#        type=bpy.types.Object
#    )
#    bpy.context.scene.faces_v2.clear()
#    bpy.context.scene.faces_v2.add().add(bpy.props.PointerProperty(
#        name="face 200",
#        type=bpy.types.Object,
#        poll=scene_mychosenobject_poll
#    ))
    
#    bpy.types.Scene.numbered_faces = []
    for x in range(0, 21):
        setattr(bpy.types.Scene, f'number{str(x)}', bpy.props.PointerProperty(
                name="face " + str(x),
                type=bpy.types.Object,
                poll=scene_mychosenobject_poll,
                update=closure(f'number{str(x)}')
        ))
    for x in range(0, 10):
        if x == 1 or x == 2:
            continue
        setattr(bpy.types.Scene, f'number{str(x)}0', bpy.props.PointerProperty(
                name=f'face {str(x)}0',
                type=bpy.types.Object,
                poll=scene_mychosenobject_poll,
                update=closure(f'number{str(x)}0')
        ))
    
    


def unregister():
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
    bpy.utils.unregister_class(CreateDiceButtonOperator)
    bpy.utils.unregister_class(StampDiceButtonOperator)
    bpy.utils.unregister_class(ApplyCollectionOfFacesButtonOperator)
    
    
    
    
    bpy.utils.register_class(SceneDiceFace)
    del(bpy.types.Scene.faces)
    
#    bpy.utils.unregister_class(MESH_OT_dropdownexample)
    del bpy.types.Scene.active_dice

    del bpy.types.Scene.number00
    del bpy.types.Scene.number0
    del bpy.types.Scene.number1
    del bpy.types.Scene.number2
    del bpy.types.Scene.number3
    del bpy.types.Scene.number4
    del bpy.types.Scene.number5
    del bpy.types.Scene.number6
    del bpy.types.Scene.number7
    del bpy.types.Scene.number8
    del bpy.types.Scene.number9
    del bpy.types.Scene.number10
    del bpy.types.Scene.number11
    del bpy.types.Scene.number12
    del bpy.types.Scene.number13
    del bpy.types.Scene.number14
    del bpy.types.Scene.number15
    del bpy.types.Scene.number16
    del bpy.types.Scene.number17
    del bpy.types.Scene.number18
    del bpy.types.Scene.number19
    del bpy.types.Scene.number20
    del bpy.types.Scene.number30
    del bpy.types.Scene.number40
    del bpy.types.Scene.number50
    del bpy.types.Scene.number60
    del bpy.types.Scene.number70
    del bpy.types.Scene.number80
    del bpy.types.Scene.number90
    
#    del bpy.types.Scene.mychosenObjectDrop
    del bpy.types.Scene.my_enum


if __name__ == "__main__":
    register()
