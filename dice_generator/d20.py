import bpy
from math import radians
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

    
class D20():
    
    def __init__(self):
        self.dice = None
        self.face_objects = {}
    
    def create_d20(self):
        bpy.ops.mesh.primitive_solid_add(source='20')

        bpy.context.active_object.name = 'd20'


        bpy.context.active_object.rotation_euler[X_AXIS] = radians(20.905)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.active_object.dimensions[2] = 20.7
        bpy.context.active_object.scale[0] =  bpy.context.active_object.scale[2]
        bpy.context.active_object.scale[1] =  bpy.context.active_object.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        return bpy.context.active_object
    
#    def rotate_to_stamp_same_number(self):
#        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
#        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(72)
#        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
#        bpy.context.active_object.rotation_euler[X_AXIS] = radians(63.43)
#        
#    def rotate_to_stamp_pivote(self):
#        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(36)
#        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
#        bpy.context.active_object.rotation_euler[X_AXIS] = radians(63.43)

    
    def stamp(self):
        self.stamp_number("20")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp_number("14")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("6")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("4")

        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        # back to 20 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)



        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        #bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        #bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        self.stamp_number("8")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("10")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("16")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        # back to 20 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)



        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp_number("2")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("18")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("12")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        # back to 20 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        self.stamp_number("1")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp_number("19")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("9")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("3")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        # back to 1 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)



        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp_number("13")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("5")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("11")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        # back to 1 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)



        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        self.stamp_number("7")
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("17")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(-120)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(41.81)
        self.stamp_number("15")
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(0)
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-41.81)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        # back to 1 now
        bpy.context.active_object.rotation_euler[Z_AXIS] = radians(60)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    
    def stamp_number(self, stamp_number):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = self.face_objects[f'number{stamp_number}']
        bpy.ops.object.modifier_apply(modifier="Boolean")