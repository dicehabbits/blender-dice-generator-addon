import bpy
from math import radians
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

    
class D10():
    
    def __init__(self):
        self.dice = None
        self.face_objects = {}
    
    def create_d10(self):
        bpy.ops.mesh.primitive_cone_add(radius1=2, radius2=0, vertices=5, depth=2.25, enter_editmode=False)
        obj1 = bpy.context.active_object.name
        bpy.ops.mesh.primitive_cone_add(radius1=2, radius2=0, vertices=5, depth=2.25, enter_editmode=False, rotation=(radians(180), 0, 0))
        bpy.context.active_object.name = 'd10'
        obj2 = bpy.context.active_object.name
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.ops.object.modifier_add(type='BOOLEAN')

        bpy.context.object.modifiers["Boolean"].object = bpy.context.scene.objects[obj1]
        bpy.context.object.modifiers["Boolean"].operation = 'INTERSECT'
        bpy.ops.object.modifier_apply(modifier="Boolean")
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[obj1].select_set(True)
        bpy.ops.object.delete()

        bpy.data.objects[obj2].select_set(True)
        
        
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-54.3)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

        bpy.context.active_object.dimensions[2] = 17
        bpy.context.active_object.scale[0] =  bpy.context.active_object.scale[2]
        bpy.context.active_object.scale[1] =  bpy.context.active_object.scale[2]
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        
        return bpy.context.active_object
    
    def rotate_to_stamp_same_number(self):
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(-35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[Y_AXIS] = radians(-72)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.active_object.rotation_euler[X_AXIS] = radians(35.7)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        

    
    def stamp(self):
        self.stamp_number("6")
        self.rotate_to_stamp_same_number()
        self.stamp_number("4")
        self.rotate_to_stamp_same_number()
        self.stamp_number("8")
        self.rotate_to_stamp_same_number()
        self.stamp_number("2")
        self.rotate_to_stamp_same_number()
        self.stamp_number("0")


        bpy.context.active_object.rotation_euler[X_AXIS] = radians(180)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


        self.stamp_number("1")
        self.rotate_to_stamp_same_number()
        self.stamp_number("9")
        self.rotate_to_stamp_same_number()
        self.stamp_number("3")
        self.rotate_to_stamp_same_number()
        self.stamp_number("7")
        self.rotate_to_stamp_same_number()
        self.stamp_number("5")
        self.rotate_to_stamp_same_number()
    
    def stamp_number(self, stamp_number):
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = self.face_objects[f'number{stamp_number}']
        bpy.ops.object.modifier_apply(modifier="Boolean")