from string import Template

slab = Template("""
{
  "parent": "minecraft:block/slab",
  "textures": {
    "bottom": "${mod_name}:block/${bottom_texture}",
    "side": "${mod_name}:block/${side_texture}",
    "top": "${mod_name}:block/${top_texture}"
  }
}
""")