from string import Template

damaged_block = Template("""
{
"credit": "Made by Hanleybrand using BlockBench",
"parent": "minecraft:block/cube_all",
"textures": {
    "0": "${mod_name}:block/${texture_name}",
    "1": "minecraft:block/iron_bars",
    "particle": "${mod_name}:block/${texture_name}"
},
"elements": [
    {
        "from": [0, 0, 0],
        "to": [4, 10, 4],
        "faces": {
            "north": {"uv": [12, 6, 16, 16], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 6, 4, 16], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [4, 0, 0],
        "to": [8, 9.5, 4],
        "faces": {
            "north": {"uv": [8, 6.5, 12, 16], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [8, 0, 0],
        "to": [12, 10.5, 4],
        "faces": {
            "north": {"uv": [4, 5, 8, 16], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [12, 0, 0],
        "to": [16, 9.75, 4],
        "faces": {
            "north": {"uv": [0, 6.25, 4, 16], "texture": "#0"},
            "east": {"uv": [12, 6.25, 16, 16], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [12, 0, 4],
        "to": [16, 9, 8],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [8, 7, 12, 16], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [0, 0, 4],
        "to": [4, 9, 8],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [4, 7, 8, 16], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [12, 0, 8],
        "to": [16, 10.5, 12],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [4, 5.5, 8, 16], "texture": "#0"},
            "south": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [0, 0, 8],
        "to": [4, 9.5, 12],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 6.5, 4, 16], "texture": "#0"},
            "west": {"uv": [8, 6.5, 12, 16], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [8, 0, 8],
        "to": [12, 12.5, 12],
        "faces": {
            "north": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "east": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "south": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "west": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "up": {"uv": [8, 8, 12, 12], "texture": "#0"},
            "down": {"uv": [8, 4, 12, 8], "texture": "#0"}
        }
    },
    {
        "from": [4, 0, 8],
        "to": [8, 11.25, 12],
        "faces": {
            "north": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "east": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "south": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "west": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "up": {"uv": [4, 8, 8, 12], "texture": "#0"},
            "down": {"uv": [8, 4, 12, 8], "texture": "#0"}
        }
    },
    {
        "from": [4, 0, 4],
        "to": [8, 12, 8],
        "faces": {
            "north": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "east": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "south": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "west": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "up": {"uv": [4, 4, 8, 8], "texture": "#0"},
            "down": {"uv": [8, 4, 12, 8], "texture": "#0"}
        }
    },
    {
        "from": [8, 0, 4],
        "to": [12, 11, 8],
        "faces": {
            "north": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "east": {"uv": [4, 3, 8, 16], "texture": "#0"},
            "south": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "west": {"uv": [8, 3, 12, 16], "texture": "#0"},
            "up": {"uv": [8, 8, 12, 12], "texture": "#0"},
            "down": {"uv": [8, 4, 12, 8], "texture": "#0"}
        }
    },
    {
        "from": [12, 0, 12],
        "to": [16, 6.5, 16],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 9.5, 4, 16], "texture": "#0"},
            "south": {"uv": [12, 9.5, 16, 16], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [0, 0, 12],
        "to": [4, 7.5, 16],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [0, 8.5, 4, 16], "texture": "#0"},
            "west": {"uv": [12, 8.5, 16, 16], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [4, 0, 12],
        "to": [8, 9.75, 16],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "south": {"uv": [4, 6.25, 8, 16], "texture": "#0"},
            "west": {"uv": [12, 6.25, 16, 16], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [8, 0, 12],
        "to": [12, 9.25, 16],
        "faces": {
            "north": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "east": {"uv": [0, 6.75, 4, 16], "texture": "#0"},
            "south": {"uv": [8, 5.75, 12, 16], "texture": "#0"},
            "west": {"uv": [0, 0, 3, 2], "texture": "#0"},
            "up": {"uv": [0, 0, 4, 4], "texture": "#0"},
            "down": {"uv": [0, 0, 3, 3], "texture": "#0"}
        }
    },
    {
        "from": [5.5, 0, 5.5],
        "to": [6.5, 16, 6.5],
        "faces": {
            "north": {"uv": [3, 1, 4, 15], "texture": "#1"},
            "east": {"uv": [8, 1, 9, 15], "texture": "#1"},
            "south": {"uv": [7, 1, 8, 15], "texture": "#1"},
            "west": {"uv": [4, 1, 5, 15], "texture": "#1"},
            "up": {"uv": [0, 0, 1, 1], "texture": "#1"},
            "down": {"uv": [0, 0, 1, 1], "texture": "#1"}
        }
    },
    {
        "from": [9.5, 0, 9.5],
        "to": [10.5, 15, 10.5],
        "faces": {
            "north": {"uv": [3, 1, 4, 15], "texture": "#1"},
            "east": {"uv": [8, 1, 9, 15], "texture": "#1"},
            "south": {"uv": [7, 1, 8, 15], "texture": "#1"},
            "west": {"uv": [4, 1, 5, 15], "texture": "#1"},
            "up": {"uv": [0, 0, 1, 1], "texture": "#1"},
            "down": {"uv": [0, 0, 1, 1], "texture": "#1"}
        }
    },
    {
        "from": [5.5, 4, 4.5],
        "to": [6.5, 20, 5.5],
        "rotation": {"angle": 22.5, "axis": "x", "origin": [0, 0, 0]},
        "faces": {
            "north": {"uv": [7, 1, 8, 15], "texture": "#1"},
            "east": {"uv": [4, 1, 5, 15], "texture": "#1"},
            "south": {"uv": [8, 1, 9, 15], "texture": "#1"},
            "west": {"uv": [3, 1, 4, 15], "texture": "#1"},
            "up": {"uv": [0, 0, 1, 1], "texture": "#1"},
            "down": {"uv": [0, 0, 1, 1], "texture": "#1"}
        }
    },
    {
        "from": [4.5, 11, 5.5],
        "to": [5.5, 18, 6.5],
        "rotation": {"angle": -22.5, "axis": "z", "origin": [0, 0, 0]},
        "faces": {
            "north": {"uv": [0, 1, 1, 8], "texture": "#1"},
            "east": {"uv": [0, 1, 1, 8], "texture": "#1"},
            "south": {"uv": [0, 1, 1, 8], "texture": "#1"},
            "west": {"uv": [0, 2, 1, 9], "texture": "#1"},
            "up": {"uv": [0, 1, 1, 2], "texture": "#1"},
            "down": {"uv": [0, 1, 1, 2], "texture": "#1"}
        }
    }
],
"groups": [
        {
            "name": "block",
            "origin": [0, 0, 0],
            "color": 0,
            "children": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        },
        {
            "name": "rebar",
            "origin": [8, 8, 8],
            "color": 0,
            "children": [16, 17, 18, 19]
        }
    ]
}
""")