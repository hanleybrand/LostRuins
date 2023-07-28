from string import Template

chipped_block2 = Template("""
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
    "name": "bricks",
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
    "from": [12, 12.5, 0],
    "to": [16, 15, 1],
    "faces": {
        "north": {"uv": [0, 1, 4, 3.5], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 3, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 4], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [14, 7, 0],
    "to": [16, 12.5, 1],
    "faces": {
        "north": {"uv": [0, 3.5, 2, 9], "rotation": 180, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 5, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 4, 16, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [13, 5, 0],
    "to": [16, 7, 1],
    "faces": {
        "north": {"uv": [10, 13, 12, 16], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 2, 3], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 9, 16, 11], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [13, 0, 0],
    "to": [16, 5, 1],
    "faces": {
        "north": {"uv": [11, 13, 16, 16], "rotation": 90, "texture": "#side"},
        "east": {"uv": [12, 2, 7, 4], "rotation": 270, "texture": "#side"},
        "south": {"uv": [9, 4, 14, 7], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 4, 2, 7], "rotation": 270, "texture": "#side"},
        "down": {"uv": [7, 4, 9, 7], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [9, 0, 0],
    "to": [13, 3.5, 1],
    "faces": {
        "north": {"uv": [12, 6, 16, 12], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 5, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 4], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [8, 11.25, 0],
    "to": [12, 15, 1],
    "faces": {
        "north": {"uv": [4, 9, 8, 13], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 8, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [1, 11, 0],
    "to": [5, 15, 1],
    "faces": {
        "north": {"uv": [10, 3, 14, 7], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 5], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [1, 7, 0],
    "to": [3.5, 11, 1],
    "faces": {
        "north": {"uv": [12, 5, 16, 9], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 5, 1, 9], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 5, 4, 9], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 5, 16, 9], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 15, 4, 16], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 4, 1], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [1, 2.5, 0],
    "to": [3, 7, 1],
    "faces": {
        "north": {"uv": [11, 1, 13, 5.5], "rotation": 180, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 10, 4, 14], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 9, 16, 13], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [5, 0, 0],
    "to": [9, 5.5, 1],
    "faces": {
        "north": {"uv": [6, 0, 10, 6], "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 6, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 10, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [5, 12, 0],
    "to": [8, 15, 1],
    "faces": {
        "north": {"uv": [8, 1, 11, 4], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 7, 3], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 8], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [1, 0, 0],
    "to": [5, 2.5, 1],
    "faces": {
        "north": {"uv": [12, 0, 16, 6], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 10, 3, 14], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 13, 16, 16], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [0, 12, 11],
    "to": [1, 15, 15],
    "faces": {
        "north": {"uv": [15, 1, 16, 4], "rotation": 270, "texture": "#side"},
        "east": {"uv": [1, 1, 5, 4], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 1, 1, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [11, 1, 15, 4], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 11, 1, 15], "texture": "#side"},
        "down": {"uv": [0, 1, 1, 5], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 7, 13],
    "to": [1, 12, 15],
    "faces": {
        "north": {"uv": [15, 4, 16, 9], "rotation": 270, "texture": "#side"},
        "east": {"uv": [1, 4, 3, 9], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 4, 1, 9], "rotation": 270, "texture": "#side"},
        "west": {"uv": [13, 4, 15, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 13, 1, 15], "texture": "#side"},
        "down": {"uv": [0, 1, 1, 3], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 5, 12],
    "to": [1, 7, 15],
    "faces": {
        "north": {"uv": [15, 9, 16, 11], "rotation": 270, "texture": "#side"},
        "east": {"uv": [1, 9, 4, 11], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 9, 1, 11], "rotation": 270, "texture": "#side"},
        "west": {"uv": [12, 9, 15, 11], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 12, 1, 15], "texture": "#side"},
        "down": {"uv": [0, 1, 1, 4], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 0, 12],
    "to": [1, 5, 15],
    "faces": {
        "north": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "east": {"uv": [1, 11, 4, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 11, 1, 16], "rotation": 270, "texture": "#side"},
        "west": {"uv": [12, 11, 15, 16], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 12, 1, 15], "texture": "#side"},
        "down": {"uv": [0, 1, 1, 4], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 0, 8],
    "to": [1, 5, 12],
    "faces": {
        "north": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "east": {"uv": [4, 11, 8, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 11, 1, 16], "rotation": 270, "texture": "#side"},
        "west": {"uv": [8, 11, 12, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 8, 1, 12], "texture": "#side"},
        "down": {"uv": [0, 4, 1, 8], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 7, 7],
    "to": [1, 15, 11],
    "faces": {
        "north": {"uv": [15, 1, 16, 9], "rotation": 180, "texture": "#side"},
        "east": {"uv": [5, 1, 9, 9], "rotation": 180, "texture": "#side"},
        "south": {"uv": [0, 1, 1, 9], "rotation": 180, "texture": "#side"},
        "west": {"uv": [7, 7, 11, 15], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 7, 1, 11], "rotation": 180, "texture": "#side"},
        "down": {"uv": [0, 5, 1, 9], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 11, 0],
    "to": [1, 15, 4],
    "faces": {
        "north": {"uv": [15, 1, 16, 5], "rotation": 90, "texture": "#side"},
        "east": {"uv": [12, 1, 16, 5], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 1, 1, 5], "rotation": 270, "texture": "#side"},
        "west": {"uv": [0, 1, 4, 5], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 1, 4], "texture": "#side"},
        "down": {"uv": [0, 12, 1, 16], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 7, 0],
    "to": [1, 11, 3.5],
    "faces": {
        "north": {"uv": [15, 5, 16, 9], "rotation": 270, "texture": "#side"},
        "east": {"uv": [12.5, 5, 16, 9], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 5, 1, 9], "rotation": 270, "texture": "#side"},
        "west": {"uv": [0, 5, 3.5, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 1, 3.5], "texture": "#side"},
        "down": {"uv": [0, 12.5, 1, 16], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 2, 0],
    "to": [1, 7, 3],
    "faces": {
        "north": {"uv": [15, 11, 16, 16], "rotation": 180, "texture": "#side"},
        "east": {"uv": [13, 9, 16, 14], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 9, 1, 14], "rotation": 270, "texture": "#side"},
        "west": {"uv": [0, 9, 3, 14], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 1, 3], "texture": "#side"},
        "down": {"uv": [0, 13, 1, 16], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 4, 4],
    "to": [1, 7, 8],
    "faces": {
        "north": {"uv": [15, 10, 16, 13], "rotation": 270, "texture": "#side"},
        "east": {"uv": [8, 10, 12, 13], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 10, 1, 13], "rotation": 270, "texture": "#side"},
        "west": {"uv": [4, 9, 8, 12], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 4, 1, 8], "texture": "#side"},
        "down": {"uv": [0, 8, 1, 12], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 8, 4],
    "to": [1, 15, 7],
    "faces": {
        "north": {"uv": [15, 1, 16, 8], "rotation": 270, "texture": "#side"},
        "east": {"uv": [9, 1, 12, 8], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 1, 1, 8], "rotation": 270, "texture": "#side"},
        "west": {"uv": [4, 1, 7, 8], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 4, 1, 7], "texture": "#side"},
        "down": {"uv": [0, 9, 1, 12], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [0, 0, 0],
    "to": [1, 2, 8],
    "faces": {
        "north": {"uv": [15, 11, 16, 13], "rotation": 90, "texture": "#side"},
        "east": {"uv": [8, 14, 16, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 14, 1, 16], "rotation": 270, "texture": "#side"},
        "west": {"uv": [0, 14, 8, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 1, 8], "texture": "#side"},
        "down": {"uv": [0, 8, 1, 16], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [11, 12, 15],
    "to": [14.25, 15, 16],
    "faces": {
        "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [11, 1, 14.25, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 4], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [14, 5, 15],
    "to": [15, 7, 16],
    "faces": {
        "north": {"uv": [10, 13, 12, 16], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 2, 3], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 9, 16, 11], "rotation": 270, "texture": "#side"},
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
        "south": {"uv": [9, 4, 14, 7], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 4, 2, 7], "rotation": 270, "texture": "#side"},
        "down": {"uv": [7, 4, 9, 7], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [8, 0, 15],
    "to": [12, 3, 16],
    "faces": {
        "north": {"uv": [12, 6, 16, 12], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 5, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 4], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [7, 7, 15],
    "to": [11, 15, 16],
    "faces": {
        "north": {"uv": [6, 0, 10, 4], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [11, 2, 15, 10], "rotation": 180, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 9], "rotation": 270, "texture": "#side"},
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
        "south": {"uv": [0, 0, 4, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 5], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [0, 7, 15],
    "to": [3, 11, 16],
    "faces": {
        "north": {"uv": [12, 5, 16, 9], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 5, 1, 9], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 5, 3, 9], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 5, 16, 9], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 15, 4, 16], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 4, 1], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [0, 3, 15],
    "to": [4, 7, 16],
    "faces": {
        "north": {"uv": [9, 0, 13, 6], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 10, 4, 14], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 9, 16, 13], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [4, 0, 15],
    "to": [8, 5, 16],
    "faces": {
        "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 6, 4], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 10, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [4, 9, 15],
    "to": [7, 15, 16],
    "faces": {
        "north": {"uv": [6, 0, 10, 6], "rotation": 90, "texture": "#side"},
        "east": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "south": {"uv": [0, 0, 7, 3], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 1, 16, 8], "rotation": 270, "texture": "#side"},
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
        "south": {"uv": [0, 10, 3, 14], "rotation": 270, "texture": "#side"},
        "west": {"uv": [15, 13, 16, 16], "rotation": 180, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 270, "texture": "#side"}
    }
},
{
    "from": [15, 10, 12],
    "to": [16, 15, 16],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [0, 1, 4, 6], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [12, 1, 16, 6], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 7, 14],
    "to": [16, 10, 16],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [0, 6, 2, 9], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 1, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [14, 6, 16, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 5, 12],
    "to": [16, 7, 16],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [0, 9, 4, 11], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [12, 9, 16, 11], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 0, 13],
    "to": [16, 5, 16],
    "faces": {
        "north": {"uv": [7, 4, 2, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [0, 11, 3, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [15, 11, 16, 16], "rotation": 180, "texture": "#side"},
        "west": {"uv": [13, 11, 16, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 4, 2, 7], "texture": "#side"},
        "down": {"uv": [7, 4, 9, 7], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 0, 9],
    "to": [16, 3, 13],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [3, 13, 7, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [9, 13, 13, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 4], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 11, 8],
    "to": [16, 15, 12],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [4, 1, 8, 5], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [8, 1, 12, 5], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 11, 1],
    "to": [16, 15, 5],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [11, 1, 15, 5], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [1, 1, 5, 5], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 7, 1],
    "to": [16, 11, 4],
    "faces": {
        "north": {"uv": [1, 6, 5, 8], "rotation": 270, "texture": "#side"},
        "east": {"uv": [12, 5, 15, 9], "rotation": 90, "texture": "#side"},
        "south": {"uv": [2, 3, 6, 5], "rotation": 270, "texture": "#side"},
        "west": {"uv": [1, 5, 4, 9], "rotation": 270, "texture": "#side"},
        "up": {"uv": [6, 1, 8, 7], "texture": "#side"},
        "down": {"uv": [10, 7, 12, 13], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 3, 1],
    "to": [16, 7, 6],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [10, 9, 15, 13], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [1, 9, 6, 13], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 0, 5],
    "to": [16, 2, 9],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [7, 14, 11, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [5, 14, 9, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [6, 10, 8, 16], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 12, 5],
    "to": [16, 15, 8],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [8, 1, 11, 4], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [5, 1, 8, 4], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "from": [15, 0, 1],
    "to": [16, 3, 5],
    "faces": {
        "north": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "east": {"uv": [11, 13, 15, 16], "rotation": 90, "texture": "#side"},
        "south": {"uv": [0, 0, 4, 2], "rotation": 270, "texture": "#side"},
        "west": {"uv": [1, 13, 5, 16], "rotation": 270, "texture": "#side"},
        "up": {"uv": [0, 0, 2, 6], "texture": "#side"},
        "down": {"uv": [0, 0, 2, 6], "rotation": 180, "texture": "#side"}
    }
},
{
    "name": "top",
    "from": [0, 15, 0],
    "to": [16, 16, 16],
    "faces": {
        "north": {"uv": [0, 0, 16, 1], "texture": "#top"},
        "east": {"uv": [0, 0, 16, 1], "texture": "#top"},
        "south": {"uv": [0, 0, 16, 1], "texture": "#top"},
        "west": {"uv": [0, 0, 16, 1], "texture": "#top"},
        "up": {"uv": [0, 0, 16, 16], "texture": "#top"},
        "down": {"uv": [0, 0, 16, 16], "texture": "#top"}
    }
},
{
    "name": "bottom",
    "from": [1, 0, 1],
    "to": [15, 1, 15],
    "faces": {
        "north": {"uv": [0, 0, 14, 1], "texture": "#bottom"},
        "east": {"uv": [0, 0, 14, 1], "texture": "#bottom"},
        "south": {"uv": [1, 15, 15, 16], "texture": "#bottom"},
        "west": {"uv": [1, 15, 15, 16], "texture": "#bottom"},
        "up": {"uv": [1, 1, 15, 15], "texture": "#bottom"},
        "down": {"uv": [1, 1, 15, 15], "texture": "#bottom"}
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
    "name": "w",
    "origin": [0, 0, 0],
    "color": 0,
    "children": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
},
{
    "name": "s",
    "origin": [0, 0, 0],
    "color": 0,
    "children": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
},
{
    "name": "e",
    "origin": [0, 0, 0],
    "color": 0,
    "children": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
},
48,
49
]
}
""")