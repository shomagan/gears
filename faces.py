import bpy
from math import *


def plate(a, b, c, d, thickness_plate):
    shift_0 = 0.0
    shift_1 = 0.0
    shift_2 = 0.0
    vertex = [a, b, c, d]
    faces_plate = [[3, 2, 1, 0], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7], [4, 5, 6, 7]]
    if a[2] == b[2] == c[2] == d[2]:
        shift_2 = thickness_plate
    elif a[1] == b[1] == c[1] == d[1]:
        shift_1 = thickness_plate
    elif a[0] == b[0] == c[0] == d[0]:
        shift_0 = thickness_plate
    vertex.append([a[0] + shift_0, a[1] + shift_1, a[2] + shift_2])  # 4
    vertex.append([b[0] + shift_0, b[1] + shift_1, b[2] + shift_2])  # 5
    vertex.append([c[0] + shift_0, c[1] + shift_1, c[2] + shift_2])  # 6
    vertex.append([d[0] + shift_0, d[1] + shift_1, d[2] + shift_2])  # 7
    return vertex, faces_plate


def create_mesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = False
    # Link object to scene and make active
    bpy.context.collection.objects.link(ob)
    ob.select_set(True)
    # Create mesh from given verts, faces.
    me.from_pydata(verts, edges, faces)
    # Update mesh with new data
    me.update()


thickness = 1.6
size_box = [90.0+thickness*2, 28.0+thickness*2, 70.0+thickness*2]
shift_gap = 0.4
diff_over = 10
diff_over_x = 100
protrusion = 10
board_2 = [43.5, 21.5, 2.0]
board_3 = [57.0, 23.0, 2.0]
board_4 = [69.8, 47.8, 2.0]
size_between_boards = 10.0
board_3_adds = size_box[1]-board_3[1]-thickness*2-thickness*2
board_2_adds = size_box[1]-board_2[1]-thickness*2-thickness*2
overlap = 14.0
gap = 1
gap_s = thickness/2 + 0.1


#plate
vertexs, faces = plate([-size_box[0] / 2, size_box[1] / 2, 0],
                       [size_box[0] / 2, size_box[1] / 2, 0],
                       [size_box[0] / 2, -size_box[1] / 2, 0],
                       [-size_box[0] / 2, -size_box[1] / 2, 0], thickness)
create_mesh('bottom', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([-size_box[0] / 2, size_box[1] / 2 - thickness, thickness],
                       [size_box[0] / 2, size_box[1] / 2 - thickness, thickness],
                       [size_box[0] / 2, size_box[1] / 2 - thickness, size_box[2]],
                       [-size_box[0] / 2, size_box[1] / 2 - thickness, size_box[2]], thickness)
create_mesh('wall_0', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([-size_box[0] / 2, -size_box[1] / 2, thickness],
                       [size_box[0] / 2, -size_box[1] / 2, thickness],
                       [size_box[0] / 2, -size_box[1] / 2, size_box[2]],
                       [-size_box[0] / 2, -size_box[1] / 2, size_box[2]], thickness)
create_mesh('wall_1', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0] / 2 - thickness, size_box[1] / 2 - thickness, thickness],
                       [size_box[0] / 2 - thickness, size_box[1] / 2 - thickness, size_box[2]],
                       [size_box[0] / 2 - thickness, -size_box[1] / 2 + thickness, size_box[2]],
                       [size_box[0] / 2 - thickness, -size_box[1] / 2 + thickness, thickness], thickness)
