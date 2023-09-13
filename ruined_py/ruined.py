import glob
import json
import os
import shutil
from pathlib import Path

from PIL import Image as Img
import blend_modes

from texture_generation import get_rgba, get_mask, img_blend, composite
from texture_generation import big_brick, big_brick_grout, big_brick_3d, big_brick_grout_lighter
from texture_generation import small_brick, sm_brick_grout, sm_brick_3d
from texture_generation import specks_1, specks_2, mellow_noise, contrasty_noise
from texture_generation import moss_trans1, moss_trans2, moss_a, moss_b, moss_c

# need to look into this, circular import errors using just "import block_meta"
import block_meta as blmt
import color_utils as colu

import ruined_dataclasses

from block_templates.models.block.basic_block import basic_block
from block_templates.models.block.damaged_block import damaged_block
from block_templates.models.block.damaged_block1 import damaged_block1
from block_templates.models.block.damaged_block2 import damaged_block2
from block_templates.models.block.chipped_block1 import chipped_block1, chipped_block1_simple
from block_templates.models.block.chipped_block2 import chipped_block2
from block_templates.models.block.slab import slab
from block_templates.models.block.stairs import stairs, inner_stairs, outer_stairs

from block_templates.blockstates.ruins_block import ruins_blockstate
from block_templates.blockstates.basic_block import basic_blockstate
from block_templates.blockstates.damaged_block import blockstate_damaged
from block_templates.blockstates.big_bricks import big_bricks

# constants & setup vars
MOD_NAME = "lostruins"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PY_ROOT = Path(PROJECT_ROOT / 'ruined_py')
BUILT_ASSETS = Path(PY_ROOT / f"built_resources")

LR_ASSETS_OUT = Path(BUILT_ASSETS / f"assets/lostruins/")
BLOCK_MODELS_DIR = Path(LR_ASSETS_OUT / f"models/block/")
BLOCKSTATES_DIR = Path(LR_ASSETS_OUT / f"blockstates/")
BLOCK_TEXTURES_DIR = Path(LR_ASSETS_OUT / f"textures/block/")

LR_DATA_OUT = Path(PY_ROOT / f"built_resources/data/lostruins")
LR_DATA_OUT_LC = Path(LR_DATA_OUT / f"lostcities")
LR_DATA_OUT_PALETTES = Path(LR_DATA_OUT_LC / "palettes")
LR_DATA_OUT_STYLES = Path(LR_DATA_OUT_LC / "styles")

LR_ASSETS_STATIC = Path(PY_ROOT / f"assets_static/assets/lostruins")
LR_DATA_STATIC = Path(PY_ROOT / f"assets_static/data/lostruins")
LR_STATIC_MODELS = Path(LR_ASSETS_STATIC / f"models/block")
LR_STATIC_TEXTURES = Path(LR_ASSETS_STATIC / f"textures/block")

SRC_MAIN_ASSETS = Path(PROJECT_ROOT / 'src/main/resources/assets/lostruins')
SRC_MAIN_DATA = Path(PROJECT_ROOT / 'src/main/resources/data/lostruins')

REGISTRATION_COPYPASTA = Path(BUILT_ASSETS / "registration_copypasta.txt")
#
# common_weight = 150
# less_common_weight = 30

os.makedirs(os.path.dirname(BLOCK_MODELS_DIR), exist_ok=True)
os.makedirs(os.path.dirname(BLOCKSTATES_DIR), exist_ok=True)
os.makedirs(os.path.dirname(BLOCK_TEXTURES_DIR), exist_ok=True)

# textures in  name & data prep: load .png file from dirs and
# create lists to zip in to dicts
concrete_list = glob.glob(os.path.join('blocks_to_ruin', "concrete/*.png"))
stone_list = glob.glob(os.path.join('blocks_to_ruin', "stones/*.png"))
etc_list = glob.glob(os.path.join('blocks_to_ruin', "etc/*.png"))
roads_list = glob.glob(os.path.join('blocks_to_ruin', "roads/*.png"))

concretes = [Img.open(path) for path in concrete_list]
concretes_names = [texture.split('/')[-1].split('.')[0] for texture in concrete_list]

stones = [Img.open(path) for path in stone_list]
stones_names = [texture.split('/')[-1].split('.')[0] for texture in stone_list]

etces: list = [Img.open(path) for path in etc_list]
etces_names = [texture.split('/')[-1].split('.')[0] for texture in etc_list]

roads: list = [Img.open(path) for path in roads_list]
roads_names = [texture.split('/')[-1].split('.')[0] for texture in roads_list]

# concrete_colors = [tn.removesuffix('_concrete') for tn in concretes_names]

