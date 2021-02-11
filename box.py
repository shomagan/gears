import bpy
import numpy


def face(a, b, c, d):
    vertices = numpy.array([
        a[0], a[1], a[2],
        b[0], b[1], b[2],
        c[0], c[1], c[2],
        d[0], d[1], d[2],
    ], dtype=numpy.float32)
    edges = numpy.array([
        0, 1,
        1, 2,
        2, 3,
        4, 0
    ], dtype=numpy.int32)
    num_vertices = vertices.shape[0] // 3
    num_edges = edges.shape[0] // 2
    vertex_index = numpy.array([0, 1, 2, 3], dtype=numpy.int32)
    loop_start = numpy.array([0], dtype=numpy.int32)
    loop_total = numpy.array([4], dtype=numpy.int32)
    num_vertex_indices = vertex_index.shape[0]
    num_loops = loop_start.shape[0]
    mesh = bpy.data.meshes.new(name='created mesh')
    mesh.vertices.add(num_vertices)
    mesh.vertices.foreach_set("co", vertices)
    mesh.edges.add(num_edges)
    mesh.edges.foreach_set("vertices", edges)
    mesh.loops.add(num_vertex_indices)
    mesh.loops.foreach_set("vertex_index", vertex_index)
    mesh.polygons.add(num_loops)
    mesh.polygons.foreach_set("loop_start", loop_start)
    mesh.polygons.foreach_set("loop_total", loop_total)
    # We're done setting up the mesh values, update mesh object and
    # let Blender do some checks on it
    mesh.update()
    mesh.validate()
    # Create Object whose Object Data is our new mesh
    obj = bpy.data.objects.new('created object', mesh)
    # Add *Object* to the scene, not the mesh
    scene = bpy.context.scene
    scene.collection.objects.link(obj)
    # Select the new object and make it active
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()


def plate(a, b, c, d, thinkness):
    if a[2] == b[2] == c[2] == d[2]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0], a[1], a[2]+thinkness],
             [b[0], b[1], b[2]+thinkness],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0], b[1], b[2]+thinkness],
             [c[0], c[1], c[2]+thinkness],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0], c[1], c[2]+thinkness],
             [d[0], d[1], d[2]+thinkness],
             [d[0], d[1], d[2]])
        face([c[0], c[1], c[2]],
             [c[0], c[1], c[2]+thinkness],
             [d[0], d[1], d[2]+thinkness],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0], d[1], d[2]+thinkness],
             [a[0], a[1], a[2]+thinkness],
             [a[0], a[1], a[2]])

        face([a[0], a[1], a[2]+thinkness],
             [b[0], b[1], b[2]+thinkness],
             [c[0], c[1], c[2]+thinkness],
             [d[0], d[1], d[2]+thinkness])
    elif a[1] == b[1] == c[1] == d[1]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0], a[1]+thinkness, a[2]],
             [b[0], b[1]+thinkness, b[2]],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0], b[1]+thinkness, b[2]],
             [c[0], c[1]+thinkness, c[2]],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0], c[1]+thinkness, c[2]],
             [d[0], d[1]+thinkness, d[2]],
             [d[0], d[1], d[2]])
        face([c[0], c[1], c[2]],
             [c[0], c[1]+thinkness, c[2]],
             [d[0], d[1]+thinkness, d[2]],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0], d[1]+thinkness, d[2]],
             [a[0], a[1]+thinkness, a[2]],
             [a[0], a[1], a[2]])

        face([a[0], a[1]+thinkness, a[2]],
             [b[0], b[1]+thinkness, b[2]],
             [c[0], c[1]+thinkness, c[2]],
             [d[0], d[1]+thinkness, d[2]])

    elif a[0] == b[0] == c[0] == d[0]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0]+thinkness, a[1], a[2]],
             [b[0]+thinkness, b[1], b[2]],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0]+thinkness, b[1], b[2]],
             [c[0]+thinkness, c[1], c[2]],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0]+thinkness, c[1], c[2]],
             [d[0]+thinkness, d[1], d[2]],
             [d[0], d[1], d[2]])
        face([c[0], c[1], c[2]],
             [c[0]+thinkness, c[1], c[2]],
             [d[0]+thinkness, d[1], d[2]],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0]+thinkness, d[1], d[2]],
             [a[0]+thinkness, a[1], a[2]],
             [a[0], a[1], a[2]])
        face([a[0]+thinkness, a[1], a[2]],
             [b[0]+thinkness, b[1], b[2]],
             [c[0]+thinkness, c[1], c[2]],
             [d[0]+thinkness, d[1], d[2]])


