import bpy
from math import radians
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

    
class D12():
    
    def __init__(self):
        self.dice = None
        self.face_objects = {}
    
    def create_d12(self):
        bpy.ops.mesh.primitive_solid_add(source='12')

        bpy.context.active_object.name = 'd12'


        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-58.285)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.active_object.dimensions[2] = 18.5
        bpy.context.active_object.scale[0] =  bpy.context.active_object.scale[2]
        bpy.context.active_object.scale[1] =  bpy.context.active_object.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        return bpy.context.active_object
    
    def rotate_to_stamp_same_number(self):
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(63.43)
        
    def rotate_to_stamp_pivote(self):
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(36)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(63.43)    

    
    def stamp(self):
        stamp_number("12")
        self.rotate_to_stamp_pivote()


        self.stamp_number("8")
        self.rotate_to_stamp_same_number()
        self.stamp_number("6")
        self.rotate_to_stamp_same_number()
        self.stamp_number("4")
        self.rotate_to_stamp_same_number()
        self.stamp_number("2")
        self.rotate_to_stamp_same_number()
        self.stamp_number("10")

        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(36)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        self.stamp_number("1")
        self.rotate_to_stamp_pivote()


        self.stamp_number("3")
        self.rotate_to_stamp_same_number()
        self.stamp_number("11")
        self.rotate_to_stamp_same_number()
        self.stamp_number("9")
        self.rotate_to_stamp_same_number()
        self.stamp_number("7")
        self.rotate_to_stamp_same_number()
        self.stamp_number("5")
    
    def stamp_number(self, stamp_number):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = self.face_objects[f'number{stamp_number}']
        bpy.ops.object.modifier_apply(modifier="Boolean")