concrete_ruins = []
concrete_ruins_names = []
block_registration_txt = []

random_palettes = []

skip_cracks = ['gray_wood_boards', 'gray_wood_planks_nailed', 'gray_wood_planks', 'tile_irregular']

lighter_grout = ['andesite', 'deepslate_top', 'dripstone_block']

make_bricks = [
    'magenta_concrete', 'blue_concrete', 'cyan_concrete', 'lime_concrete', 'brown_concrete', 'gray_concrete',
    'white_concrete', 'green_concrete', 'purple_concrete', 'pink_concrete', 'yellow_concrete',
    'light_gray_concrete', 'light_blue_concrete', 'red_concrete', 'black_concrete', 'orange_concrete',
    'andesite', 'blackstone', 'deepslate', 'diorite', 'dripstone_block', 'red_sandstone', 'sandstone',
    'smooth_basalt', 'stone', 'old_stone', 'tuff', 'plastic_blue', 'white_granite'
]

# don't create a randompalette for building generation
skip_random_palette = [
    'magenta_concrete', 'blue_concrete', 'cyan_concrete', 'lime_concrete',
    'green_concrete', 'purple_concrete', 'pink_concrete', 'yellow_concrete',
    'light_blue_concrete', 'red_concrete', 'orange_concrete',
    'asphalt', 'asphalt_darker', 'asphalt_lined', 'asphalt_lined1', 'blackstone_top',
    'beige_tile', 'beige_tile_2',
    'basalt_side', 'basalt_top', 'deepslate_top',
    'gray_wood_planks', 'gray_wood_boards', 'gray_wood_planks_nailed',
    'red_sandstone_top', 'sandstone_bottom', 'sandstone_top', 'smooth_stone_slab_side',
    'tile_irregular',
]

# TODO: refactor script so that bricks are skipped if necessary instead of needing to be declared via make_bricks
skip_bricks = [
    'asphalt', 'asphalt_darker', 'asphalt_lined', 'asphalt_lined1', 'polished_andesite', 'polished_blackstone',
    'polished_deepslate', 'çobblestone', 'cobbled_deepslate', 'blackstone_top', 'basalt_side', 'basalt_top',
    'red_sandstone_top', 'sandstone_bottom', 'sandstone_top',
]

# it would be nice to do this, but need to revise block_meta.py & randompalette gen
# to make sure other data files don't point at non-existant resources
skip_rubble = []


# skip_rubble = ['blackstone', 'cobblestone',
#                'gray_wood_planks', 'gray_wood_boards', 'gray_wood_planks_nailed','beige_tile_2']


def full_block_id(block_id: str):
    if "lostruins" not in block_id.split(':') and ":" not in block_id:
        return f"lostruins:{block_id}"
    else:
        return block_id


def full_ruins_id_from_base(block_id: str):
    if "lostruins" not in block_id.split(':') and ":" not in block_id:
        block_id = f"lostruins:{block_id}"
    if "_ruins" not in block_id[-6:]:
        block_id = f"{block_id}_ruins"
    return block_id


def reg_variant(block_name: str, name: str, texture_sub: str, variant_list: list[str] = None):
    lr_txts = []
    for v in variant_list:
        lr_txts.append(f'lrTxt("{texture_sub}/{v}")')

    return f"""
            variant("{block_name}", "{name}", {', '.join(lr_txts)}); """


def reg_rubble(block_name: str, name: str, texture_sub: str):
    return f'            rubble("{block_name}_rubble", "{name} Rubble", lrTxt("{texture_sub}/{block_name}"));\n'


