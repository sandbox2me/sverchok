# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import bmesh
from bpy.props import EnumProperty
from sverchok.node_tree import SverchCustomTreeNode
from sverchok.data_structure import (updateNode, enum_item as e)


class SvBMOpsNode(bpy.types.Node, SverchCustomTreeNode):
    ''' BMesh Ops '''
    bl_idname = 'SvBMOpsNode'
    bl_label = 'bmesh_ops'
    bl_icon = 'OUTLINER_OB_EMPTY'

    PV = ['remove_doubles(bm,verts=Vidx,dist=v[0])',
          'collapse(bm,edges=Eidx)',
          'unsubdivide(bm,verts=Vidx,iterations=v[0])',
          'holes_fill(bm,edges=Eidx,sides=v[0])',
          'bridge_loops(bm,edges=Eidx,use_pairs=v[0],use_cyclic=v[1],use_merge=v[2],merge_factor=v[3],twist_offset=v[4])',
          'smooth_vert(bm,verts=Vidx,factor=v[0],mirror_clip_x=v[1],mirror_clip_y=v[2],mirror_clip_z=v[3],clip_dist=v[4],use_axis_x=v[5],use_axis_y=v[6],use_axis_z=v[7])',
          'dissolve_verts(bm,verts=Vidx,use_face_split=v[0],use_boundary_tear=v[1])',
          'dissolve_edges(bm,edges=Eidx,use_verts=v[0],use_face_split=v[1])',
          'dissolve_faces(bm,faces=Pidx,use_verts=v[0])',
          'triangulate(bm,faces=Pidx,quad_method=v[0],ngon_method=v[1])',
          'join_triangles(bm,faces=Pidx,cmp_sharp=v[0],cmp_uvs=v[1],cmp_vcols=v[2],cmp_materials=v[3],limit=v[4])',
          'connect_verts_concave(bm,faces=Pidx)',
          'connect_verts_nonplanar(bm,angle_limit=v[0],faces=Pidx)',
          'subdivide_edgering(bm,edges=Eidx,interp_mode=v[0],smooth=v[1],cuts=v[2],profile_shape=v[3],profile_shape_factor=v[4])',
          'inset_individual(bm,faces=Pidx,thickness=v[0],depth=v[1],use_even_offset=v[2],use_interpolate=v[3],use_relative_offset=v[4])',
          'grid_fill(bm,edges=Eidx,mat_nr=v[0],use_smooth=v[1],use_interp_simple=v[2])',
          'edgenet_fill(bm, edges=Eidx, mat_nr=v[0], use_smooth=v[1], sides=v[2])',
          'rotate_edges(bm, edges=Eidx, use_ccw=v[0])'
          ]

    oper = EnumProperty(name="BMop", default=PV[0], items=e(PV), update=updateNode)

    def sv_init(self, context):
        si = self.inputs.new
        si('StringsSocket', 'bmesh_list')
        si('StringsSocket', 'Value(v)')
        si('StringsSocket', 'idx')
        self.outputs.new('StringsSocket', 'bmesh_list')

    def draw_buttons(self, context, layout):
        layout.prop(self, "oper", "Get")

    def process(self):
        if not self.outputs['bmesh_list'].is_linked:
            return
        si = self.inputs
        obj = si['bmesh_list'].sv_get()
        obl = len(obj)
        if obl>1:
            v = (si['Value(v)'].sv_get([[1,1,1,1,1,1,1,1]])*obl)[:obl]
            idx = (si['idx'].sv_get([[0]])*obl)[:obl]
        else:
            v = si['Value(v)'].sv_get([[1,1,1,1,1,1,1,1]])
            idx = si['idx'].sv_get([[0]])
        Sidx = si['idx'].is_linked
        outp = []
        op = "bmesh.ops."+self.oper
        if "verts=Vidx" in op:
            cur = 1
        elif "edges=Eidx" in op:
            cur = 2
        elif "faces=Pidx" in op:
            cur = 3
        for bm, v, idx in zip(obj,v,idx):
            if Sidx:
                if cur == 1:
                    bm.verts.ensure_lookup_table()
                    Vidx = [bm.verts[i] for i in idx]
                elif cur == 2:
                    bm.edges.ensure_lookup_table()
                    Eidx = [bm.edges[i] for i in idx]
                elif cur == 3:
                    bm.faces.ensure_lookup_table()
                    Pidx = [bm.faces[i] for i in idx]
            else:
                Vidx,Eidx,Pidx=bm.verts,bm.edges,bm.faces
            exec(op)
            outp.append(bm.copy())
            bm.free()
        self.outputs['bmesh_list'].sv_set(outp)

    def update_socket(self, context):
        self.update()


def register():
    bpy.utils.register_class(SvBMOpsNode)


def unregister():
    bpy.utils.unregister_class(SvBMOpsNode)