def plate_with_shift(a, b, c, d, thinkness, shift_x, shift_y, invert):
    if invert:
        shift_x = 0-shift_x
        shift_y = 0-shift_y
    if a[2] == b[2] == c[2] == d[2]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0]+shift_x, a[1], a[2]+thinkness],
             [b[0]-shift_y, b[1], b[2]+thinkness],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0]-shift_y, b[1], b[2]+thinkness],
             [c[0]-shift_y, c[1], c[2]+thinkness],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0]-shift_y, c[1], c[2]+thinkness],
             [d[0]+shift_x, d[1], d[2]+thinkness],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0]+shift_x, d[1], d[2]+thinkness],
             [a[0]+shift_x, a[1], a[2]+thinkness],
             [a[0], a[1], a[2]])
        face([a[0]+shift_x, a[1], a[2]+thinkness],
             [b[0]-shift_y, b[1], b[2]+thinkness],
             [c[0]-shift_y, c[1], c[2]+thinkness],
             [d[0]+shift_x, d[1], d[2]+thinkness])
    elif a[1] == b[1] == c[1] == d[1]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0]+shift_x, a[1]+thinkness, a[2]],
             [b[0]-shift_y, b[1]+thinkness, b[2]],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0]-shift_y, b[1]+thinkness, b[2]],
             [c[0]-shift_y, c[1]+thinkness, c[2]],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0]-shift_y, c[1]+thinkness, c[2]],
             [d[0]+shift_x, d[1]+thinkness, d[2]],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0]+shift_x, d[1]+thinkness, d[2]],
             [a[0]+shift_x, a[1]+thinkness, a[2]],
             [a[0], a[1], a[2]])
        face([a[0]+shift_x, a[1]+thinkness, a[2]],
             [b[0]-shift_y, b[1]+thinkness, b[2]],
             [c[0]-shift_y, c[1]+thinkness, c[2]],
             [d[0]+shift_x, d[1]+thinkness, d[2]])
    elif a[0] == b[0] == c[0] == d[0]:
        face([a[0], a[1], a[2]],
             [b[0], b[1], b[2]],
             [c[0], c[1], c[2]],
             [d[0], d[1], d[2]])
        face([a[0], a[1], a[2]],
             [a[0]+thinkness, a[1]+shift_x, a[2]],
             [b[0]+thinkness, b[1]-shift_y, b[2]],
             [b[0], b[1], b[2]])
        face([b[0], b[1], b[2]],
             [b[0]+thinkness, b[1]-shift_y, b[2]],
             [c[0]+thinkness, c[1]-shift_y, c[2]],
             [c[0], c[1], c[2]])
        face([c[0], c[1], c[2]],
             [c[0]+thinkness, c[1]-shift_y, c[2]],
             [d[0]+thinkness, d[1]+shift_x, d[2]],
             [d[0], d[1], d[2]])
        face([d[0], d[1], d[2]],
             [d[0]+thinkness, d[1]+shift_x, d[2]],
             [a[0]+thinkness, a[1]+shift_x, a[2]],
             [a[0], a[1], a[2]])

        face([a[0]+thinkness, a[1]+shift_x, a[2]],
             [b[0]+thinkness, b[1]-shift_y, b[2]],
             [c[0]+thinkness, c[1]-shift_y, c[2]],
             [d[0]+thinkness, d[1]+shift_x, d[2]])


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
size_template = [20, 20, 20]
thinkness = 1.2
shift_gap = 0.4
diff_over = 10
diff_over_x = 100
protrusion = 10

gap = 1
gap_s = thinkness/2 + 0.1

#plate
#bottom
plate([-size_template[0]/2, size_template[1]/2, 0],
      [size_template[0]/2, size_template[1]/2, 0],
      [size_template[0]/2, -size_template[1]/2, 0],
      [-size_template[0]/2, -size_template[1]/2, 0], thinkness)
#wall
plate([-size_template[0]/2, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2, size_template[1]/2-thinkness, size_template[2]],
      [-size_template[0]/2, size_template[1]/2-thinkness, size_template[2]],thinkness)
plate([-size_template[0]/2, -size_template[1]/2, thinkness],
      [size_template[0]/2, -size_template[1]/2, thinkness],
      [size_template[0]/2, -size_template[1]/2, size_template[2]],
      [-size_template[0]/2, -size_template[1]/2, size_template[2]],thinkness)
