from string import Template

big_bricks = Template("""
{
  "variants": {
    "": [
    
      {
        "model": "${mod_name}:block/${block_name}_big_bricks",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks1",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks2",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks3",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks4",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks5",
        "weight": ${common_weight}
      },
   
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked1",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked2",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked3",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked4",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_cracked5",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped1",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped1",
        "y": 90,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped1",
        "y": 180,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped1",
        "y": 270,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped2",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped2",
        "y": 90,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped2",
        "y": 180,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_big_bricks_chipped2",
        "y": 270,
        "uvlock" : "true",
        "weight": ${less_common_weight}
      }
    ]
  }
}

""")
