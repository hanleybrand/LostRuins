import ruined as rn

# BLOCK_META = {
#     "andesite": {
#         "hex": "595d54",
#         "rgb": (89, 93, 84),
#         "compl_rgb": (166, 162, 171),
#         "compl_block": "beige_tile_ruins",
#         "compl_dist": 20.639767440550294,
#     },
#     "asphalt": {
#         "hex": "515151",
#         "rgb": (81, 81, 81),
#         "compl_rgb": (174, 174, 174),
#         "compl_block": "beige_tile_ruins",
#         "compl_dist": 23.430749027719962,
#     },
#     "asphalt_darker": {
#         "hex": "404040",
#         "rgb": (64, 64, 64),
#         "compl_rgb": (191, 191, 191),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 5.196152422706632,
#     },
#     "basalt_ruins": {
#         "hex": "3a3c40",
#         "rgb": (58, 60, 64),
#         "compl_rgb": (197, 195, 191),
#         "compl_block": "white_granite_pillar_ruins",
#         "compl_dist": 6.0,
#     },
#     "basalt_ruins": {
#         "hex": "3a3c40",
#         "rgb": (58, 60, 64),
#         "compl_rgb": (201, 199, 195),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 12.449899597988733,
#     },
#     "black_concrete": {
#         "hex": "434040",
#         "rgb": (67, 64, 64),
#         "compl_rgb": (188, 191, 191),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 4.242640687119285,
#     },
#     "blackstone": {
#         "hex": "34343c",
#         "rgb": (52, 52, 60),
#         "compl_rgb": (203, 203, 195),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 9.1104335791443,
#     },
#     "blackstone_ruins": {
#         "hex": "34343c",
#         "rgb": (52, 52, 60),
#         "compl_rgb": (203, 203, 195),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 8.06225774829855,
#     },
#     "blue_concrete": {
#         "hex": "555e97",
#         "rgb": (85, 94, 151),
#         "compl_rgb": (170, 161, 104),
#         "compl_block": "sandstone_ruins",
#         "compl_dist": 32.68026927673638,
#     },
#     "blue_tile": {
#         "hex": "0c2122",
#         "rgb": (12, 33, 34),
#         "compl_rgb": (243, 222, 221),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 42.261093218230876,
#     },
#     "beige_tile": {
#         "hex": "ada698",
#         "rgb": (173, 166, 152),
#         "compl_rgb": (82, 89, 103),
#         "compl_block": "plastic_blue_ruins",
#         "compl_dist": 9.433981132056603,
#     },
#     "beige_tile_2": {
#         "hex": "ada698",
#         "rgb": (173, 166, 152),
#         "compl_rgb": (82, 89, 103),
#         "compl_block": "pink_concrete_ruins",
#         "compl_dist": 9.433981132056603,
#     },
#     "brown_concrete": {
#         "hex": "655043",
#         "rgb": (101, 80, 67),
#         "compl_rgb": (154, 175, 188),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 36.40054944640259,
#     },
#     "cobbled_deepslate": {
#         "hex": "3a413f",
#         "rgb": (58, 65, 63),
#         "compl_rgb": (189, 182, 184),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 7.280109889280518,
#     },
#     "cobblestone": {
#         "hex": "797a72",
#         "rgb": (121, 122, 114),
#         "compl_rgb": (134, 133, 141),
#         "compl_block": "light_gray_concrete_ruins",
#         "compl_dist": 7.681145747868608,
#     },
#     "cyan_concrete": {
#         "hex": "4b7a82",
#         "rgb": (75, 122, 130),
#         "compl_rgb": (180, 133, 125),
#         "compl_block": "pink_concrete_ruins",
#         "compl_dist": 22.02271554554524,
#     },
#     "deepslate": {
#         "hex": "3c4240",
#         "rgb": (60, 66, 64),
#         "compl_rgb": (195, 189, 191),
#         "compl_block": "white_granite_pillar_ruins",
#         "compl_dist": 4.47213595499958,
#     },
#     "deepslate_ruins": {
#         "hex": "3c4240",
#         "rgb": (60, 66, 64),
#         "compl_rgb": (195, 189, 191),
#         "compl_block": "white_granite_pillar_ruins",
#         "compl_dist": 4.47213595499958,
#     },
#     "diorite": {
#         "hex": "c0c0b6",
#         "rgb": (192, 192, 182),
#         "compl_rgb": (63, 63, 73),
#         "compl_block": "blue_tile_ruins",
#         "compl_dist": 8.306623862918075,
#     },
#     "dripstone_block": {
#         "hex": "91846d",
#         "rgb": (145, 132, 109),
#         "compl_rgb": (110, 123, 146),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 18.466185312619388,
#     },
#     "gray_concrete": {
#         "hex": "5c5c5c",
#         "rgb": (92, 92, 92),
#         "compl_rgb": (163, 163, 163),
#         "compl_block": "beige_tile_ruins",
#         "compl_dist": 15.165750888103101,
#     },
#     "gray_wood_boards": {
#         "hex": "645e59",
#         "rgb": (100, 94, 89),
#         "compl_rgb": (155, 161, 166),
#         "compl_block": "beige_tile_ruins",
#         "compl_dist": 23.345235059857504,
#     },
#     "gray_wood_planks": {
#         "hex": "423f3d",
#         "rgb": (66, 63, 61),
#         "compl_rgb": (189, 192, 194),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 7.280109889280518,
#     },
#     "gray_wood_planks_nailed": {
#         "hex": "423f3d",
#         "rgb": (66, 63, 61),
#         "compl_rgb": (189, 192, 194),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 7.280109889280518,
#     },
#     "green_concrete": {
#         "hex": "546142",
#         "rgb": (84, 97, 66),
#         "compl_rgb": (171, 158, 189),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 34.49637662132068,
#     },
#     "light_blue_concrete": {
#         "hex": "6d7fa4",
#         "rgb": (109, 127, 164),
#         "compl_rgb": (146, 128, 91),
#         "compl_block": "dripstone_block_ruins",
#         "compl_dist": 18.466185312619388,
#     },
#     "light_gray_concrete": {
#         "hex": "898c8c",
#         "rgb": (137, 140, 140),
#         "compl_rgb": (118, 115, 115),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 7.681145747868608,
#     },
#     "lime_concrete": {
#         "hex": "5b8358",
#         "rgb": (91, 131, 88),
#         "compl_rgb": (164, 124, 167),
#         "compl_block": "magenta_concrete_ruins",
#         "compl_dist": 22.67156809750927,
#     },
#     "magenta_concrete": {
#         "hex": "986b9e",
#         "rgb": (152, 107, 158),
#         "compl_rgb": (103, 148, 97),
#         "compl_block": "lime_concrete_ruins",
#         "compl_dist": 22.67156809750927,
#     },
#     "orange_concrete": {
#         "hex": "a9734a",
#         "rgb": (169, 115, 74),
#         "compl_rgb": (86, 140, 181),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 31.416556144810016,
#     },
#     "pink_concrete": {
#         "hex": "a57785",
#         "rgb": (165, 119, 133),
#         "compl_rgb": (90, 136, 122),
#         "compl_block": "cyan_concrete_ruins",
#         "compl_dist": 22.02271554554524,
#     },
#     "plastic_blue": {
#         "hex": "556163",
#         "rgb": (85, 97, 99),
#         "compl_rgb": (170, 158, 156),
#         "compl_block": "beige_tile_ruins",
#         "compl_dist": 9.433981132056603,
#     },
#     "purple_concrete": {
#         "hex": "6c5086",
#         "rgb": (108, 80, 134),
#         "compl_rgb": (147, 175, 121),
#         "compl_block": "sandstone_ruins",
#         "compl_dist": 30.757112998459398,
#     },
#     "red_concrete": {
#         "hex": "995553",
#         "rgb": (153, 85, 83),
#         "compl_rgb": (102, 170, 172),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 43.32435804486894,
#     },
#     "red_sandstone": {
#         "hex": "9f6c52",
#         "rgb": (159, 108, 82),
#         "compl_rgb": (96, 147, 173),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 25.495097567963924,
#     },
#     "red_sandstone_ruins": {
#         "hex": "96654d",
#         "rgb": (150, 101, 77),
#         "compl_rgb": (105, 154, 178),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 30.675723300355934,
#     },
#     "sandstone": {
#         "hex": "9c9382",
#         "rgb": (156, 147, 130),
#         "compl_rgb": (99, 108, 125),
#         "compl_block": "cyan_concrete_ruins",
#         "compl_dist": 28.231188426986208,
#     },
#     "sandstone_bottom": {
#         "hex": "928a7b",
#         "rgb": (146, 138, 123),
#         "compl_rgb": (109, 117, 132),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 22.20360331117452,
#     },
#     "sandstone_ruins": {
#         "hex": "93897a",
#         "rgb": (147, 137, 122),
#         "compl_rgb": (108, 118, 133),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 23.366642891095847,
#     },
#     "smooth_basalt": {
#         "hex": "303235",
#         "rgb": (48, 50, 53),
#         "compl_rgb": (207, 205, 202),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 3.7416573867739413,
#     },
#     "smooth_stone": {
#         "hex": "878880",
#         "rgb": (135, 136, 128),
#         "compl_rgb": (120, 119, 127),
#         "compl_block": "white_granite_ruins",
#         "compl_dist": 13.379088160259652,
#     },
#     "smooth_stone_slab": {
#         "hex": "86877f",
#         "rgb": (134, 135, 127),
#         "compl_rgb": (121, 120, 128),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 14.142135623730951,
#     },
#     "stone": {
#         "hex": "87877f",
#         "rgb": (135, 135, 127),
#         "compl_rgb": (120, 120, 128),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 14.177446878757825,
#     },
#     "old_stone": {
#         "hex": "87877f",
#         "rgb": (135, 135, 127),
#         "compl_rgb": (120, 120, 128),
#         "compl_block": "cobblestone_ruins",
#         "compl_dist": 14.177446878757825,
#     },
#     "tile_irregular": {
#         "hex": "43464b",
#         "rgb": (67, 70, 75),
#         "compl_rgb": (188, 185, 180),
#         "compl_block": "diorite_ruins",
#         "compl_dist": 8.306623862918075,
#     },
#     "tile_pattern": {
#         "hex": "453931",
#         "rgb": (69, 57, 49),
#         "compl_rgb": (186, 198, 206),
#         "compl_block": "white_concrete_ruins",
#         "compl_dist": 20.688160865577203,
#     },
#     "tuff": {
#         "hex": "b59e88",
#         "rgb": (181, 158, 136),
#         "compl_rgb": (74, 97, 119),
#         "compl_block": "plastic_blue_ruins",
#         "compl_dist": 22.825424421026653,
#     },
#     "white_granite": {
#         "hex": "cecac5",
#         "rgb": (206, 202, 197),
#         "compl_rgb": (45, 49, 55),
#         "compl_block": "smooth_basalt_ruins",
#         "compl_dist": 3.7416573867739413,
#     },
#     "white_concrete": {
#         "hex": "bcbcbc",
#         "rgb": (188, 188, 188),
#         "compl_rgb": (67, 67, 67),
#         "compl_block": "black_concrete_ruins",
#         "compl_dist": 4.242640687119285,
#     },
#     "white_granite_pillar": {
#         "hex": "c3bfbb",
#         "rgb": (195, 191, 187),
#         "compl_rgb": (60, 64, 68),
#         "compl_block": "deepslate_ruins",
#         "compl_dist": 4.47213595499958,
#     },
#     "yellow_concrete": {
#         "hex": "9a9140",
#         "rgb": (154, 145, 64),
#         "compl_rgb": (101, 110, 191),
#         "compl_block": "light_blue_concrete_ruins",
#         "compl_dist": 32.87856444554719,
#     },
# }


