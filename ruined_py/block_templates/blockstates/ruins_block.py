from string import Template

ruins_blockstate = Template("""
{
  "variants": {
    "": [
    
      {
        "model": "${mod_name}:block/${block_name}",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}",
        "x": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}1",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}1",
        "x": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}2",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}2",
        "x": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}3",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}3",
        "x": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}4",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}4",
        "x": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}5",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}5",
        "x": 180,
        "weight": ${common_weight}
      },      
      {
        "model": "${mod_name}:block/${block_name}_cracked",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked1",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked1",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked2",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked2",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked3",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked3",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked4",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked4",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked5",
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_cracked5",
        "x": 180,
        "weight": ${cracked_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped1",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped1",
        "y": 90,
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped1",
        "y": 180,
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped1",
        "y": 270,
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped2",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped2",
        "y": 90,
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped2",
        "y": 180,
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_chipped2",
        "y": 270,
        "weight": ${less_common_weight}
      }
    ]
  }
}

""")
