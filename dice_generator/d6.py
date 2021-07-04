import bpy
from math import radians
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2



class D6():
    
    def __init__(self):
        self.dice = None
        self.face_objects = {}
    
    def create_d6(self):
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.active_object.name = 'd6'


        bpy.context.active_object.dimensions = [16,16,16]
        
        
        self.dice = bpy.context.active_object
        return bpy.context.active_object
    
    def rotate_to_stamp_same_number(self):
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[Y_AXIS] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        
    def rotate_to_stamp_same_number_odd(self):
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[Y_AXIS] = radians(90)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    
    def stamp(self):
        self.stamp_number("6")
        self.rotate_to_stamp_same_number()
        self.stamp_number("2")
        self.rotate_to_stamp_same_number()
        self.stamp_number("4")

        bpy.context.active_object.rotation_euler[X_AXIS] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        self.stamp_number("3")
        self.rotate_to_stamp_same_number_odd()
        self.stamp_number("1")
        self.rotate_to_stamp_same_number_odd()
        bpy.ops.object.modifier_apply(modifier="Boolean")
        self.stamp_number("5")
        self.rotate_to_stamp_same_number()
    
    def stamp_number(self, stamp_number):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = self.face_objects[f'number{stamp_number}']
        bpy.ops.object.modifier_apply(modifier="Boolean")