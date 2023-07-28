import os
import json
from string import Template


def stair_blockstate_gen(block_name):
    block_states = None
    file_ends = [numb if numb > 0 else "" for numb in range(6)]

    output = {"variants": {}}

    with open('stairs.json', 'r') as f:
        block_states = json.load(f)

    for k, v in block_states['variants'].items():
        output["variants"][k] = []
        mdl = Template(v['model'])
        print(k)
        for numb in range(6):
            v_out = None
            end = file_ends[numb]
            model = mdl.substitute(block_name=f"{block_name}_", n=f"{end}")
            v.update({"model": mdl.substitute(block_name=f"{block_name}_", n=f"{end}")})
            # important - if you keep appending v, each item in the list will become the
            # current value of v because you're copying v not the contents
            # this is solved by appending a copy of v, i.e. dict(v)
            output["variants"][k].append(dict(v))
            print(output["variants"][k])

        # output["variants"][k] = variant_list
        print(f"end  {k}")
        print(output["variants"][k])

    return json.dumps(output, indent=4)


if __name__ == "__main__":
    bn = 'black_concrete_ruined'
    the_file = stair_blockstate_gen(bn)
    # print(stair_blockstate_gen(bn))