BLOCK_META = {
    "andesite": {
        'hex': '595d54',
        'rgb': (89, 93, 84),
        'compl_rgb': (166, 162, 171),
        'compl_block': 'beige_tile',
        'compl_dist': 20.639767440550294
    },
    "asphalt": {
        'hex': '515151',
        'rgb': (81, 81, 81),
        'compl_rgb': (174, 174, 174),
        'compl_block': 'beige_tile',
        'compl_dist': 23.430749027719962},
    "asphalt_darker": {
        'hex': '404040',
        'rgb': (64, 64, 64),
        'compl_rgb': (191, 191, 191),
        'compl_block': 'white_concrete',
        'compl_dist': 5.196152422706632},
    "beige_tile": {
        'hex': 'ada698',
        'rgb': (173, 166, 152),
        'compl_rgb': (82, 89, 103),
        'compl_block': 'plastic_blue',
        'compl_dist': 9.433981132056603},
    "beige_tile_2": {
        'hex': 'ada698',
        'rgb': (173, 166, 152),
        'compl_rgb': (82, 89, 103),
        'compl_block': 'plastic_blue',
        'compl_dist': 9.433981132056603},
    "black_concrete": {
        'hex': '434040',
        'rgb': (67, 64, 64),
        'compl_rgb': (188, 191, 191),
        'compl_block': 'white_concrete',
        'compl_dist': 4.242640687119285},
    "blackstone": {
        'hex': '34343c',
        'rgb': (52, 52, 60),
        'compl_rgb': (203, 203, 195),
        'compl_block': 'white_granite',
        'compl_dist': 9.1104335791443},
    "blue_tile": {
        'hex': '0c2122',
        'rgb': (12, 33, 34),
        'compl_rgb': (243, 222, 221),
        'compl_block': 'white_granite',
        'compl_dist': 42.261093218230876},
    "brown_concrete": {
        'hex': '655043',
        'rgb': (101, 80, 67),
        'compl_rgb': (154, 175, 188),
        'compl_block': 'white_concrete',
        'compl_dist': 36.40054944640259},
    "cobbled_deepslate": {
        'hex': '424947',
        'rgb': (66, 73, 71),
        'compl_rgb': (189, 182, 184),
        'compl_block': 'white_concrete',
        'compl_dist': 7.280109889280518},
    "cobblestone": {
        'hex': '797a72',
        'rgb': (121, 122, 114),
        'compl_rgb': (134, 133, 141),
        'compl_block': 'light_gray_concrete',
        'compl_dist': 7.681145747868608},
    "deepslate": {
        'hex': '3c4240',
        'rgb': (60, 66, 64),
        'compl_rgb': (195, 189, 191),
        'compl_block': 'white_granite_pillar',
        'compl_dist': 4.47213595499958},
    "diorite": {
        'hex': 'c0c0b6',
        'rgb': (192, 192, 182),
        'compl_rgb': (63, 63, 73),
        'compl_block': 'tile_irregular',
        'compl_dist': 8.306623862918075},
    "dripstone_block": {
        'hex': '91846d',
        'rgb': (145, 132, 109),
        'compl_rgb': (110, 123, 146),
        'compl_block': 'light_gray_concrete',
        'compl_dist': 32.46536616149585},
    "gray_concrete": {
        'hex': '5c5c5c',
        'rgb': (92, 92, 92),
        'compl_rgb': (163, 163, 163),
        'compl_block': 'beige_tile',
        'compl_dist': 15.165750888103101},
    "gray_wood_boards": {
        'hex': '626261',
        'rgb': (98, 98, 97),
        'compl_rgb': (157, 157, 158),
        'compl_block': 'beige_tile',
        'compl_dist': 19.313207915827967},
    "gray_wood_planks": {
        'hex': '423f3d',
        'rgb': (66, 63, 61),
        'compl_rgb': (189, 192, 194),
        'compl_block': 'white_concrete',
        'compl_dist': 7.280109889280518},
    "gray_wood_planks_nailed": {
        'hex': '5f5e5d',
        'rgb': (95, 94, 93),
        'compl_rgb': (160, 161, 162),
        'compl_block': 'beige_tile',
        'compl_dist': 17.146428199482248},
    "light_gray_concrete": {
        'hex': '898c8c',
        'rgb': (137, 140, 140),
        'compl_rgb': (118, 115, 115),
        'compl_block': 'cobblestone',
        'compl_dist': 7.681145747868608},
    "old_stone": {
        'hex': '87877f',
        'rgb': (135, 135, 127),
        'compl_rgb': (120, 120, 128),
        'compl_block': 'cobblestone',
        'compl_dist': 14.177446878757825},
    "plastic_blue": {
        'hex': '556163',
        'rgb': (85, 97, 99),
        'compl_rgb': (170, 158, 156),
        'compl_block': 'beige_tile',
        'compl_dist': 9.433981132056603},
    "red_sandstone": {
        'hex': '9f6c52',
        'rgb': (159, 108, 82),
        'compl_rgb': (96, 147, 173),
        'compl_block': 'light_gray_concrete',
        'compl_dist': 53.094255809833136},
    "sandstone": {
        'hex': '9c9382',
        'rgb': (156, 147, 130),
        'compl_rgb': (99, 108, 125),
        'compl_block': 'cobblestone',
        'compl_dist': 28.30194339616981},
    "smooth_basalt": {
        'hex': '303235',
        'rgb': (48, 50, 53),
        'compl_rgb': (207, 205, 202),
        'compl_block': 'white_granite',
        'compl_dist': 3.7416573867739413},
    "smooth_stone": {
        'hex': '878880',
        'rgb': (135, 136, 128),
        'compl_rgb': (120, 119, 127),
        'compl_block': 'cobblestone',
        'compl_dist': 13.379088160259652},
    "tile_irregular": {
        'hex': '43464b',
        'rgb': (67, 70, 75),
        'compl_rgb': (188, 185, 180),
        'compl_block': 'diorite',
        'compl_dist': 8.306623862918075},
    "tile_pattern": {
        'hex': '453931',
        'rgb': (69, 57, 49),
        'compl_rgb': (186, 198, 206),
        'compl_block': 'white_concrete',
        'compl_dist': 20.688160865577203},
    "tuff": {
        'hex': 'b59e88',
        'rgb': (181, 158, 136),
        'compl_rgb': (74, 97, 119),
        'compl_block': 'plastic_blue',
        'compl_dist': 22.825424421026653},
    "white_concrete": {
        'hex': 'bcbcbc',
        'rgb': (188, 188, 188),
        'compl_rgb': (67, 67, 67),
        'compl_block': 'black_concrete',
        'compl_dist': 4.242640687119285},
    "white_granite": {
        'hex': 'd2cec8',
        'rgb': (210, 206, 200),
        'compl_rgb': (49, 53, 58),
        'compl_block': 'blackstone',
        'compl_dist': 3.7416573867739413},
    "white_granite_pillar": {
        'hex': 'c3bfbb',
        'rgb': (195, 191, 187),
        'compl_rgb': (60, 64, 68),
        'compl_block': 'deepslate',
        'compl_dist': 4.47213595499958}
}


def get_complimentary_block(block_id, lookup_dict=None):
    if not lookup_dict:
        lookup_dict = BLOCK_META
    if ':' in block_id:
        block_id = block_id.split(':')[1]
    compliment_block = BLOCK_META[block_id]['compl_block']
    return rn.full_block_id(compliment_block)