create_mesh('wall_2', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([-size_box[0] / 2, size_box[1] / 2 - thickness, thickness],
                       [-size_box[0] / 2, size_box[1] / 2 - thickness, size_box[2]],
                       [-size_box[0] / 2, -size_box[1] / 2 + thickness, size_box[2]],
                       [-size_box[0] / 2, -size_box[1] / 2 + thickness, thickness], thickness)
create_mesh('wall_3', [0, 0, 0], vertexs, [], faces)
'''
vertexs, faces = plate([-size_box[0] / 2, size_box[1] / 2, size_box[2] + diff_over],
                       [size_box[0] / 2, size_box[1] / 2, size_box[2] + diff_over],
                       [size_box[0] / 2, -size_box[1] / 2, size_box[2] + diff_over],
                       [-size_box[0] / 2, -size_box[1] / 2, size_box[2] + diff_over], thickness)
create_mesh('over_0', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([-size_box[0] / 2 + gap, size_box[1] / 2 - gap, size_box[2] + diff_over - thickness],
                       [size_box[0] / 2 - gap, size_box[1] / 2 - gap, size_box[2] + diff_over - thickness],
                       [size_box[0] / 2 - gap, -size_box[1] / 2 + gap, size_box[2] + diff_over - thickness],
                       [-size_box[0] / 2 + gap, -size_box[1] / 2 + gap, size_box[2] + diff_over - thickness], thickness)
create_mesh('over_1', [0, 0, 0], vertexs, [], faces)
'''

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness, size_box[1]/2-thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness, size_box[1]/2-thickness-overlap, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness, size_box[1]/2-thickness-overlap, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness, size_box[1]/2-thickness, size_box[2]], thickness)
create_mesh('overlap_0', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1], size_box[1]/2-overlap, thickness],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-thickness-overlap, thickness],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-thickness-overlap, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-overlap, size_box[2]], thickness)
create_mesh('overlap_0_rail_0', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1], size_box[1]/2-overlap+board_4[2]+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-thickness-overlap+board_4[2]+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-thickness-overlap+board_4[2]+thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1], size_box[1]/2-overlap+board_4[2]+thickness, size_box[2]], thickness)
create_mesh('overlap_0_rail_1', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness*2, size_box[1]/2-overlap, thickness],
                       [size_box[0]/2-thickness*2, size_box[1]/2-thickness-overlap, thickness],
                       [size_box[0]/2-thickness*2, size_box[1]/2-thickness-overlap, size_box[2]],
                       [size_box[0]/2-thickness*2, size_box[1]/2-overlap, size_box[2]], thickness)
create_mesh('overlap_0_rail_2', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness*2, size_box[1]/2-overlap+board_4[2]+thickness, thickness],
                       [size_box[0]/2-thickness*2, size_box[1]/2-thickness-overlap+board_4[2]+thickness, thickness],
                       [size_box[0]/2-thickness*2, size_box[1]/2-thickness-overlap+board_4[2]+thickness, size_box[2]],
                       [size_box[0]/2-thickness*2, size_box[1]/2-overlap+board_4[2]+thickness, size_box[2]], thickness)
create_mesh('overlap_0_rail_3', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness, size_box[2]], thickness*2+board_3[2])
create_mesh('board_3_adds', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds-thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds-thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), size_box[1]/2-thickness-board_3_adds, size_box[2]], thickness)
create_mesh('board_3_rail_0', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), size_box[1]/2-thickness-board_3_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), size_box[1]/2-thickness-board_3_adds-thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), size_box[1]/2-thickness-board_3_adds-thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), size_box[1]/2-thickness-board_3_adds, size_box[2]], thickness)
create_mesh('board_3_rail_1', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), -size_box[1]/2+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), -size_box[1]/2+2*thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), -size_box[1]/2+2*thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness*2+board_3[2]), -size_box[1]/2+thickness, size_box[2]], thickness)
create_mesh('board_3_rail_2', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), -size_box[1]/2+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), -size_box[1]/2+2*thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), -size_box[1]/2+2*thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards-(thickness), -size_box[1]/2+thickness, size_box[2]], thickness)
create_mesh('board_3_rail_3', [0, 0, 0], vertexs, [], faces)


vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness-board_2_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness-board_2_adds, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness, size_box[2]], thickness*2+board_2[2])
create_mesh('board_2_adds', [0, 0, 0], vertexs, [], faces)

vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness-board_2_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-2*thickness-board_2_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-2*thickness-board_2_adds, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), size_box[1]/2-thickness-board_2_adds, size_box[2]], thickness)
create_mesh('board_2_rail_0', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, size_box[1]/2-thickness-board_2_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, size_box[1]/2-2*thickness-board_2_adds, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, size_box[1]/2-2*thickness-board_2_adds, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, size_box[1]/2-thickness-board_2_adds, size_box[2]], thickness)
create_mesh('board_2_rail_1', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), -size_box[1]/2+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), -size_box[1]/2+2*thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), -size_box[1]/2+2*thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-(thickness*2+board_2[2]), -size_box[1]/2+thickness, size_box[2]], thickness)
create_mesh('board_2_rail_2', [0, 0, 0], vertexs, [], faces)
vertexs, faces = plate([size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, -size_box[1]/2+thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, -size_box[1]/2+2*thickness, thickness],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, -size_box[1]/2+2*thickness, size_box[2]],
                       [size_box[0]/2-thickness-board_4[1]-thickness-size_between_boards*2-(thickness*2+board_3[2])-thickness, -size_box[1]/2+thickness, size_box[2]], thickness)
create_mesh('board_2_rail_3', [0, 0, 0], vertexs, [], faces)
