from block_templates.models.block.basic_block import basic_block
from block_templates.models.block.damaged_block import damaged_block
from block_templates.models.block.damaged_block1 import damaged_block1
from block_templates.models.block.damaged_block2 import damaged_block2
from block_templates.models.block.chipped_block1 import chipped_block1

from block_templates.blockstates.basic_block import basic_blockstate
from block_templates.blockstates.damaged_block import blockstate_damaged

mod_name = "kubejs"
block_name = "black_concrete"
texture_name = "black_concrete"

common_weight = 150
less_common_weight = 30

block_states = [basic_blockstate, blockstate_damaged]
block_models = [basic_block, damaged_block, damaged_block1, damaged_block2, chipped_block1]