def generate_registrations(block_id_list: list, texture_sub: str, id_suffix=None, reg_all_variants=None) -> tuple:
    block_list, rubble_list = ([], [])

    for block_id in block_id_list:
        if id_suffix:
            block_id = f"{block_id}_{id_suffix}"

        cracked = f"{block_id}_cracked"
        big_bricks = f"{block_id}_big_bricks"
        big_bricks_cracked = f"{block_id}_big_bricks_cracked"
        has_cracked = Path(f'assets_out/lostruins/textures/block/{texture_sub}/{cracked}.png').exists()
        has_bricks = Path(f'assets_out/lostruins/textures/block/{texture_sub}/{big_bricks}.png').exists()
        has_bricks_cracked = Path(
            f'assets_out/lostruins/textures/block/{texture_sub}/{big_bricks_cracked}.png').exists()

        name = " ".join([word.capitalize() for word in f"{block_id}".split('_')])
        # base variant

        variant_base_list = [f"{block_id}", f"{block_id}1", f"{block_id}2", f"{block_id}3", f"{block_id}4",
                             f"{block_id}5"]

        variant_cracked_list = [f"{cracked}", f"{cracked}1", f"{cracked}2",
                                f"{cracked}3", f"{cracked}4", f"{cracked}5"]

        ruined_variants = variant_base_list + variant_cracked_list if block_id not in skip_cracks and has_cracked else variant_base_list

        # register the _ruined type as a variant block. This always happens
        # this has the most variants,for _ruins blocks with lots of variation
        block_list.append(reg_variant(f"{block_id}_ruins", f"{name} Ruins", texture_sub, sorted(ruined_variants)))

        # register rubble for the block unless block_id in skip_rubble
        if block_id not in skip_rubble:
            rubble_list.append(reg_rubble(block_id, name, texture_sub))

        # if reg_all_variants, each texture subtype is a separate registration
        if reg_all_variants:
            # register discrete base block
            block_list.append(reg_variant(f"{block_id}", f"{name}", texture_sub, sorted(variant_base_list)))

            # has_cracked ensures the _cracked textures have been generated
            if block_id not in skip_cracks and has_cracked:
                block_list.append(
                    reg_variant(f"{block_id}_cracked", f"{name} (Cracked)", texture_sub, sorted(variant_cracked_list))
                )

        # has_bricks checks if the bricks texture exists
        if has_bricks:
            variant_big_bricks = [f"{big_bricks}", f"{big_bricks}1", f"{big_bricks}2", f"{big_bricks}3",
                                  f"{big_bricks}4", f"{big_bricks}5"]

            if block_id not in skip_cracks:
                variant_big_bricks_cracked = [f"{big_bricks_cracked}", f"{big_bricks_cracked}1",
                                              f"{big_bricks_cracked}2",
                                              f"{big_bricks_cracked}3", f"{big_bricks_cracked}4",
                                              f"{big_bricks_cracked}5"]
                ruined_brick_variants = variant_big_bricks + variant_big_bricks_cracked
                if reg_all_variants:
                    # register discrete big_bricks_cracked block
                    block_list.append(reg_variant(big_bricks_cracked,
                                                  f"{name} (Cracked Big Bricks)",
                                                  texture_sub,
                                                  sorted(variant_big_bricks_cracked))
                                      )
            else:
                ruined_brick_variants = variant_big_bricks
                if reg_all_variants:
                    # register discrete big_bricks block
                    block_list.append(
                        reg_variant(big_bricks, f"{name} (Big Bricks)", texture_sub, sorted(variant_big_bricks))
                    )

            # register the _ruined type as a variant block. This always happens
            block_list.append(reg_variant(f"{big_bricks}_ruins",
                                          f"{name} Big Brick Ruins",
                                          texture_sub,
                                          sorted(ruined_brick_variants)
                                          )
                              )

    return block_list, rubble_list


