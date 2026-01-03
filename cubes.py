import bpy  # type: ignore

cube0 = bpy.data.objects["Cube0"]
cube1 = bpy.data.objects["Cube1"]
cube2 = bpy.data.objects["Cube2"]

red = (1.0, 0.0, 0.0, 1.0)
green = (0.0, 1.0, 0.0, 1.0)
blue = (0.0, 0.0, 1.0, 1.0)

cube0.data.materials.append(bpy.data.materials.new(name="Red"))
material = cube0.data.materials[0]
material.use_nodes = True
nodes = material.node_tree.nodes
nodes.clear()
bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
bsdf.inputs["Base Color"].default_value = red
output = nodes.new(type="ShaderNodeOutputMaterial")
material.node_tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

cube1.data.materials.append(bpy.data.materials.new(name="Green"))
material = cube1.data.materials[0]
material.use_nodes = True
nodes = material.node_tree.nodes
nodes.clear()
bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
bsdf.inputs["Base Color"].default_value = green
output = nodes.new(type="ShaderNodeOutputMaterial")
material.node_tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

cube2.data.materials.append(bpy.data.materials.new(name="Blue"))
material = cube2.data.materials[0]
material.use_nodes = True
nodes = material.node_tree.nodes
nodes.clear()
bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
bsdf.inputs["Base Color"].default_value = blue
output = nodes.new(type="ShaderNodeOutputMaterial")
material.node_tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
