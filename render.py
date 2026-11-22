import bpy
from mathutils import Vector
import os
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=os.path.abspath("cena-espelhos.glb"))
scene = bpy.context.scene
points = [o.matrix_world @ Vector(p) for o in scene.objects if o.type == 'MESH' for p in o.bound_box]
center = sum(points, Vector()) / len(points)
radius = max((p-center).length for p in points)
camera = next((o for o in scene.objects if o.type == 'CAMERA'), None)
if camera is None:
    bpy.ops.object.camera_add(location=center + Vector((1,-2,1))*radius)
    camera = bpy.context.object
    camera.rotation_euler = (center-camera.location).to_track_quat('-Z','Y').to_euler()
scene.camera = camera
scene.world = bpy.data.worlds.new("Ambiente")
scene.world.use_nodes = True
scene.world.node_tree.nodes["Background"].inputs[0].default_value = (.8,.85,.9,1)
bpy.ops.object.light_add(type='AREA', location=center+Vector((1,-1,2))*radius)
light = bpy.context.object
light.rotation_euler = (center-light.location).to_track_quat('-Z','Y').to_euler()
light.data.energy = 150*radius**2
light.data.size = radius
scene.render.engine = 'CYCLES'
scene.cycles.samples = 32
scene.render.resolution_x = 1280
scene.render.resolution_y = 960
scene.render.resolution_percentage = 100
scene.render.filepath = os.path.abspath("resultado.png")
bpy.ops.render.render(write_still=True)