def ruin_blocks(name_list: list[str],
                pil_img_list: list[Img],
                save_texture_dir_name: str) -> [list[str], list[Img]]:
    ruined_blocks, ruined_block_names = ([], [])

    # for file endings in range(6) -- list:  ['', 1, 2, 3, 4, 5]
    file_ends = [numb if numb > 0 else "" for numb in range(6)]

    save_texture_dir = os.path.join(BLOCK_TEXTURES_DIR, save_texture_dir_name)

    def add_it(pil_img, name, img_out_list=None, name_out_list=None):
        if name_out_list is None:
            name_out_list = ruined_block_names
        if img_out_list is None:
            img_out_list = ruined_blocks
        img_out_list.append(pil_img)
        name_out_list.append(name)
        pil_img.save(os.path.join(save_texture_dir, f"{name}.png"))

    for b_name, b_tex in dict(zip(name_list, pil_img_list)).items():
        concrete_ruins.append(b_tex)
        concrete_ruins_names.append(b_name)
        # rgba_tex = b_tex.convert('RGBA')

        ruined_bases = []
        ruined_bases_names = []

        def ruining_sequence(number):
            match number:
                case 0:
                    return img_blend(b_tex.convert('RGBA'), specks_2, blend_modes.multiply, .29)
                case 1:
                    return img_blend(ruined_bases[0], specks_2.rotate(90), blend_modes.multiply, .22)
                case 2:
                    return img_blend(ruined_bases[1], specks_1.rotate(90), blend_modes.multiply, .3)
                case 3:
                    return img_blend(ruined_bases[2], specks_1.rotate(90), blend_modes.multiply, .3)
                case 4:
                    return img_blend(ruined_bases[3], specks_1, blend_modes.multiply, .3)
                case _:
                    return img_blend(ruined_bases[4], specks_1.rotate(90), blend_modes.multiply, .3)

        # moss textures need a redo
        def moss_sequence(number):
            match number:
                case 0:
                    return composite(b_tex.convert('RGBA'), moss_a)
                case 1:
                    return composite(ruined_bases[0], moss_trans1)
                case 2:
                    return composite(ruined_bases[1], moss_b)
                case 3:
                    return composite(ruined_bases[2], moss_trans2)
                case 4:
                    return composite(ruined_bases[3], moss_c)
                case _:
                    return composite(ruined_bases[4], moss_b.rotate(90))

        mosses = [moss_a, moss_b, moss_trans1, moss_b.rotate(90), moss_trans2, moss_c]

        # create ruined bases & big_bricks, plus add them to the out lists
        for numb in range(6):
            ruin_name = f'{b_name}{file_ends[numb]}'
            mossy_name = f'{b_name}_mossy{file_ends[numb]}'
            # adds the img and name to respective lists, saves the file and creates the block model
            add_it(
                ruining_sequence(numb),
                ruin_name,
                ruined_bases,
                ruined_bases_names
            )

            add_it(
                ruining_sequence(numb),
                ruin_name
            )

        def cracked_blocks_and_bricks():
            """cracked blocks & bricks"""
            pass

        crack_bases = [ruined_bases[x] for x in [3, 4, 5, 4, 3, 4]]
        full_block_cracks, big_brick_cracks = ([], [])

        rgb = blmt.BLOCK_META[b_name]['rgb']
        b_colour = colu.colour_from_rgb_tuple(rgb)
        b, w = colu.get_color_ramp(base_rgb=rgb, steps=2, light_lum=.99, dark_lum=0.15)
        b_lum = b_colour.get_luminance()

        # # this creates the lists
        # for numb in range(6):
        #     file_end = file_ends[numb]
        #     full_block_cracks.append(Img.open(f'res16/cracks_full_block/cracks{file_end}.png'))
        #     big_brick_cracks.append(Img.open(f'res16/cracks_big_brick/cracks{file_end}.png'))
        # cracks_tex = Img.open(f'res16/cracks{file_end}.png')
        # r, g, b, cr_alpha = cracks_tex.split()
        # cracks_mask = ImageOps.invert(cr_alpha)

        # crack_brick = ImageChops.composite(crack_bases[-numb], cracks_tex, cracks_mask)
        # # crack_brick = composite(crack_bases[-numb], cracks_tex)
        # # blend was too little cracks @ .75, .25 was too much cracks-- trying .6
        # crack_brick2 = ImageChops.blend(crack_brick, ruined_bases[numb], .6)

        def crack_texturizer(base_texture, base_name, grayscale_crack, color_crack):
            texturized_cracked = base_texture.copy()
            texturized_cracked.paste(color_crack, (0, 0), color_crack)
            # blending the grayscle crack
            grayscale_crack_comp = texturized_cracked.copy()
            grayscale_crack_comp.paste(grayscale_crack, (0, 0), grayscale_crack)

            # TODO: needs to be changed so the efects of this blend step are more obvious (add to block_meta?)
            if base_name in ['black', 'blue', 'brown_concrete', 'purple_concrete', 'red_concrete', 'gray_concrete']:
                texturized_cracked = img_blend(texturized_cracked, grayscale_crack_comp, blend_modes.lighten_only, .25)

            elif base_name in ['green_concrete', 'gray_concrete']:
                texturized_cracked = img_blend(texturized_cracked, grayscale_crack_comp, blend_modes.lighten_only, .30)

            elif base_name in ['cyan_concrete', 'green_concrete', 'light_blue_concrete', 'magenta_concrete',
                               'orange_concrete', 'pink_concrete', 'lime_concrete']:
                texturized_cracked = img_blend(texturized_cracked, grayscale_crack_comp, blend_modes.lighten_only, .45)

            elif base_name in ['pink_concrete', 'yellow_concrete', 'light_gray_concrete']:
                texturized_cracked = img_blend(texturized_cracked, grayscale_crack_comp, blend_modes.lighten_only, .95)
            else:
                texturized_cracked = img_blend(texturized_cracked, grayscale_crack_comp, blend_modes.lighten_only, .50)

            return texturized_cracked

        # loops through the base texture and creates cracked & brick variants
        for numb in range(6):
            if b_name in skip_cracks:
                continue
            file_end = file_ends[numb]
            full_block_cracks.append(Img.open(f'res16/cracks_full_block/cracks{file_end}.png'))
            big_brick_cracks.append(Img.open(f'res16/cracks_big_brick/cracks{file_end}.png'))

            # lets save the colored cracks, because it's fun to do things like that
            colored_full_block_crack = full_block_cracks[numb]
            plain_full_block_crack = full_block_cracks[numb]
            colored_full_block_crack = colu.colorize_overlay(colored_full_block_crack, b, w, mid_rgb=rgb)
            colored_full_block_crack.save(f'res16/cracks_colors/full_block/{b_name}_cracks{file_end}.png')

            cracked_block = crack_texturizer(crack_bases[numb],
                                             b_name,
                                             plain_full_block_crack,
                                             colored_full_block_crack)

            add_it(
                cracked_block,
                f"{b_name}_cracked{file_end}")

            # cancel mossy until it's ready
            # add_it(composite(crack_brick2, mosses[numb]), f"{b_name}_cracked_mossy{file_end}")

            if b_name in make_bricks:
                # generate colored crack files
                colored_big_brick_crack = big_brick_cracks[numb]
                plain_big_brick_crack = colored_big_brick_crack
                colored_big_brick_crack = colu.colorize_overlay(colored_big_brick_crack, b, w, mid_rgb=rgb)
                colored_big_brick_crack.save(f'res16/cracks_colors/big_brick/{b_name}_cracks{file_end}.png')

                # creates cracks based on
                cracked_brick_base = crack_texturizer(crack_bases[numb],
                                                      b_name,
                                                      plain_big_brick_crack,
                                                      colored_big_brick_crack)

                grout = big_brick_grout_lighter if b_name in lighter_grout else big_brick_grout
                add_it(
                    big_brick(crack_bases[numb], grout, blend_step=True, blend_amt=.7),
                    f'{b_name}_big_bricks{file_end}'
                )
                add_it(
                    big_brick(cracked_brick_base, grout),
                    f"{b_name}_big_bricks_cracked{file_end}"
                )
                # mosses on hold until textures fixed
                # add_it(
                #     composite(big_brick(cracked_block, grout), mosses[numb]),
                #     f"{b_name}_big_bricks_cracked{file_end}"
                # )

        # need to redo the mossy textures, they are not working
        # add_it(
        #     moss_sequence(numb),
        #     mossy_name
        # )
        # make brick variants
        # print(b_name,b_name in make_bricks)

        # bricks should go after cracks
        # if b_name in make_bricks:
        #     for numb in range(6):
        #         grout = big_brick_grout_lighter if b_name in lighter_grout else big_brick_grout
        #         add_it(
        #             big_brick(ruined_bases[numb], grout, blend_step=True, blend_amt=.7),
        #             f'{b_name}_big_bricks{file_ends[numb]}'
        #         )
        # re-add when mosses are redone
        # add_it(
        #     composite(big_brick(ruined_bases[numb], grout,
        #                         blend_step=True, blend_amt=.7), mosses[numb]),
        #     f'{b_name}_big_bricks_mossy{file_ends[numb]}'
        # )

        # cracked variants

        """ blockstates & models json """
        # finally, create the blockstates json files that define the variants

        # this will supply a textures/block sub dir to models etc (e.g. 'concretes/black_concrete')
        b_texture_res_loc = f"{save_texture_dir_name}/{b_name}"

        # base
        with open(os.path.join(BLOCKSTATES_DIR, f'{b_name}.json'), 'w') as f:
            f.write(basic_blockstate.substitute(mod_name=MOD_NAME,
                                                block_name=f"{b_name}",
                                                common_weight=150,
                                                less_common_weight=30)
                    )

        with open(os.path.join(BLOCKSTATES_DIR, f'{b_name}_ruins.json'), 'w') as f:
            f.write(ruins_blockstate.substitute(mod_name=MOD_NAME,
                                                block_name=f"{b_name}",
                                                common_weight=150,
                                                cracked_weight=40,
                                                less_common_weight=30)
                    )

        # generate lostcities randompalettes

        if b_name not in skip_random_palette:
            compl_name = blmt.get_complimentary_block(b_name)
            full_b_name = full_block_id(b_name)

            # random_palettes.append(
            #     {
            #         "factor": 1.0,
            #         "palette": f"{full_b_name}_ruins"
            #     })
            random_palettes.append(f"{full_b_name}_ruins")

            pal = ruined_dataclasses.BasicRuinedRandomPalette(
                four_block_list=[f"{full_b_name}_ruins", f"{compl_name}_ruins",
                                 f"{full_b_name}_ruins", f"{full_b_name}_ruins"],
                damaged=f"{full_b_name}_rubble"
            )

            jo = pal.to_json()
            js = json.dumps(json.loads(jo), indent=2)
            with open(Path(LR_DATA_OUT_PALETTES / f"{b_name}_ruins.json"), 'w') as f:
                f.write(js)

        # big_bricks blockstate
        with open(os.path.join(BLOCKSTATES_DIR, f'{b_name}_big_bricks.json'), 'w') as f:
            f.write(big_bricks.substitute(mod_name=MOD_NAME,
                                          block_name=f"{b_name}",
                                          common_weight=150,
                                          less_common_weight=30)
                    )
        # damaged blockstate
        with open(os.path.join(BLOCKSTATES_DIR, f'{b_name}_damaged.json'), 'w') as f:
            f.write(blockstate_damaged.substitute(
                mod_name=MOD_NAME,
                block_name=b_name,
                common_weight=150,
                less_common_weight=30)
            )

        ## models that only apply to basic blocks
        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_chipped1.json'), 'w') as f:
            f.write(chipped_block1_simple.substitute(mod_name=MOD_NAME,
                                                     side_texture=f"{b_texture_res_loc}5",
                                                     bottom_texture=f"{b_texture_res_loc}_cracked1",
                                                     top_texture=f"{b_texture_res_loc}4"))

        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_chipped2.json'), 'w') as f:
            f.write(chipped_block2.substitute(mod_name=MOD_NAME,
                                              side_texture=f"{b_texture_res_loc}_cracked4",
                                              bottom_texture=f"{b_texture_res_loc}_cracked2",
                                              top_texture=f"{b_texture_res_loc}_cracked3"))
            # _big_bricks_chipped1
        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_big_bricks_chipped1.json'), 'w') as f:
            f.write(chipped_block1_simple.substitute(mod_name=MOD_NAME,
                                                     side_texture=f"{b_texture_res_loc}_big_bricks5",
                                                     bottom_texture=f"{b_texture_res_loc}_big_bricks3",
                                                     top_texture=f"{b_texture_res_loc}_big_bricks2"))

        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_big_bricks_chipped2.json'), 'w') as f:
            f.write(chipped_block2.substitute(mod_name=MOD_NAME,
                                              side_texture=f"{b_texture_res_loc}_big_bricks_cracked4",
                                              bottom_texture=f"{b_texture_res_loc}_big_bricks_cracked1",
                                              top_texture=f"{b_texture_res_loc}_big_bricks_cracked5"))

        # damaged blocks
        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_damaged.json'), 'w') as f:
            f.write(damaged_block.substitute(mod_name=MOD_NAME,
                                             texture_name=f"{b_texture_res_loc}5"))

        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_damaged1.json'), 'w') as f:
            f.write(damaged_block1.substitute(mod_name=MOD_NAME,
                                              texture_name=f"{b_texture_res_loc}_cracked4"))

        with open(os.path.join(BLOCK_MODELS_DIR, f'{b_name}_damaged2.json'), 'w') as f:
            f.write(damaged_block2.substitute(mod_name=MOD_NAME,
                                              texture_name=f"{b_texture_res_loc}3"))

        # models -- for x:
        #               {b_name}[''-5],  {b_name}_cracked[''-5]

        for numb in range(6):
            file_ends = [numb if numb > 0 else "" for numb in range(6)]
            file_end = file_ends[numb]
            # split_name = [b_name.split(b_name.split('_')[-1])[0], b_name.split('_')[-1]]

            # regular ruined bases - handled by LostRuins:RunData
            with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}{file_end}.json"), 'w') as f:
                f.write(basic_block.substitute(mod_name=MOD_NAME, texture_name=f"{b_texture_res_loc}{file_end}"))

            if b_name not in skip_cracks:
                with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_cracked{file_end}.json"), 'w') as f:
                    f.write(
                        basic_block.substitute(mod_name=MOD_NAME, texture_name=f"{b_texture_res_loc}{file_end}"))

            # big_bricks & cracked_bricks - handled by LostRuins:RunData, unless generate_all_reg is false =\
            if b_name in make_bricks:
                with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_big_bricks{file_ends[numb]}.json"), 'w') as f:
                    f.write(basic_block.substitute(mod_name=MOD_NAME,
                                                   texture_name=f"{b_texture_res_loc}_big_bricks{file_ends[numb]}"))
                if b_name not in skip_cracks:
                    with open(os.path.join(BLOCK_MODELS_DIR,
                                           f"{b_name}_big_bricks_cracked{file_ends[numb]}.json"), 'w') as f:
                        f.write(basic_block.substitute(mod_name=MOD_NAME,
                                                       texture_name=f"{b_texture_res_loc}_big_bricks{file_ends[numb]}"))

        # TODO: implement stair blocks via com.mcjty.lostruins.blocks
        # not making big_brick stairs or slabs
        # stair_bottom = f"{b_name}{file_ends[numb]}"
        # stair_side = f"{b_name}{file_ends[numb]}"
        # stair_top = f"{b_name}{file_ends[numb]}"
        # slab_bottom = f"{b_name}{file_ends[numb]}"
        # slab_top = f"{b_name}{file_ends[numb]}"
        # slab_side = f"{b_name}{file_ends[numb]}"
        #
        # with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_stairs{file_ends[numb]}.json"), 'w') as f:
        #     f.write(stairs.substitute(mod_name=MOD_NAME, bottom_texture=stair_bottom,
        #                               side_texture=stair_side, top_texture=stair_top))
        # with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_stairs_inner{file_ends[numb]}.json"), 'w') as f:
        #     f.write(inner_stairs.substitute(mod_name=MOD_NAME, bottom_texture=stair_bottom,
        #                                     side_texture=stair_side, top_texture=stair_top))
        #
        # with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_stairs_outer{file_ends[numb]}.json"), 'w') as f:
        #     f.write(outer_stairs.substitute(mod_name=MOD_NAME, bottom_texture=stair_bottom,
        #                                     side_texture=stair_side, top_texture=stair_top))

        # TODO: implement slab texture gen via ruined_py
        # TODO: implement slab blocks via com.mcjty.lostruins.blocks
        # # slabs have multiple textures
        # with open(os.path.join(BLOCK_MODELS_DIR, f"{b_name}_slab{file_ends[numb]}.json"), 'w') as f:
        #     f.write(slab.substitute(mod_name=MOD_NAME, bottom_texture=slab_bottom,
        #                             side_texture=slab_side, top_texture=slab_top))

    random_palettes_blocks_always_include = ["lostruins:ruined_bricks", "lostruins:ruined_stone",
                                             "lostruins:ruined_stone1", "lostruins:ruined_concrete1",
                                             "lostruins:ruined_blackstone"]

    random_palettes_glass_pane_always_include = ["lostruins:glasspane_broken", "lostruins:glass_broken"]

    random_palettes_variant_always_include = ["glass_side_variant_glass",
                                              "glass_side_variant_bricks"]

    now_its_ruined = ruined_dataclasses.StylesFiveCatGenerator(
        random_palettes_blocks_always_include + random_palettes,
        random_palettes_glass_pane_always_include,
        random_palettes_variant_always_include,
        common_palette_name='lostruins:common_ruined',
        default_palette_name='lostruins:default_ruined'
    )

    # TODO: should this be different? if not, why not just write the same file under both names?
    outside_is_also_ruined = ruined_dataclasses.StylesFiveCatGenerator(
        random_palettes_blocks_always_include + random_palettes,
        random_palettes_glass_pane_always_include,
        random_palettes_variant_always_include,
        common_palette_name='lostruins:common_ruined',
        default_palette_name='lostruins:default_ruined'
    )

    styles_ruined = json.dumps(json.loads(now_its_ruined.to_json()), indent=2)
    styles_outside_ruined = json.dumps(json.loads(outside_is_also_ruined.to_json()), indent=2)

    with open(Path(LR_DATA_OUT_STYLES / f"ruined.json"), 'w') as r:
        r.write(styles_ruined)

    with open(Path(LR_DATA_OUT_STYLES / f"outside_ruined.json"), 'w') as fo:
        fo.write(styles_outside_ruined)

    return ruined_blocks, ruined_block_names


