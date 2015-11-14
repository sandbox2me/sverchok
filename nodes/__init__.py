nodes_dict = {
    'analyzer': [
        'area',
        'normals',
        'volume',
        'bbox',
        'mesh_filter',
        'edge_angles',
        'distance_pp',
        'polygons_centers',
        'neuro_elman',
        'image_components',
        'kd_tree',
        'kd_tree_edges',
        'weights',
        'object_raycast',
        'scene_raycast',
        'bmesh_props',
        'closest_point_on_mesh',
        'colors',
       # 'bvh_raycast',
       # 'bvh_overlap',
       # 'bvh_nearest'
    ],

    'basic_view': [
        'viewer_bmesh',
        'viewer_bmesh_mk2',
        'viewer_indices',
        'viewer_curves',
        'viewer_skin',
        'viewer_text',
        'viewer_mk2',
        'viewer_typography',
        'empty_out',
    ],

    'basic_data': [
        'objects',
        'text',
        'wifi_in',
        'wifi_out',
        'switch',
        'obj_remote',
        'group',
        'cache',
        'getsetprop',
        'get_blenddata',
        'set_blenddata',
        'sort_blenddata',
        'filter_blenddata',
        'blenddata_to_svdata',
        'BMOperators',
        'bmesh_in',
        'bmesh_out',
       # 'create_bvh_tree',
        'bmesh_to_element'
    ],

    'basic_debug': [
        'debug_print',
        'frame_info',
        'gtext',
        'note',
        '3dview_props',
        'stethoscope'
    ],

    'generator': [
        'box',
        'box_rounded',
        'circle',
        'ngon',
        'cylinder',
        'hilbert_image',
        'hilbert',
        'hilbert3d',
        'image',
        'line',
        'plane',
        'bricks',
        'random_vector',
        'script',
        'script_mk2',
        'prototyper_js',
        'dupli_instances',
        'formula',
        'sphere',
        'basic_spline',
        'basic_3pt_arc',
        'instancer',
        'profile',
        'generative_art'
    ],

    'list_basic': [
        'converter',
        'decompose',
        'func',
        'join',
        'length',
        'levels',
        'mask_join',
        'mask',
        'match',
        'sum',
        'sum_mk2',
        'zip'
    ],

    'list_interfere': [
        'shift',
        'shift_mk2',
        'repeater',
        'slice',
        'split',
        'start_end',
        'item',
        'reverse',
        'shuffle',
        'sort',
        'sort_mk2',
        'flip',
        'numpy_array'
    ],

    'matrix': [
        'apply',
        'apply_and_join',
        'deform',
        'destructor',
        'generator',
        'input',
        'interpolation',
        'shear',
        'euler'
    ],

    'modifier_change': [
        'delete_loose',
        'edges_intersect',
        'holes_fill',
        'mesh_join',
        'mesh_separate',
        'mirror',
        'polygons_boom',
        'polygons_to_edges',
        'triangulate',
        'remove_doubles',
        'recalc_normals',
        'rotation',
        'scale',
        'vertices_mask',
        'bevel',
        'objects_along_edge',
        'randomize',
        'extrude_separate',
        'extrude_edges',
        'iterate',
    ],

    'modifier_make': [
        'bisect',
        'convex_hull',
        'cross_section',
        'edges_adaptative',
        'join_tris',
        'lathe',
        'line_connect',
        'offset',
        'inset_special',
        'polygons_adaptative',
        'solidify',
        'voronoi_2d',
        'wireframe',
        'wafel',
        'csg_boolean',
        'pipe_tubes',
        'matrix_tube',
    ],  #

    'number': [
        'float_to_int',
        'float',
        'integer',
        'random',
        'formula2',
        'scalar',
        'list_input',
        'range_map',
        'range_float',
        'range_int',
        'fibonacci',
        'exponential',
        'easing',
        'logic'
    ],

    'vector': [
        'drop',
        'interpolation',
        'interpolation_mk2',
        'line_evaluate',
        'math',
        'move',
        'noise',
        'normal',
        'vector_polar_in',
        'vector_polar_out',
        'vector_in',
        'vector_out',
        'vertices_delete_doubles',
        'vertices_sort',
        'axis_input'
    ],

    'network': [
        'udp_client'
    ]

}
