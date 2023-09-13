from string import Template

chipped_block1_simple = Template("""
{
"credit": "Made by Hanleybrand with Blockbench",
"parent": "lostruins:block/chipped1",
"textures": {
    "0": "block/bricks",
    "particle": "${mod_name}:block/${side_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}",
    "bottom": "${mod_name}:block/${bottom_texture}"
}
}
""")

chipped_block1 = Template("""
{
"credit": "Made with Blockbench",
"parent": "minecraft:block/cube_all",
"textures": {
    "0": "block/bricks",
    "particle": "${mod_name}:block/${side_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}",
    "bottom": "${mod_name}:block/${bottom_texture}"
},
"elements": [
    {
        "from": [1, 1, 1],
        "to": [15, 15, 15],
        "faces": {
            "north": {"uv": [1, 1, 15, 15], "texture": "#0"},
            "east": {"uv": [1, 1, 15, 15], "texture": "#0"},
            "south": {"uv": [1, 1, 15, 15], "texture": "#0"},
            "west": {"uv": [1, 1, 15, 15], "texture": "#0"},
            "up": {"uv": [1, 1, 15, 15], "texture": "#0"},
            "down": {"uv": [1, 1, 15, 15], "texture": "#0"}
        }
    },
    {
        "from": [13, 0, 0],
        "to": [16, 4, 1],
        "faces": {
            "north": {"uv": [0, 12, 3, 16], "texture": "#side"},
            "east": {"uv": [15, 12, 16, 16], "texture": "#side"},
            "south": {"uv": [13, 12, 16, 16], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [13, 15, 16, 16], "texture": "#bottom"}
        }
    },
    {
        "from": [8, 0, 0],
        "to": [13, 3, 1],
        "faces": {
            "north": {"uv": [3, 13, 8, 16], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "south": {"uv": [8, 13, 13, 16], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [8, 15, 13, 16], "texture": "#bottom"}
        }
    },
    {
        "from": [6, 0, 0],
        "to": [8, 3, 1],
        "faces": {
            "north": {"uv": [8, 13, 10, 16], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "south": {"uv": [6, 13, 8, 16], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [6, 15, 8, 16], "texture": "#bottom"}
        }
    },
    {
        "from": [1, 0, 0],
        "to": [6, 3, 1],
        "faces": {
            "north": {"uv": [10, 13, 15, 16], "texture": "#side"},
            "east": {"uv": [0, 4, 2, 7], "texture": "#side"},
            "south": {"uv": [1, 13, 6, 16], "texture": "#side"},
            "west": {"uv": [7, 4, 9, 7], "texture": "#side"},
            "up": {"uv": [7, 4, 2, 2], "texture": "#side"},
            "down": {"uv": [1, 15, 6, 16], "texture": "#bottom"}
        }
    },
    {
        "from": [1, 3, 0],
        "to": [9, 7, 1],
        "faces": {
            "north": {"uv": [7, 9, 15, 13], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 4], "texture": "#side"},
            "south": {"uv": [1, 9, 9, 13], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [10, 4, 0],
        "to": [16, 8, 1],
        "faces": {
            "north": {"uv": [0, 8, 6, 12], "texture": "#side"},
            "east": {"uv": [15, 8, 16, 12], "texture": "#side"},
            "south": {"uv": [10, 8, 16, 12], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [12, 11, 0],
        "to": [16, 15, 1],
        "faces": {
            "north": {"uv": [0, 1, 4, 5], "texture": "#side"},
            "east": {"uv": [15, 1, 16, 5], "texture": "#side"},
            "south": {"uv": [12, 1, 16, 5], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [8, 8, 0],
        "to": [12, 15, 1],
        "faces": {
            "north": {"uv": [4, 1, 8, 8], "texture": "#side"},
            "east": {"uv": [6, 1, 8, 7], "texture": "#side"},
            "south": {"uv": [8, 1, 12, 8], "texture": "#side"},
            "west": {"uv": [10, 7, 12, 13], "texture": "#side"},
            "up": {"uv": [1, 6, 5, 8], "texture": "#side"},
            "down": {"uv": [2, 3, 6, 5], "texture": "#side"}
        }
    },
    {
        "from": [4, 9, 0],
        "to": [8, 15, 1],
        "faces": {
            "north": {"uv": [8, 1, 12, 7], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "south": {"uv": [4, 1, 8, 7], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [1, 7, 0],
        "to": [4, 12, 1],
        "faces": {
            "north": {"uv": [12, 4, 15, 9], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "south": {"uv": [1, 4, 4, 9], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [12, 8, 0],
        "to": [16, 11, 1],
        "faces": {
            "north": {"uv": [0, 5, 4, 8], "texture": "#side"},
            "east": {"uv": [15, 5, 16, 8], "texture": "#side"},
            "south": {"uv": [12, 5, 16, 8], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [1, 12, 0],
        "to": [4, 15, 1],
        "faces": {
            "north": {"uv": [12, 1, 15, 4], "texture": "#side"},
            "east": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "south": {"uv": [1, 1, 4, 4], "texture": "#side"},
            "west": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 4, 2], "texture": "#side"},
            "down": {"uv": [0, 0, 4, 2], "texture": "#side"}
        }
    },
    {
        "from": [11, 12, 15],
        "to": [15, 15, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [11, 1, 15, 4], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [13, 7, 15],
        "to": [15, 12, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [13, 4, 15, 9], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [12, 5, 15],
        "to": [15, 7, 16],
        "faces": {
            "north": {"uv": [10, 13, 12, 16], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [12, 9, 15, 11], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [12, 0, 15],
        "to": [15, 5, 16],
        "faces": {
            "north": {"uv": [11, 13, 16, 16], "rotation": 90, "texture": "#side"},
            "east": {"uv": [12, 2, 7, 4], "rotation": 270, "texture": "#side"},
            "south": {"uv": [12, 11, 15, 16], "texture": "#side"},
            "west": {"uv": [7, 4, 2, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 4, 2, 7], "rotation": 270, "texture": "#side"},
            "down": {"uv": [12, 0, 15, 1], "texture": "#bottom"}
        }
    },
    {
        "from": [8, 0, 15],
        "to": [12, 5, 16],
        "faces": {
            "north": {"uv": [12, 6, 16, 12], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [8, 11, 12, 16], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 4], "rotation": 270, "texture": "#side"},
            "down": {"uv": [8, 0, 12, 1], "texture": "#bottom"}
        }
    },
    {
        "from": [7, 7, 15],
        "to": [11, 15, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 4], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [7, 1, 11, 9], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [0, 11, 15],
        "to": [4, 15, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [0, 1, 4, 5], "texture": "#side"},
            "west": {"uv": [15, 1, 16, 5], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [0, 7, 15],
        "to": [4, 11, 16],
        "faces": {
            "north": {"uv": [2, 0, 6, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [2, 3, 6, 5], "rotation": 270, "texture": "#side"},
            "south": {"uv": [0, 5, 4, 9], "texture": "#side"},
            "west": {"uv": [15, 5, 16, 9], "texture": "#side"},
            "up": {"uv": [6, 1, 8, 7], "rotation": 270, "texture": "#side"},
            "down": {"uv": [10, 7, 12, 13], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [0, 3, 15],
        "to": [4, 7, 16],
        "faces": {
            "north": {"uv": [9, 0, 13, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [0, 9, 4, 13], "texture": "#side"},
            "west": {"uv": [15, 9, 16, 13], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [4, 0, 15],
        "to": [8, 6, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [4, 10, 8, 16], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [2, 0, 8, 1], "texture": "#bottom"}
        }
    },
    {
        "from": [4, 8, 15],
        "to": [7, 15, 16],
        "faces": {
            "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [4, 1, 7, 8], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
        }
    },
    {
        "from": [0, 0, 15],
        "to": [4, 3, 16],
        "faces": {
            "north": {"uv": [12, 0, 16, 6], "rotation": 90, "texture": "#side"},
            "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "south": {"uv": [0, 13, 4, 16], "texture": "#side"},
            "west": {"uv": [15, 13, 16, 16], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
            "down": {"uv": [0, 0, 4, 1], "texture": "#bottom"}
        }
    },
    {
        "from": [0, 11, 11],
        "to": [1, 15, 15],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [11, 1, 15, 5], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 7, 13],
        "to": [1, 9, 15],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [13, 7, 15, 9], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 5, 11],
        "to": [1, 7, 15],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [10, 13, 12, 16], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [11, 9, 15, 11], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 0, 12],
        "to": [1, 5, 15],
        "faces": {
            "north": {"uv": [7, 4, 2, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [11, 13, 16, 16], "rotation": 90, "texture": "#side"},
            "south": {"uv": [12, 2, 7, 4], "rotation": 270, "texture": "#side"},
            "west": {"uv": [12, 11, 15, 16], "texture": "#side"},
            "up": {"uv": [0, 4, 2, 7], "texture": "#side"},
            "down": {"uv": [0, 1, 1, 4], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [0, 0, 8],
        "to": [1, 3, 12],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [12, 6, 16, 12], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [8, 13, 12, 16], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 4], "texture": "#side"},
            "down": {"uv": [0, 4, 1, 8], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [0, 9, 7],
        "to": [1, 15, 11],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [6, 0, 10, 4], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [7, 1, 11, 7], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 12, 0],
        "to": [1, 15, 4],
        "faces": {
            "north": {"uv": [15, 1, 16, 4], "texture": "#side"},
            "east": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 1, 4, 4], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 9, 0],
        "to": [1, 12, 3],
        "faces": {
            "north": {"uv": [15, 4, 16, 7], "texture": "#side"},
            "east": {"uv": [2, 0, 6, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [2, 3, 6, 5], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 4, 3, 7], "texture": "#side"},
            "up": {"uv": [6, 1, 8, 7], "texture": "#side"},
            "down": {"uv": [10, 7, 12, 13], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 3, 0],
        "to": [1, 9, 8],
        "faces": {
            "north": {"uv": [15, 7, 16, 13], "texture": "#side"},
            "east": {"uv": [9, 0, 13, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 7, 8, 13], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 0, 4],
        "to": [1, 3, 8],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [4, 13, 8, 16], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 8, 1, 12], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [0, 10, 4],
        "to": [1, 15, 7],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [4, 1, 7, 6], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [0, 0, 0],
        "to": [1, 3, 4],
        "faces": {
            "north": {"uv": [15, 13, 16, 16], "texture": "#side"},
            "east": {"uv": [12, 0, 16, 6], "rotation": 90, "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 13, 4, 16], "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 12, 1, 16], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [15, 10, 12],
        "to": [16, 15, 16],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [0, 1, 4, 6], "texture": "#side"},
            "south": {"uv": [15, 1, 16, 6], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 6], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 7, 14],
        "to": [16, 10, 16],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [0, 6, 2, 9], "texture": "#side"},
            "south": {"uv": [15, 6, 16, 9], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 6], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 5, 12],
        "to": [16, 7, 16],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [0, 9, 4, 11], "texture": "#side"},
            "south": {"uv": [15, 9, 16, 11], "texture": "#side"},
            "west": {"uv": [0, 0, 4, 6], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 0, 13],
        "to": [16, 5, 16],
        "faces": {
            "north": {"uv": [7, 4, 2, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [0, 11, 3, 16], "texture": "#side"},
            "south": {"uv": [15, 11, 16, 16], "texture": "#side"},
            "west": {"uv": [11, 13, 16, 16], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 4, 2, 7], "texture": "#side"},
            "down": {"uv": [15, 0, 16, 3], "texture": "#bottom"}
        }
    },
    {
        "from": [15, 0, 9],
        "to": [16, 3, 13],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [3, 13, 7, 16], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [8, 10, 12, 16], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 4], "texture": "#side"},
            "down": {"uv": [15, 3, 16, 7], "texture": "#bottom"}
        }
    },
    {
        "from": [15, 11, 8],
        "to": [16, 15, 12],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [4, 1, 8, 5], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 0, 4, 6], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 11, 1],
        "to": [16, 15, 5],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [11, 1, 15, 5], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 1, 4, 7], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 7, 1],
        "to": [16, 11, 4],
        "faces": {
            "north": {"uv": [1, 6, 5, 8], "rotation": 270, "texture": "#side"},
            "east": {"uv": [12, 5, 15, 9], "texture": "#side"},
            "south": {"uv": [2, 3, 6, 5], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 4, 4, 10], "rotation": 270, "texture": "#side"},
            "up": {"uv": [6, 1, 8, 7], "texture": "#side"},
            "down": {"uv": [10, 7, 12, 13], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 3, 1],
        "to": [16, 7, 6],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [10, 9, 15, 13], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 10, 4, 15], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 0, 5],
        "to": [16, 2, 9],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [7, 14, 11, 16], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 0, 2, 4], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [15, 7, 16, 11], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [15, 12, 5],
        "to": [16, 15, 8],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [8, 1, 11, 4], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 0, 2, 3], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
        }
    },
    {
        "from": [15, 0, 1],
        "to": [16, 3, 5],
        "faces": {
            "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "east": {"uv": [11, 13, 15, 16], "texture": "#side"},
            "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
            "west": {"uv": [0, 0, 4, 6], "rotation": 270, "texture": "#side"},
            "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
            "down": {"uv": [15, 11, 16, 15], "rotation": 180, "texture": "#bottom"}
        }
    },
    {
        "from": [0, 15, 0],
        "to": [16, 16, 16],
        "faces": {
            "north": {"uv": [0, 0, 16, 1], "texture": "#side"},
            "east": {"uv": [0, 0, 16, 1], "texture": "#side"},
            "south": {"uv": [0, 0, 16, 1], "texture": "#side"},
            "west": {"uv": [0, 0, 16, 1], "texture": "#side"},
            "up": {"uv": [0, 0, 16, 16], "texture": "#top"},
            "down": {"uv": [0, 0, 16, 16], "texture": "#side"}
        }
    },
    {
        "from": [1, 0, 1],
        "to": [15, 1, 15],
        "faces": {
            "north": {"uv": [0, 0, 14, 1], "texture": "#bottom"},
            "east": {"uv": [0, 0, 14, 1], "texture": "#bottom"},
            "south": {"uv": [1, 15, 15, 16], "texture": "#bottom"},
            "west": {"uv": [1, 0, 15, 1], "texture": "#bottom"},
            "up": {"uv": [1, 1, 15, 15], "texture": "#bottom"},
            "down": {"uv": [1, 1, 15, 15], "rotation": 90, "texture": "#bottom"}
        }
    }
],
"groups": [
    0,
    {
        "name": "n",
        "origin": [0, 0, 0],
        "color": 0,
        "children": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    {
        "name": "s",
        "origin": [0, 0, 0],
        "color": 0,
        "children": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    },
    {
        "name": "e",
        "origin": [0, 0, 0],
        "color": 0,
        "children": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    },
    {
        "name": "w",
        "origin": [0, 0, 0],
        "color": 0,
        "children": [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    },
    {
        "name": "u",
        "origin": [0, 0, 0],
        "color": 0,
        "children": [49, 50]
    }
]
}
""")