if __name__ == "__main__":
    lots_of_block_types = False
    # TODO: convert to gradle task?
    #       I think no, because that would require running python scripts from grade, and require correct python setup
    #       on top of setting up java/forge/gradle, and the python portion shouldn't be necessary for contributors
    #       not working on the block models & textures

    if lots_of_block_types:
        print(f"BEGINNING RUINATION. Each base texture will generate a number of variants (ruined, cracked, etc")
    else:
        print(f"BEGINNING RUINATION. Block variants (ruined, cracked, chipped) collected in single _ruins block")

    # delete previous built assets & data
    if LR_ASSETS_OUT.exists():
        print(f'removing previous {LR_ASSETS_OUT}')
        shutil.rmtree(LR_ASSETS_OUT)
    if LR_DATA_OUT.exists():
        print(f'removing previous {LR_DATA_OUT}')
        shutil.rmtree(LR_DATA_OUT)
    if REGISTRATION_COPYPASTA.exists():
        print(f'removing previous {REGISTRATION_COPYPASTA}')
        os.remove(REGISTRATION_COPYPASTA)

    # (re)create the build directories
    BLOCK_MODELS_DIR.mkdir(parents=True, exist_ok=True)
    BLOCKSTATES_DIR.mkdir(parents=True, exist_ok=True)
    BLOCK_TEXTURES_DIR.mkdir(parents=True, exist_ok=True)
    LR_DATA_OUT_PALETTES.mkdir(parents=True, exist_ok=True)
    LR_DATA_OUT_STYLES.mkdir(parents=True, exist_ok=True)
    # copy pre-generated assets & data
    print('copying assets_static/* -> built_resources/*')
    shutil.copytree(LR_ASSETS_STATIC, LR_ASSETS_OUT, dirs_exist_ok=True)
    shutil.copytree(LR_DATA_STATIC, LR_DATA_OUT, dirs_exist_ok=True)
    # end

    for dir_name in ["concretes", "roads", 'stones', 'etc']:
        # texture_dir = os.path.join(block_textures_dir, dir_name)
        Path(BLOCK_TEXTURES_DIR / dir_name).mkdir(parents=True, exist_ok=True)

    # begin processing blocks_to_ruin subdirectories
    # lots_of_block_types = True  will greatly increase the number of blocks registered


    concrete_imgs, concrete_variant_names = ruin_blocks(concretes_names, concretes, 'concretes')
    conc_reg, conc_rubble = generate_registrations(sorted(concretes_names), 'concretes',
                                                   reg_all_variants=lots_of_block_types)
    print(f"ruined & rubbled: {concrete_variant_names}")

    stone_imgs, stone_variant_names = ruin_blocks(stones_names, stones, 'stones')
    stone_reg, stone_rubble = generate_registrations(sorted(stones_names), 'stones',
                                                     reg_all_variants=lots_of_block_types)
    print(f"ruined & rubbled: {stone_variant_names}")

    etc_imgs, etc_variant_names = ruin_blocks(etces_names, etces, 'etc')
    etc_reg, etc_rubble = generate_registrations(sorted(etces_names), 'etc',
                                                 reg_all_variants=lots_of_block_types)
    print(f"ruined & rubbled: {etc_variant_names}")

    road_imgs, road_variant_names = ruin_blocks(roads_names, roads, 'roads')
    roads_reg, road_rubble = generate_registrations(sorted(roads_names), 'roads',
                                                    reg_all_variants=lots_of_block_types)
    print(f"ruined & rubbled: {etc_variant_names} ")

    # write the "registration_copypasta.txt" file in built_assets
    with open(REGISTRATION_COPYPASTA, 'w+') as f:
        f.writelines(f"\t\t\t// BEGIN GENERATED REGISTRATION \n")
        f.writelines(f"\t\t\t// concrete blocks \n")
        for item in conc_reg:
            f.writelines(f"{item}")
        f.writelines(f"\n\n\t\t\t// concrete rubble \n")
        for item in conc_rubble:
            f.writelines(f"{item}")

        f.writelines(f"\n\n\t\t\t// stone blocks \n")
        for item in stone_reg:
            f.writelines(f"{item}")

        f.writelines(f"\n\n\t\t\t// stone rubble \n")
        for item in stone_rubble:
            f.writelines(f"{item}")

        f.writelines(f"\n\n\t\t\t// etc blocks \n")
        for item in etc_reg:
            f.writelines(f"{item}")
        f.writelines(f"\n\n\t\t\t// etc rubble \n")
        for item in etc_rubble:
            f.writelines(f"{item}")

        f.writelines(f"\n\n\t\t\t// roads blocks ")
        for item in roads_reg:
            f.writelines(f"{item}")
        f.writelines(f"\n\n\t\t\t// roads rubble \n")
        for item in road_rubble:
            f.writelines(f"{item}")
        f.writelines(f"\n\t\t\t// END GENERATED REGISTRATION \n")

    if SRC_MAIN_ASSETS.exists():
        print(f'removing previously built {SRC_MAIN_ASSETS}')
        shutil.rmtree(SRC_MAIN_ASSETS)
    if SRC_MAIN_DATA.exists():
        print(f'removing previously built {SRC_MAIN_DATA}')
        shutil.rmtree(SRC_MAIN_DATA)

    print(f'copying {LR_ASSETS_OUT} -> {SRC_MAIN_ASSETS}')
    shutil.copytree(LR_ASSETS_OUT, SRC_MAIN_ASSETS, dirs_exist_ok=True)
    print(f'copying {LR_DATA_OUT} -> {SRC_MAIN_DATA}')
    shutil.copytree(LR_DATA_OUT, SRC_MAIN_DATA, dirs_exist_ok=True)

    print("""
    RUINATION complete. 
    Next steps:
     - Manually copy registration_copypasta.txt code block to src/main/java/setup/Registration.java
     - Run gradle build tasks
    """)
