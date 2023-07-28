from string import Template

stairs = Template("""
{
  "parent": "minecraft:block/stairs",
  "textures": {
    "bottom": "${mod_name}:block/${bottom_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}"
  }
}
""")

inner_stairs = Template("""
{
  "parent": "minecraft:block/inner_stairs",
  "textures": {
    "bottom": "${mod_name}:block/${bottom_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}"
  }
}
""")

outer_stairs = Template("""
{
  "parent": "minecraft:block/outer_stairs",
  "textures": {
    "bottom": "${mod_name}:block/${bottom_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}"
  }
}
""")
