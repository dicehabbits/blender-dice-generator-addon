import bpy
from math import radians
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

class D8():
    
    def __init__(self):
        self.dice = None
        self.face_objects = {}
    
    def create_d8(self):
        bpy.ops.mesh.primitive_solid_add(source='8', size=1)
        bpy.context.active_object.name = 'd8'

        bpy.context.active_object.rotation_euler[Y_AXIS] = radians(45)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.active_object.dimensions[2] = 16.4
        bpy.context.active_object.scale[0] =  bpy.context.active_object.scale[2]
        bpy.context.active_object.scale[1] =  bpy.context.active_object.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        
        self.dice = bpy.context.active_object
        return bpy.context.active_object
    
    def rotate_to_stamp_same_number(self):
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[Y_AXIS] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(35.265)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        

    
    def stamp(self):
        self.stamp_number("8")
        self.rotate_to_stamp_same_number()
        self.stamp_number("2")
        self.rotate_to_stamp_same_number()
        self.stamp_number("6")
        self.rotate_to_stamp_same_number()
        self.stamp_number("4")

        bpy.context.active_object.rotation_euler[X_AXIS] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        self.stamp_number("5")
        rotate_to_stamp_same_number()
        self.stamp_number("3")
        self.rotate_to_stamp_same_number()
        self.stamp_number("7")
        self.rotate_to_stamp_same_number()
        self.stamp_number("1")
    
    def stamp_number(self, stamp_number):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = self.face_objects[f'number{stamp_number}']
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")