plate([size_template[0]/2-thinkness, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2-thinkness, size_template[1]/2-thinkness, size_template[2]],
      [size_template[0]/2-thinkness, -size_template[1]/2+thinkness, size_template[2]],
      [size_template[0]/2-thinkness, -size_template[1]/2+thinkness, thinkness],thinkness)
plate([-size_template[0]/2, size_template[1]/2-thinkness, thinkness],
      [-size_template[0]/2, size_template[1]/2-thinkness, size_template[2]],
      [-size_template[0]/2, -size_template[1]/2+thinkness, size_template[2]],
      [-size_template[0]/2, -size_template[1]/2+thinkness, thinkness],thinkness)
#over
plate([-size_template[0]/2, size_template[1]/2, size_template[2]+diff_over],
      [size_template[0]/2, size_template[1]/2, size_template[2]+diff_over],
      [size_template[0]/2, -size_template[1]/2, size_template[2]+diff_over],
      [-size_template[0]/2, -size_template[1]/2, size_template[2]+diff_over],thinkness)

plate([-size_template[0]/2+gap, size_template[1]/2-gap, size_template[2]+diff_over-thinkness],
      [size_template[0]/2-gap, size_template[1]/2-gap, size_template[2]+diff_over-thinkness],
      [size_template[0]/2-gap, -size_template[1]/2+gap, size_template[2]+diff_over-thinkness],
      [-size_template[0]/2+gap, -size_template[1]/2+gap, size_template[2]+diff_over-thinkness],thinkness)
#plate 2
#bottom
plate([-size_template[0]/2 + diff_over_x, size_template[1]/2, 0],
      [size_template[0]/2 + diff_over_x, size_template[1]/2, 0],
      [size_template[0]/2 + diff_over_x, -size_template[1]/2, 0],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2, 0],thinkness)
#wall
plate([-size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, size_template[2]],
      [-size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, size_template[2]],thinkness)
plate([-size_template[0]/2 + diff_over_x, -size_template[1]/2, thinkness],
      [size_template[0]/2 + diff_over_x, -size_template[1]/2, thinkness],
      [size_template[0]/2 + diff_over_x, -size_template[1]/2, size_template[2]],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2, size_template[2]],thinkness)
plate([size_template[0]/2-thinkness + diff_over_x, size_template[1]/2-thinkness, thinkness],
      [size_template[0]/2-thinkness + diff_over_x, size_template[1]/2-thinkness, size_template[2]],
      [size_template[0]/2-thinkness + diff_over_x, -size_template[1]/2+thinkness, size_template[2]],
      [size_template[0]/2-thinkness + diff_over_x, -size_template[1]/2+thinkness, thinkness],thinkness)
plate([-size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, thinkness],
      [-size_template[0]/2 + diff_over_x, size_template[1]/2-thinkness, size_template[2]],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, size_template[2]],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, thinkness],thinkness)
plate_with_shift([-size_template[0]/2 + diff_over_x+thinkness/2, size_template[1]/2, size_template[2]],
     [-size_template[0]/2 + diff_over_x, size_template[1]/2, size_template[2]],
     [-size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, size_template[2]],
     [-size_template[0]/2 + diff_over_x+thinkness/2, -size_template[1]/2+thinkness, size_template[2]], thinkness, shift_gap, 0, 0)
plate_with_shift([size_template[0]/2 + diff_over_x, size_template[1]/2, size_template[2]],
     [size_template[0]/2 + diff_over_x-thinkness/2, size_template[1]/2, size_template[2]],
     [size_template[0]/2 + diff_over_x-thinkness/2, -size_template[1]/2+thinkness, size_template[2]],
     [size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, size_template[2]], thinkness, 0, shift_gap, 0)
plate([size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, size_template[2]],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2+thinkness, size_template[2]],
      [-size_template[0]/2 + diff_over_x, -size_template[1]/2, size_template[2]],
      [size_template[0]/2 + diff_over_x, -size_template[1]/2, size_template[2]], thinkness)
#over 2 simply
plate_with_shift([-size_template[0]/2+gap_s + diff_over_x, size_template[1]/2-gap_s+protrusion, size_template[2] + diff_over - thinkness],
     [size_template[0]/2-gap_s + diff_over_x, size_template[1]/2-gap_s+protrusion, size_template[2]+diff_over-thinkness],
     [size_template[0]/2-gap_s + diff_over_x, -size_template[1]/2+gap_s, size_template[2]+diff_over-thinkness],
     [-size_template[0]/2+gap_s + diff_over_x, -size_template[1]/2+gap_s, size_template[2]+diff_over-thinkness], thinkness, shift_gap, shift_gap, 0)
