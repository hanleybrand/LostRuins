import json
from dataclasses import dataclass, field
from typing import List, Dict, Union

from pathlib import Path

from enum import Enum

from dataclass_wizard import JSONWizard
from marshmallow import Schema, fields

import ruined

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LR_PALETTES = Path(PROJECT_ROOT / "src/main/resources/data/lostruins/lostcities/palettes/")


def weight_list_128(length: int):
    equal_weight = int(128 / length)
    weight_list = [equal_weight for x in range(length - 1)]
    weight_list.append(1000)
    return weight_list


def dataclass_str(cls):
    return cls.__string__()


@dataclass
class Data(JSONWizard):
    palette: List['Palette']


@dataclass
class Palette:
    char: str
    block: str = None
    damaged: str = None
    blocks: List['RandomBlock'] = None


#
@dataclass
class Block:
    block: str

    def __str__(self):
        return f'{self.block}'

    def __repr__(self):
        return f'{self.block}'


@dataclass
class BlockSingle:
    char: str
    block: str
    damaged: str

    def __init__(self, char: str, block_id: str, damaged: str = "minecraft:iron_bars"):
        self.char = char
        self.block = ruined.full_block_id(block_id)
        self.damaged = ruined.full_block_id(damaged)


@dataclass
class RandomBlock:
    random: int
    block: str


#
@dataclass
class RandomBlocks:
    # name: str
    char: str
    blocks: List[RandomBlock]
    damaged: str

    def __init__(self, char: str, randomize_blocks: list, damaged: str = "minecraft:iron_bars"):
        _weight_list = weight_list_128(len(randomize_blocks))
        self.char = char
        if type(randomize_blocks[0]) == str:
            self.blocks = [RandomBlock(random=w, block=ruined.full_block_id(b)) for b, w in
                           dict(zip(randomize_blocks, _weight_list)).items()]
        elif type(randomize_blocks[0]) == dict and "random" in randomize_blocks[0].keys():
            self.blocks = [RandomBlock(random=x['random'], block=x['block']) for x in randomize_blocks]
        self.damaged = ruined.full_block_id(damaged)


@dataclass
class BasicRuinedRandomPalette(JSONWizard):
    palette: List[RandomBlocks or BlockSingle]

    def __init__(self, four_block_list: list, damaged: str = None, damaged_blocks: list = None):
        self.palette = []
        if type(four_block_list[0]) == str:
            for i, (char, block) in enumerate(dict(zip(["X", "$", "#", "}"], four_block_list)).items()):
                if damaged_blocks and len(damaged_blocks) == len(four_block_list):
                    self.palette.append(BlockSingle(char, block, damaged_blocks[i]))
                if not damaged:
                    self.palette.append(BlockSingle(char, block))
                else:
                    dmg_block = f"{damaged}"
                    self.palette.append(BlockSingle(char, block, dmg_block))
        elif type(four_block_list[0]) == dict:
            for entry in four_block_list:
                if "damaged" in entry.keys():
                    if "blocks" in entry.keys():
                        self.palette.append(RandomBlocks(entry["char"], entry["blocks"], entry["damaged"]))
                    else:
                        self.palette.append(BlockSingle(entry["char"], entry["block"], entry["damaged"]))
                elif not damaged:
                    if "blocks" in entry.keys():
                        self.palette.append(RandomBlocks(entry["char"], entry["blocks"], entry["damaged"]))
                    else:
                        self.palette.append(BlockSingle(entry["char"], entry["block"]))


@dataclass
class StylesFiveCatGenerator(JSONWizard):
    """
    Creates a 5 category style.json file that is referenced from lostcities/worldstyles/ruined.json,
    categories are:  common, default, block (definitions for building/part gen), glass block and glass pane
    the palette field is the file name of a palette.json in lostcities/palettes
    (e.g. "palette": "lostruins:ruined_bricks" refers to lostcities/palettes/ruined_bricks.json)
    """
    randompalettes: List[
        Union[
            List['PalettesCommon'],
            List['PalettesDefault'],
            List['PalettesBuildingBlockChoice'],
            List['PalettesGlassPaneChoice'],
            List['PalettesSideVariantChoice']
        ]
    ]

    def __init__(self, block_list: list, glass_list: list, last_list: list,
                 common_palette_name: str = None,
                 default_palette_name: str = None, ):
        self.randompalettes = [
            [
                PalettesCommon(palette=common_palette_name)
            ],
            [
                PalettesDefault(factor=1.0, palette=default_palette_name)
            ],
            [PalettesBuildingBlockChoice(factor=1.0, palette=block_pal) for block_pal in block_list],
            [PalettesGlassPaneChoice(factor=1.0, palette=glass_pal) for glass_pal in glass_list],
            [PalettesBuildingBlockChoice(factor=1.0, palette=last_pal) for last_pal in last_list],
        ]


