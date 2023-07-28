from string import Template

blockstate_damaged = Template("""
{
"variants": {
    "": [
      {
        "model": "${mod_name}:block/${block_name}_damaged",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_damaged",
        "y": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_damaged1",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_damaged1",
        "y": 180,
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_damaged2",
        "weight": ${common_weight}
      },
      {
        "model": "${mod_name}:block/${block_name}_damaged2",
        "y": 180,
        "weight": ${common_weight}
      }
    ]
}
}

""")