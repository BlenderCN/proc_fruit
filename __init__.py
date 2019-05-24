bl_info = {
    "name": "Procedural Fruit",
    "category": "Add Mesh",
    "author": "Rafael",
    "version": (0, 0),
    "blender":(2.79),
    }

import bpy
from .util import linkAndSelect
from .fruit import Fruit
from .evolution import Evolvable
from . import evolution
from bpy.types import (
    Panel,
    )

class GENERATE_PT_FRUIT(Panel):
	bl_label = "Random Fruit"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Fruit"

	def draw(self,context):
		layout = self.layout
		row = layout.row()
		row.operator(evolution.generateOperator(Evolvable,"Random Fruit","fruit").bl_idname)
		row1 = layout.row()
		row1.operator(evolution.mutationOperator(Evolvable,"Mutate Fruit","fruit").bl_idname)
		row2 = layout.row()
		row2.operator(evolution.editOperator(Evolvable,"Edit Fruit","fruit").bl_idname)
		row3 = layout.row()
		row3.operator(evolution.combineOperator(Evolvable,"Combine Fruits","fruit").bl_idname)


def register():
    Fruit.registerOperators()
    bpy.utils.register_class(GENERATE_PT_FRUIT)
    
def unregister():
    Fruit.unregisterOperators()
    bpy.utils.unregister_class(GENERATE_PT_FRUIT)

if __name__ == "__main__": # lets you run the script from a Blender text block; useful during development
    register()
