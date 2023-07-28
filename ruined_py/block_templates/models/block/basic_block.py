from string import Template

basic_block = Template("""
{
  "parent": "minecraft:block/cube_all",
  "textures": {
    "all": "${mod_name}:block/${texture_name}"
  }
}
""")