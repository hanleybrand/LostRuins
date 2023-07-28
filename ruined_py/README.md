# ruined_py
### ruins your textures and loses them in your ruins

From a small group of base textures, generate dirty/ruined & cracked (optional) 
& brick (optional) variant textures that are packed into ruins blocks that create a 
believable look for old, abandoned buildings.

### License notes

This sub-repository (ruined_py) draws on base images (in the blocks_to_ruin subdirectory) from the texture pack
[Isabella II by Bonemouse](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/resource-packs/1226573-16x-1-5-isabella-ii-1-5v2-i-got-yer-redstone-here) 
which has been kept alive since Minecraft 1.5 by a number of talented and wonderful people, most recently [yurisuka](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/resource-packs/resource-pack-discussion/2745599-isabella-status-thread-updated-4-june-2021),
and previously by [Gnomeo](https://www.minecraftforum.net/linkout?remoteUrl=https%253a%252f%252fgithub.com%252fGnomeo%252fModded_Isabella), 
[ScottKillen](https://github.com/ScottKillen/Isabella-II-FTB), and many other dedicated fans of the pack. 
Reuse of textures from the pack is covered by the creative commons Attribution 3.0 Unported (CC BY 3.0) license. 

Images in the /res16 subdirectory (and possibly a few in blocks_to_ruin) are created or modified by hanleybrand, those images are 
also released under the same creative commons Attribution 3.0 Unported (CC BY 3.0) license -- any images by MCJty originating from the original 
LostRuins repo are covered by the MIT License that LostRuins is distributed with, if I understand how it works (spoiler alert: I don't)

## Setup

The libraries required can probably be installed via ```$ pip install -f requirements.txt```, 
but as there are sometimes issues with some of the scientific libraries like numpy, it's likely easier to 
[install conda](https://www.anaconda.com/download#downloads) first if it's not installed already,
and then create a virtual environment with the following command in this directory

```bash
$ conda create --name lostruins_py --file requirements.txt
# ... follow prompts ...
$ conda activate lostruins_py
```
or 
```bash
$ conda env create -f lostruins_py.yml
# ... follow prompts ...
$ conda activate lostruins_py
```

## What it does / How it works

To generate ruined textures, blockstates & block models, data/lostcities files and the necessary 
lines of code to be added to _com/mcjty/lostruins/setup/Registration.java_, either cd to this directory 
(_LostRuins/ruined_py/&nbsp;_) and execute `python -i ruined.py` or if using IntelliJ, install the 
Python plugin and then add the Conda/Python virtualenv to your Project Structure in the SDKs section, and 
set up a Run Configuration for _ruined.py_

When _ruined.py&nbsp;_ is executed, it deletes all content in built_resources, and then loads 16x16 RGBA base texture pngs from the directories 
`blocks_to_ruin/["concretes", "roads", "stones", "etc"]` and processes them with the function `ruin_blocks()` 
which per `block_name` (for non-glass textures) generates the following textures with file_end = ['',1,2,3,4,5'] in 
the directory _built_resources/assets/lostruins/textures_:

* 6 {block_name}{file_end}.png via `ruin_blocks.ruining_sequence()`
* 6 {block_name}_cracks{file_end}.png via `ruin_blocks.crack_texturizer()` (if block_name not in skip_cracks)
* 6 of `{block_name}_big_bricks_cracked{file_end}.png` (if block_name in make_bricks)
* 6 of `{block_name}_big_bricks_cracked{file_end}.png` (if block_name in make_bricks)

Additionally, `ruin_blocks()` generates blockstates and models/block files which introduces redundancies with the 
`LostRuins.runData` gradle task -- eventually I'd prefer to remove this part of `ruin_blocks()`, but I haven't yet 
looked at how to change `runData` and/or the various LostRuins classes to account for some of the things included
in the current block models and blockstates, e.g. the chipped_block variants, etc. 

Currently, _ruined.py_ will generate the following blockstates files (note: I edited LostRuins/build.gradle so that 
generated duplicates will be copied into the jar overwriting some of the files created by `runData` -- without this,
the chipped_blocks (showing the bricks texture underneath by default) will not show up in game and big_bricks variants
will include Y:180 rotation, which causes the brick grouts to not tile correctly):

* built_resources/assets/lostruins/blockstates/{block_name}.json
* built_resources/assets/lostruins/blockstates/{block_name}_ruins.json
* built_resources/assets/lostruins/blockstates/{block_name}_big_bricks_ruins.json
* built_resources/assets/lostruins/blockstates/{block_name}_damaged.json (DamagedBlock class unimplemented)

_ruins blocks include the 6 base ruined textures, plus cracked variants if they are generated at a lesser rate, and then
2 chipped_bloc

as well as a model.json for each texture variant as:
* built_resources/assets/lostruins/models/block/{block_name}{variant}.json



Currently, `ruin_blocks()` is set to not generate block registrations for each texture sub_type except big_bricks, keeping it to 
3 block registrations per texture: {block_name}_ruins, {block_name}_big_bricks_ruins with an additional block_name}_rubble. 
This was implemented recently to mitigate what seemed like an unreasonable amount of block registrations 
(the _ruins type combines normal & cracked variants, splitting them up would generate 5 blocks per texture  
and any other variants were implemented (e.g. _mossy), this would 

Also generated at the end, is a txt file - _built_resources/registration_copypasta.txt_ - is generated to copy/paste block
registration lines into _com/mcjty/lostruins/setup/Registration.java_ -- there are a number of things to add into 
the LostRuins classes (e.g. blocks registered via variant() seem to break too quickly in survival mode),
but I wanted to get feedback on what's been done so far first (i.e. the textures and blocks))

Finally, to speed integration into lostcities worldgen, I added a worldstyle _more_ruins.json&nbsp;_ and citystyle 
_citystyle_more_ruins.json&nbsp;_ that draws from the following generated content in built_resources/data/lostruins/lostcities/ --

For every block_name not in skip_random_palette
* a `palettes/{block_name}_ruins.json` randompalette 

And to tie it all together:
* `styles/more_ruins.json`  adds each randompalette above to what's in /styles/ruined.json



### Altering output 

#### Adding textures

Add/Remove RGBA 16x16 .png texture files in the  subdirectories `["concretes", "roads", "stones", "etc"]` 
in the `blocks_to_ruin` dir 
and run _ruined.py_. Generation of big_bricks & cracked variants, not generating a randompalette for structures
and/or using a lighter grout for the bricks can be controlled by appending the texture name to a number of control lists, 
currently `make_bricks`, `skip_cracks`, `skip_random_palette`, `lighter_grout`. 

For example, if a texture files `blocks_to_ruin/stones/dark_fuscia_stone.png` and `blocks_to_ruin/etc/crazy_tiles.png` 
were added, but the `crazy_tiles.png` texture doesn't work with cracked and big_bricks variants and looked bad
as a structure, while `dark_fuscia_stone.png` was good for bricks & cracks, but it was hard to read the grout in the bricks 
edit _ruined.py_ like so for testing:

```python
# Find the if __name__ line and then append the textures after it
if __name__ == "__main__":
    skip_cracks.append('crazy_tiles')
    skip_random_palette.append('crazy_tiles')

    make_bricks.append('dark_fuscia_stone')
    lighter_grout.append('dark_fuscia_stone')
    
```
Note the current inconsistency between `make_bricks` which is an allow list and the two skip_ lists 
which are deny lists - refactoring the script to change `make_bricks`to `skip_bricks` is on the TODO list.

#### Removing textures

Deleting a texture from one of the `["concretes", "roads", "stones", "etc"]` directories will cause the file
to no longer be generated on next run. 