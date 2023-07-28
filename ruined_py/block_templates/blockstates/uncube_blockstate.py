from string import Template

uncube_blockstate = Template("""
{
  "variants": {
    "": [
    
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}1",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}1",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}2",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}2",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}3",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}3",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}4",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}4",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}5",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}5",
        "y": 90,
        "weight": 1
      },      
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked1",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked1",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked2",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked2",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked3",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked3",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked4",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked4",
        "y": 90,
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked5",
        "weight": 1
      },
      {
        "model": "${mod_name}:block/${block_name}_ruined_${blocktype}_cracked5",
        "y": 90,
        "weight": 1
      }
    ]
  }
}

""")