@dataclass
class PalettesCommon:
    """
    points to the common palette ( eg 'common' for 'lostcites/palettes/common.json')

    """
    factor: float
    palette: str

    def __init__(self, palette: str = None):
        self.factor = 1.0
        self.palette = 'lostruins:common_ruined' if not palette else palette


@dataclass
class PalettesDefault:
    """
    Data3 dataclass

    """
    factor: float
    palette: str

    def __init__(self, factor: float = None, palette: str = None):
        self.factor = 1.0 if not factor else factor
        self.palette = 'lostruins:default_ruined' if not palette else palette


@dataclass
class PalettesBuildingBlockChoice:
    """
    Data4 dataclass

    """
    factor: float
    palette: str

    def __init__(self, factor: float = None, palette: str = None):
        self.factor = 1.0 if not factor else factor
        self.palette = palette


@dataclass
class PalettesGlassPaneChoice:
    """
    Data6 dataclass

    """
    factor: float
    palette: str

    def __init__(self, factor: float = None, palette: str = None):
        self.factor = 1.0 if not factor else factor
        self.palette = palette


@dataclass
class PalettesSideVariantChoice:
    """
    Data5 dataclass

    """
    factor: float
    palette: str

    def __init__(self, factor: float = None, palette: str = None):
        self.factor = 1.0 if not factor else factor
        self.palette = palette


if __name__ == "__main__":
    block_list = ['brown_concrete',
                  'gray_concrete',
                  'white_concrete',
                  'light_gray_concrete',
                  'black_concrete']

    gray_types = ['lostruins:gray_concrete', 'lostruins:gray_concrete_cracked',
                  'lostruins:gray_concrete_big_bricks', 'lostruins:gray_concrete_big_bricks_cracked']

    block_name = 'lostruins:white_concrete'


    random_palettes_blocks_always_include = ["lostruins:ruined_bricks", "lostruins:ruined_stone",
                                             "lostruins:ruined_stone1", "lostruins:ruined_concrete1",
                                             "lostruins:ruined_blackstone"]

    random_palettes_glass_pane_always_include = ["lostruins:glasspane_broken", "lostruins:glass_broken"]

    random_palettes_variant_always_include = ["glass_side_variant_glass",
                                              "glass_side_variant_bricks"]

    now_its_ruined = StylesFiveCatGenerator(
        random_palettes_blocks_always_include,
        random_palettes_glass_pane_always_include,
        random_palettes_variant_always_include,
        common_palette_name='lostruins:common_ruined',
        default_palette_name='lostruins:default_ruined'
    )


    bs = BlockSingle('X', block_name)
    rb = RandomBlocks(char='#', randomize_blocks=gray_types, damaged='gray_concrete_rubble')

    block_pal = BasicRuinedRandomPalette(four_block_list=[f"{block_name}_ruins", f"{block_name}_big_bricks",
                                                          f"{block_name}_ruins", f"{block_name}_ruins"],
                                         damaged=f"{block_name}_rubble"
                                         )

    with open(Path(LR_PALETTES / "ruined_bricks.json"), 'r') as f:
        ruined_bricks_d = json.load(f)['palette']

    pal = BasicRuinedRandomPalette(ruined_bricks_d)

    jo = block_pal.to_json()
    js = json.dumps(json.loads(jo), indent=2)
    # print(js)
    print(" use print(js) to see a BasicRuinedRandomPalette created from ruined_bricks.json")

    # random palettes
    rp_block_pals_always_include = ["lostruins:ruined_bricks", "lostruins:ruined_stone",
                                    "lostruins:ruined_stone1", "lostruins:ruined_concrete1",
                                    "lostruins:ruined_blackstone"]
    rp_glass_pals_always_include = ["lostruins:glasspane_broken", "lostruins:glass_broken", "glass_pane"]
    rp_side_pals_always_include = ["glass_side_variant_glass", "glass_side_variant_bricks"]

    ruined = StylesFiveCatGenerator(rp_block_pals_always_include,
                                    rp_glass_pals_always_include,
                                    rp_side_pals_always_include,
                                    'common_ruined',
                                    'default_ruined')

    styles_ruined = json.dumps(json.loads(ruined.to_json()), indent=2)
