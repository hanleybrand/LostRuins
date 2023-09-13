package com.mcjty.lostruins.setup;


import com.google.common.collect.Lists;
import com.mcjty.lostruins.LostRuins;
import net.minecraft.world.inventory.MenuType;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import org.jetbrains.annotations.NotNull;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static com.mcjty.lostruins.LostRuins.MODID;
import static com.mcjty.lostruins.setup.BlockWithItem.*;

public class Registration {

    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, MODID);
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, MODID);
    public static final DeferredRegister<BlockEntityType<?>> TILES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, MODID);
    public static final DeferredRegister<MenuType<?>> CONTAINERS = DeferredRegister.create(ForgeRegistries.MENU_TYPES, MODID);

    private static String lrTxt(String txt) {
        return "lostruins:block/" + txt;
    }

    private static String mcTxt(String txt) {
        return "minecraft:block/" + txt;
    }

    static {
        simple("bricks1a", "Bricks 1", lrTxt("bricks1/bricks1a"));
        simple("bricks1b", "Bricks 1", lrTxt("bricks1/bricks1b"));
        simple("bricks1c", "Bricks 1", lrTxt("bricks1/bricks1c"));

        variant("old_bricks", "Old Bricks", lrTxt("bricks1/bricks1a"), lrTxt("bricks1/bricks1b"), lrTxt("bricks1/bricks1c"));

        variant("concrete1", "Concrete 1", lrTxt("concrete1/concrete1a"), lrTxt("concrete1/concrete1b"), lrTxt("concrete1/concrete1c"));
        variant("concrete1_bricks", "Concrete 1 Bricks", lrTxt("concrete1/concrete1a_bricks"), lrTxt("concrete1/concrete1a_bricks"), lrTxt("concrete1/concrete1a_bricks"));
        variant("concrete1_mossy", "Concrete 1 Mossy", lrTxt("concrete1/concrete1a_mossy"), lrTxt("concrete1/concrete1b_mossy"), lrTxt("concrete1/concrete1c_mossy"));
        variant("stone1", "Stone 1", lrTxt("stone1/stone1"), lrTxt("stone1/stone1_mirrored"), lrTxt("stone1/stone1_rotated"));
        variant("stone1_cracked", "Stone 1 (Cracked)", lrTxt("stone1/stone1_cracked"), lrTxt("stone1/stone1_cracked2"));
        variant("stone1_mossy", "Stone 1 (Mossy)", lrTxt("stone1/stone1_mossy"));

        variant("road1", "Road 1", lrTxt("road1/road1a"), lrTxt("road1/road1b"));
        variant("road1_cracked", "Road 1 (Cracked)", lrTxt("road1/road1a_cracked"), lrTxt("road1/road1b_cracked"));

        rubble("bricks1_rubble", "Brick rubble", lrTxt("bricks1/bricks1a"));
        rubble("stone_rubble", "Stone rubble", mcTxt("stone"));
        rubble("stone1_rubble", "Stone 1 rubble", lrTxt("stone1/stone1"));
        rubble("concrete1_rubble", "Concrete 1 rubble", lrTxt("concrete1/concrete1a_bricks"));
        rubble("stonebricks_rubble", "Stone brick rubble", mcTxt("stone_bricks"));
        //rubble("blackstone_rubble", "Blackstone rubble", mcTxt("blackstone"));
        rubble("blackstonebricks_rubble", "Blackstone brick rubble", mcTxt("polished_blackstone_bricks"));

        // TODO: variant blocks seem very low str -- implement several variants that account for different types of blocks
        // TODO: _ruins - for _ruins & bricks_ruins blocks; Properties.of(Material.STONE).strength(1.2F).sound(SoundType.STONE)
        // TODO: _damaged - for all bases; Properties.of(Material.STONE).strength(0.8F).sound(SoundType.STONE).noOcclusion(); -- do they need a DamagedBlock class?
        // TODO: _mossy - for all bases
        // TODO: slab_ruins, stairs_ruins

        // BEGIN GENERATED REGISTRATION
        // concrete blocks

        variant("black_concrete_ruins", "Black Concrete Ruins", lrTxt("concretes/black_concrete"), lrTxt("concretes/black_concrete1"), lrTxt("concretes/black_concrete2"), lrTxt("concretes/black_concrete3"), lrTxt("concretes/black_concrete4"), lrTxt("concretes/black_concrete5"), lrTxt("concretes/black_concrete_cracked"), lrTxt("concretes/black_concrete_cracked1"), lrTxt("concretes/black_concrete_cracked2"), lrTxt("concretes/black_concrete_cracked3"), lrTxt("concretes/black_concrete_cracked4"), lrTxt("concretes/black_concrete_cracked5"));
        variant("black_concrete_big_bricks_ruins", "Black Concrete Big Brick Ruins", lrTxt("concretes/black_concrete_big_bricks"), lrTxt("concretes/black_concrete_big_bricks1"), lrTxt("concretes/black_concrete_big_bricks2"), lrTxt("concretes/black_concrete_big_bricks3"), lrTxt("concretes/black_concrete_big_bricks4"), lrTxt("concretes/black_concrete_big_bricks5"), lrTxt("concretes/black_concrete_big_bricks_cracked"), lrTxt("concretes/black_concrete_big_bricks_cracked1"), lrTxt("concretes/black_concrete_big_bricks_cracked2"), lrTxt("concretes/black_concrete_big_bricks_cracked3"), lrTxt("concretes/black_concrete_big_bricks_cracked4"), lrTxt("concretes/black_concrete_big_bricks_cracked5"));
        variant("brown_concrete_ruins", "Brown Concrete Ruins", lrTxt("concretes/brown_concrete"), lrTxt("concretes/brown_concrete1"), lrTxt("concretes/brown_concrete2"), lrTxt("concretes/brown_concrete3"), lrTxt("concretes/brown_concrete4"), lrTxt("concretes/brown_concrete5"), lrTxt("concretes/brown_concrete_cracked"), lrTxt("concretes/brown_concrete_cracked1"), lrTxt("concretes/brown_concrete_cracked2"), lrTxt("concretes/brown_concrete_cracked3"), lrTxt("concretes/brown_concrete_cracked4"), lrTxt("concretes/brown_concrete_cracked5"));
        variant("brown_concrete_big_bricks_ruins", "Brown Concrete Big Brick Ruins", lrTxt("concretes/brown_concrete_big_bricks"), lrTxt("concretes/brown_concrete_big_bricks1"), lrTxt("concretes/brown_concrete_big_bricks2"), lrTxt("concretes/brown_concrete_big_bricks3"), lrTxt("concretes/brown_concrete_big_bricks4"), lrTxt("concretes/brown_concrete_big_bricks5"), lrTxt("concretes/brown_concrete_big_bricks_cracked"), lrTxt("concretes/brown_concrete_big_bricks_cracked1"), lrTxt("concretes/brown_concrete_big_bricks_cracked2"), lrTxt("concretes/brown_concrete_big_bricks_cracked3"), lrTxt("concretes/brown_concrete_big_bricks_cracked4"), lrTxt("concretes/brown_concrete_big_bricks_cracked5"));
        variant("gray_concrete_ruins", "Gray Concrete Ruins", lrTxt("concretes/gray_concrete"), lrTxt("concretes/gray_concrete1"), lrTxt("concretes/gray_concrete2"), lrTxt("concretes/gray_concrete3"), lrTxt("concretes/gray_concrete4"), lrTxt("concretes/gray_concrete5"), lrTxt("concretes/gray_concrete_cracked"), lrTxt("concretes/gray_concrete_cracked1"), lrTxt("concretes/gray_concrete_cracked2"), lrTxt("concretes/gray_concrete_cracked3"), lrTxt("concretes/gray_concrete_cracked4"), lrTxt("concretes/gray_concrete_cracked5"));
        variant("gray_concrete_big_bricks_ruins", "Gray Concrete Big Brick Ruins", lrTxt("concretes/gray_concrete_big_bricks"), lrTxt("concretes/gray_concrete_big_bricks1"), lrTxt("concretes/gray_concrete_big_bricks2"), lrTxt("concretes/gray_concrete_big_bricks3"), lrTxt("concretes/gray_concrete_big_bricks4"), lrTxt("concretes/gray_concrete_big_bricks5"), lrTxt("concretes/gray_concrete_big_bricks_cracked"), lrTxt("concretes/gray_concrete_big_bricks_cracked1"), lrTxt("concretes/gray_concrete_big_bricks_cracked2"), lrTxt("concretes/gray_concrete_big_bricks_cracked3"), lrTxt("concretes/gray_concrete_big_bricks_cracked4"), lrTxt("concretes/gray_concrete_big_bricks_cracked5"));
        variant("light_gray_concrete_ruins", "Light Gray Concrete Ruins", lrTxt("concretes/light_gray_concrete"), lrTxt("concretes/light_gray_concrete1"), lrTxt("concretes/light_gray_concrete2"), lrTxt("concretes/light_gray_concrete3"), lrTxt("concretes/light_gray_concrete4"), lrTxt("concretes/light_gray_concrete5"), lrTxt("concretes/light_gray_concrete_cracked"), lrTxt("concretes/light_gray_concrete_cracked1"), lrTxt("concretes/light_gray_concrete_cracked2"), lrTxt("concretes/light_gray_concrete_cracked3"), lrTxt("concretes/light_gray_concrete_cracked4"), lrTxt("concretes/light_gray_concrete_cracked5"));
        variant("light_gray_concrete_big_bricks_ruins", "Light Gray Concrete Big Brick Ruins", lrTxt("concretes/light_gray_concrete_big_bricks"), lrTxt("concretes/light_gray_concrete_big_bricks1"), lrTxt("concretes/light_gray_concrete_big_bricks2"), lrTxt("concretes/light_gray_concrete_big_bricks3"), lrTxt("concretes/light_gray_concrete_big_bricks4"), lrTxt("concretes/light_gray_concrete_big_bricks5"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked1"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked2"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked3"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked4"), lrTxt("concretes/light_gray_concrete_big_bricks_cracked5"));
        variant("white_concrete_ruins", "White Concrete Ruins", lrTxt("concretes/white_concrete"), lrTxt("concretes/white_concrete1"), lrTxt("concretes/white_concrete2"), lrTxt("concretes/white_concrete3"), lrTxt("concretes/white_concrete4"), lrTxt("concretes/white_concrete5"), lrTxt("concretes/white_concrete_cracked"), lrTxt("concretes/white_concrete_cracked1"), lrTxt("concretes/white_concrete_cracked2"), lrTxt("concretes/white_concrete_cracked3"), lrTxt("concretes/white_concrete_cracked4"), lrTxt("concretes/white_concrete_cracked5"));
        variant("white_concrete_big_bricks_ruins", "White Concrete Big Brick Ruins", lrTxt("concretes/white_concrete_big_bricks"), lrTxt("concretes/white_concrete_big_bricks1"), lrTxt("concretes/white_concrete_big_bricks2"), lrTxt("concretes/white_concrete_big_bricks3"), lrTxt("concretes/white_concrete_big_bricks4"), lrTxt("concretes/white_concrete_big_bricks5"), lrTxt("concretes/white_concrete_big_bricks_cracked"), lrTxt("concretes/white_concrete_big_bricks_cracked1"), lrTxt("concretes/white_concrete_big_bricks_cracked2"), lrTxt("concretes/white_concrete_big_bricks_cracked3"), lrTxt("concretes/white_concrete_big_bricks_cracked4"), lrTxt("concretes/white_concrete_big_bricks_cracked5"));

        // concrete rubble
        rubble("black_concrete_rubble", "Black Concrete Rubble", lrTxt("concretes/black_concrete"));
        rubble("brown_concrete_rubble", "Brown Concrete Rubble", lrTxt("concretes/brown_concrete"));
        rubble("gray_concrete_rubble", "Gray Concrete Rubble", lrTxt("concretes/gray_concrete"));
        rubble("light_gray_concrete_rubble", "Light Gray Concrete Rubble", lrTxt("concretes/light_gray_concrete"));
        rubble("white_concrete_rubble", "White Concrete Rubble", lrTxt("concretes/white_concrete"));


        // stone blocks

        variant("andesite_ruins", "Andesite Ruins", lrTxt("stones/andesite"), lrTxt("stones/andesite1"), lrTxt("stones/andesite2"), lrTxt("stones/andesite3"), lrTxt("stones/andesite4"), lrTxt("stones/andesite5"), lrTxt("stones/andesite_cracked"), lrTxt("stones/andesite_cracked1"), lrTxt("stones/andesite_cracked2"), lrTxt("stones/andesite_cracked3"), lrTxt("stones/andesite_cracked4"), lrTxt("stones/andesite_cracked5"));
        variant("andesite_big_bricks_ruins", "Andesite Big Brick Ruins", lrTxt("stones/andesite_big_bricks"), lrTxt("stones/andesite_big_bricks1"), lrTxt("stones/andesite_big_bricks2"), lrTxt("stones/andesite_big_bricks3"), lrTxt("stones/andesite_big_bricks4"), lrTxt("stones/andesite_big_bricks5"), lrTxt("stones/andesite_big_bricks_cracked"), lrTxt("stones/andesite_big_bricks_cracked1"), lrTxt("stones/andesite_big_bricks_cracked2"), lrTxt("stones/andesite_big_bricks_cracked3"), lrTxt("stones/andesite_big_bricks_cracked4"), lrTxt("stones/andesite_big_bricks_cracked5"));
        variant("blackstone_ruins", "Blackstone Ruins", lrTxt("stones/blackstone"), lrTxt("stones/blackstone1"), lrTxt("stones/blackstone2"), lrTxt("stones/blackstone3"), lrTxt("stones/blackstone4"), lrTxt("stones/blackstone5"), lrTxt("stones/blackstone_cracked"), lrTxt("stones/blackstone_cracked1"), lrTxt("stones/blackstone_cracked2"), lrTxt("stones/blackstone_cracked3"), lrTxt("stones/blackstone_cracked4"), lrTxt("stones/blackstone_cracked5"));
        variant("blackstone_big_bricks_ruins", "Blackstone Big Brick Ruins", lrTxt("stones/blackstone_big_bricks"), lrTxt("stones/blackstone_big_bricks1"), lrTxt("stones/blackstone_big_bricks2"), lrTxt("stones/blackstone_big_bricks3"), lrTxt("stones/blackstone_big_bricks4"), lrTxt("stones/blackstone_big_bricks5"), lrTxt("stones/blackstone_big_bricks_cracked"), lrTxt("stones/blackstone_big_bricks_cracked1"), lrTxt("stones/blackstone_big_bricks_cracked2"), lrTxt("stones/blackstone_big_bricks_cracked3"), lrTxt("stones/blackstone_big_bricks_cracked4"), lrTxt("stones/blackstone_big_bricks_cracked5"));
        variant("cobbled_deepslate_ruins", "Cobbled Deepslate Ruins", lrTxt("stones/cobbled_deepslate"), lrTxt("stones/cobbled_deepslate1"), lrTxt("stones/cobbled_deepslate2"), lrTxt("stones/cobbled_deepslate3"), lrTxt("stones/cobbled_deepslate4"), lrTxt("stones/cobbled_deepslate5"), lrTxt("stones/cobbled_deepslate_cracked"), lrTxt("stones/cobbled_deepslate_cracked1"), lrTxt("stones/cobbled_deepslate_cracked2"), lrTxt("stones/cobbled_deepslate_cracked3"), lrTxt("stones/cobbled_deepslate_cracked4"), lrTxt("stones/cobbled_deepslate_cracked5"));
        variant("cobblestone_ruins", "Cobblestone Ruins", lrTxt("stones/cobblestone"), lrTxt("stones/cobblestone1"), lrTxt("stones/cobblestone2"), lrTxt("stones/cobblestone3"), lrTxt("stones/cobblestone4"), lrTxt("stones/cobblestone5"), lrTxt("stones/cobblestone_cracked"), lrTxt("stones/cobblestone_cracked1"), lrTxt("stones/cobblestone_cracked2"), lrTxt("stones/cobblestone_cracked3"), lrTxt("stones/cobblestone_cracked4"), lrTxt("stones/cobblestone_cracked5"));
        variant("deepslate_ruins", "Deepslate Ruins", lrTxt("stones/deepslate"), lrTxt("stones/deepslate1"), lrTxt("stones/deepslate2"), lrTxt("stones/deepslate3"), lrTxt("stones/deepslate4"), lrTxt("stones/deepslate5"), lrTxt("stones/deepslate_cracked"), lrTxt("stones/deepslate_cracked1"), lrTxt("stones/deepslate_cracked2"), lrTxt("stones/deepslate_cracked3"), lrTxt("stones/deepslate_cracked4"), lrTxt("stones/deepslate_cracked5"));
        variant("deepslate_big_bricks_ruins", "Deepslate Big Brick Ruins", lrTxt("stones/deepslate_big_bricks"), lrTxt("stones/deepslate_big_bricks1"), lrTxt("stones/deepslate_big_bricks2"), lrTxt("stones/deepslate_big_bricks3"), lrTxt("stones/deepslate_big_bricks4"), lrTxt("stones/deepslate_big_bricks5"), lrTxt("stones/deepslate_big_bricks_cracked"), lrTxt("stones/deepslate_big_bricks_cracked1"), lrTxt("stones/deepslate_big_bricks_cracked2"), lrTxt("stones/deepslate_big_bricks_cracked3"), lrTxt("stones/deepslate_big_bricks_cracked4"), lrTxt("stones/deepslate_big_bricks_cracked5"));
        variant("diorite_ruins", "Diorite Ruins", lrTxt("stones/diorite"), lrTxt("stones/diorite1"), lrTxt("stones/diorite2"), lrTxt("stones/diorite3"), lrTxt("stones/diorite4"), lrTxt("stones/diorite5"), lrTxt("stones/diorite_cracked"), lrTxt("stones/diorite_cracked1"), lrTxt("stones/diorite_cracked2"), lrTxt("stones/diorite_cracked3"), lrTxt("stones/diorite_cracked4"), lrTxt("stones/diorite_cracked5"));
        variant("diorite_big_bricks_ruins", "Diorite Big Brick Ruins", lrTxt("stones/diorite_big_bricks"), lrTxt("stones/diorite_big_bricks1"), lrTxt("stones/diorite_big_bricks2"), lrTxt("stones/diorite_big_bricks3"), lrTxt("stones/diorite_big_bricks4"), lrTxt("stones/diorite_big_bricks5"), lrTxt("stones/diorite_big_bricks_cracked"), lrTxt("stones/diorite_big_bricks_cracked1"), lrTxt("stones/diorite_big_bricks_cracked2"), lrTxt("stones/diorite_big_bricks_cracked3"), lrTxt("stones/diorite_big_bricks_cracked4"), lrTxt("stones/diorite_big_bricks_cracked5"));
        variant("dripstone_block_ruins", "Dripstone Block Ruins", lrTxt("stones/dripstone_block"), lrTxt("stones/dripstone_block1"), lrTxt("stones/dripstone_block2"), lrTxt("stones/dripstone_block3"), lrTxt("stones/dripstone_block4"), lrTxt("stones/dripstone_block5"), lrTxt("stones/dripstone_block_cracked"), lrTxt("stones/dripstone_block_cracked1"), lrTxt("stones/dripstone_block_cracked2"), lrTxt("stones/dripstone_block_cracked3"), lrTxt("stones/dripstone_block_cracked4"), lrTxt("stones/dripstone_block_cracked5"));
        variant("dripstone_block_big_bricks_ruins", "Dripstone Block Big Brick Ruins", lrTxt("stones/dripstone_block_big_bricks"), lrTxt("stones/dripstone_block_big_bricks1"), lrTxt("stones/dripstone_block_big_bricks2"), lrTxt("stones/dripstone_block_big_bricks3"), lrTxt("stones/dripstone_block_big_bricks4"), lrTxt("stones/dripstone_block_big_bricks5"), lrTxt("stones/dripstone_block_big_bricks_cracked"), lrTxt("stones/dripstone_block_big_bricks_cracked1"), lrTxt("stones/dripstone_block_big_bricks_cracked2"), lrTxt("stones/dripstone_block_big_bricks_cracked3"), lrTxt("stones/dripstone_block_big_bricks_cracked4"), lrTxt("stones/dripstone_block_big_bricks_cracked5"));
        variant("old_stone_ruins", "Old Stone Ruins", lrTxt("stones/old_stone"), lrTxt("stones/old_stone1"), lrTxt("stones/old_stone2"), lrTxt("stones/old_stone3"), lrTxt("stones/old_stone4"), lrTxt("stones/old_stone5"));
        variant("red_sandstone_ruins", "Red Sandstone Ruins", lrTxt("stones/red_sandstone"), lrTxt("stones/red_sandstone1"), lrTxt("stones/red_sandstone2"), lrTxt("stones/red_sandstone3"), lrTxt("stones/red_sandstone4"), lrTxt("stones/red_sandstone5"), lrTxt("stones/red_sandstone_cracked"), lrTxt("stones/red_sandstone_cracked1"), lrTxt("stones/red_sandstone_cracked2"), lrTxt("stones/red_sandstone_cracked3"), lrTxt("stones/red_sandstone_cracked4"), lrTxt("stones/red_sandstone_cracked5"));
        variant("red_sandstone_big_bricks_ruins", "Red Sandstone Big Brick Ruins", lrTxt("stones/red_sandstone_big_bricks"), lrTxt("stones/red_sandstone_big_bricks1"), lrTxt("stones/red_sandstone_big_bricks2"), lrTxt("stones/red_sandstone_big_bricks3"), lrTxt("stones/red_sandstone_big_bricks4"), lrTxt("stones/red_sandstone_big_bricks5"), lrTxt("stones/red_sandstone_big_bricks_cracked"), lrTxt("stones/red_sandstone_big_bricks_cracked1"), lrTxt("stones/red_sandstone_big_bricks_cracked2"), lrTxt("stones/red_sandstone_big_bricks_cracked3"), lrTxt("stones/red_sandstone_big_bricks_cracked4"), lrTxt("stones/red_sandstone_big_bricks_cracked5"));
        variant("sandstone_ruins", "Sandstone Ruins", lrTxt("stones/sandstone"), lrTxt("stones/sandstone1"), lrTxt("stones/sandstone2"), lrTxt("stones/sandstone3"), lrTxt("stones/sandstone4"), lrTxt("stones/sandstone5"), lrTxt("stones/sandstone_cracked"), lrTxt("stones/sandstone_cracked1"), lrTxt("stones/sandstone_cracked2"), lrTxt("stones/sandstone_cracked3"), lrTxt("stones/sandstone_cracked4"), lrTxt("stones/sandstone_cracked5"));
        variant("sandstone_big_bricks_ruins", "Sandstone Big Brick Ruins", lrTxt("stones/sandstone_big_bricks"), lrTxt("stones/sandstone_big_bricks1"), lrTxt("stones/sandstone_big_bricks2"), lrTxt("stones/sandstone_big_bricks3"), lrTxt("stones/sandstone_big_bricks4"), lrTxt("stones/sandstone_big_bricks5"), lrTxt("stones/sandstone_big_bricks_cracked"), lrTxt("stones/sandstone_big_bricks_cracked1"), lrTxt("stones/sandstone_big_bricks_cracked2"), lrTxt("stones/sandstone_big_bricks_cracked3"), lrTxt("stones/sandstone_big_bricks_cracked4"), lrTxt("stones/sandstone_big_bricks_cracked5"));
        variant("smooth_basalt_ruins", "Smooth Basalt Ruins", lrTxt("stones/smooth_basalt"), lrTxt("stones/smooth_basalt1"), lrTxt("stones/smooth_basalt2"), lrTxt("stones/smooth_basalt3"), lrTxt("stones/smooth_basalt4"), lrTxt("stones/smooth_basalt5"), lrTxt("stones/smooth_basalt_cracked"), lrTxt("stones/smooth_basalt_cracked1"), lrTxt("stones/smooth_basalt_cracked2"), lrTxt("stones/smooth_basalt_cracked3"), lrTxt("stones/smooth_basalt_cracked4"), lrTxt("stones/smooth_basalt_cracked5"));
        variant("smooth_basalt_big_bricks_ruins", "Smooth Basalt Big Brick Ruins", lrTxt("stones/smooth_basalt_big_bricks"), lrTxt("stones/smooth_basalt_big_bricks1"), lrTxt("stones/smooth_basalt_big_bricks2"), lrTxt("stones/smooth_basalt_big_bricks3"), lrTxt("stones/smooth_basalt_big_bricks4"), lrTxt("stones/smooth_basalt_big_bricks5"), lrTxt("stones/smooth_basalt_big_bricks_cracked"), lrTxt("stones/smooth_basalt_big_bricks_cracked1"), lrTxt("stones/smooth_basalt_big_bricks_cracked2"), lrTxt("stones/smooth_basalt_big_bricks_cracked3"), lrTxt("stones/smooth_basalt_big_bricks_cracked4"), lrTxt("stones/smooth_basalt_big_bricks_cracked5"));
        variant("smooth_stone_ruins", "Smooth Stone Ruins", lrTxt("stones/smooth_stone"), lrTxt("stones/smooth_stone1"), lrTxt("stones/smooth_stone2"), lrTxt("stones/smooth_stone3"), lrTxt("stones/smooth_stone4"), lrTxt("stones/smooth_stone5"), lrTxt("stones/smooth_stone_cracked"), lrTxt("stones/smooth_stone_cracked1"), lrTxt("stones/smooth_stone_cracked2"), lrTxt("stones/smooth_stone_cracked3"), lrTxt("stones/smooth_stone_cracked4"), lrTxt("stones/smooth_stone_cracked5"));
        variant("tuff_ruins", "Tuff Ruins", lrTxt("stones/tuff"), lrTxt("stones/tuff1"), lrTxt("stones/tuff2"), lrTxt("stones/tuff3"), lrTxt("stones/tuff4"), lrTxt("stones/tuff5"), lrTxt("stones/tuff_cracked"), lrTxt("stones/tuff_cracked1"), lrTxt("stones/tuff_cracked2"), lrTxt("stones/tuff_cracked3"), lrTxt("stones/tuff_cracked4"), lrTxt("stones/tuff_cracked5"));
        variant("tuff_big_bricks_ruins", "Tuff Big Brick Ruins", lrTxt("stones/tuff_big_bricks"), lrTxt("stones/tuff_big_bricks1"), lrTxt("stones/tuff_big_bricks2"), lrTxt("stones/tuff_big_bricks3"), lrTxt("stones/tuff_big_bricks4"), lrTxt("stones/tuff_big_bricks5"), lrTxt("stones/tuff_big_bricks_cracked"), lrTxt("stones/tuff_big_bricks_cracked1"), lrTxt("stones/tuff_big_bricks_cracked2"), lrTxt("stones/tuff_big_bricks_cracked3"), lrTxt("stones/tuff_big_bricks_cracked4"), lrTxt("stones/tuff_big_bricks_cracked5"));
        variant("white_granite_ruins", "White Granite Ruins", lrTxt("stones/white_granite"), lrTxt("stones/white_granite1"), lrTxt("stones/white_granite2"), lrTxt("stones/white_granite3"), lrTxt("stones/white_granite4"), lrTxt("stones/white_granite5"), lrTxt("stones/white_granite_cracked"), lrTxt("stones/white_granite_cracked1"), lrTxt("stones/white_granite_cracked2"), lrTxt("stones/white_granite_cracked3"), lrTxt("stones/white_granite_cracked4"), lrTxt("stones/white_granite_cracked5"));
        variant("white_granite_big_bricks_ruins", "White Granite Big Brick Ruins", lrTxt("stones/white_granite_big_bricks"), lrTxt("stones/white_granite_big_bricks1"), lrTxt("stones/white_granite_big_bricks2"), lrTxt("stones/white_granite_big_bricks3"), lrTxt("stones/white_granite_big_bricks4"), lrTxt("stones/white_granite_big_bricks5"), lrTxt("stones/white_granite_big_bricks_cracked"), lrTxt("stones/white_granite_big_bricks_cracked1"), lrTxt("stones/white_granite_big_bricks_cracked2"), lrTxt("stones/white_granite_big_bricks_cracked3"), lrTxt("stones/white_granite_big_bricks_cracked4"), lrTxt("stones/white_granite_big_bricks_cracked5"));
        variant("white_granite_pillar_ruins", "White Granite Pillar Ruins", lrTxt("stones/white_granite_pillar"), lrTxt("stones/white_granite_pillar1"), lrTxt("stones/white_granite_pillar2"), lrTxt("stones/white_granite_pillar3"), lrTxt("stones/white_granite_pillar4"), lrTxt("stones/white_granite_pillar5"), lrTxt("stones/white_granite_pillar_cracked"), lrTxt("stones/white_granite_pillar_cracked1"), lrTxt("stones/white_granite_pillar_cracked2"), lrTxt("stones/white_granite_pillar_cracked3"), lrTxt("stones/white_granite_pillar_cracked4"), lrTxt("stones/white_granite_pillar_cracked5"));

        // stone rubble
        rubble("andesite_rubble", "Andesite Rubble", lrTxt("stones/andesite"));
        rubble("blackstone_rubble", "Blackstone Rubble", lrTxt("stones/blackstone"));
        rubble("cobbled_deepslate_rubble", "Cobbled Deepslate Rubble", lrTxt("stones/cobbled_deepslate"));
        rubble("cobblestone_rubble", "Cobblestone Rubble", lrTxt("stones/cobblestone"));
        rubble("deepslate_rubble", "Deepslate Rubble", lrTxt("stones/deepslate"));
        rubble("diorite_rubble", "Diorite Rubble", lrTxt("stones/diorite"));
        rubble("dripstone_block_rubble", "Dripstone Block Rubble", lrTxt("stones/dripstone_block"));
        rubble("old_stone_rubble", "Old Stone Rubble", lrTxt("stones/old_stone"));
        rubble("red_sandstone_rubble", "Red Sandstone Rubble", lrTxt("stones/red_sandstone"));
        rubble("sandstone_rubble", "Sandstone Rubble", lrTxt("stones/sandstone"));
        rubble("smooth_basalt_rubble", "Smooth Basalt Rubble", lrTxt("stones/smooth_basalt"));
        rubble("smooth_stone_rubble", "Smooth Stone Rubble", lrTxt("stones/smooth_stone"));
        rubble("tuff_rubble", "Tuff Rubble", lrTxt("stones/tuff"));
        rubble("white_granite_rubble", "White Granite Rubble", lrTxt("stones/white_granite"));
        rubble("white_granite_pillar_rubble", "White Granite Pillar Rubble", lrTxt("stones/white_granite_pillar"));


        // etc blocks

        variant("beige_tile_ruins", "Beige Tile Ruins", lrTxt("etc/beige_tile"), lrTxt("etc/beige_tile1"), lrTxt("etc/beige_tile2"), lrTxt("etc/beige_tile3"), lrTxt("etc/beige_tile4"), lrTxt("etc/beige_tile5"), lrTxt("etc/beige_tile_cracked"), lrTxt("etc/beige_tile_cracked1"), lrTxt("etc/beige_tile_cracked2"), lrTxt("etc/beige_tile_cracked3"), lrTxt("etc/beige_tile_cracked4"), lrTxt("etc/beige_tile_cracked5"));
        variant("beige_tile_2_ruins", "Beige Tile 2 Ruins", lrTxt("etc/beige_tile_2"), lrTxt("etc/beige_tile_21"), lrTxt("etc/beige_tile_22"), lrTxt("etc/beige_tile_23"), lrTxt("etc/beige_tile_24"), lrTxt("etc/beige_tile_25"), lrTxt("etc/beige_tile_2_cracked"), lrTxt("etc/beige_tile_2_cracked1"), lrTxt("etc/beige_tile_2_cracked2"), lrTxt("etc/beige_tile_2_cracked3"), lrTxt("etc/beige_tile_2_cracked4"), lrTxt("etc/beige_tile_2_cracked5"));
        variant("blue_tile_ruins", "Blue Tile Ruins", lrTxt("etc/blue_tile"), lrTxt("etc/blue_tile1"), lrTxt("etc/blue_tile2"), lrTxt("etc/blue_tile3"), lrTxt("etc/blue_tile4"), lrTxt("etc/blue_tile5"), lrTxt("etc/blue_tile_cracked"), lrTxt("etc/blue_tile_cracked1"), lrTxt("etc/blue_tile_cracked2"), lrTxt("etc/blue_tile_cracked3"), lrTxt("etc/blue_tile_cracked4"), lrTxt("etc/blue_tile_cracked5"));
        variant("gray_wood_boards_ruins", "Gray Wood Boards Ruins", lrTxt("etc/gray_wood_boards"), lrTxt("etc/gray_wood_boards1"), lrTxt("etc/gray_wood_boards2"), lrTxt("etc/gray_wood_boards3"), lrTxt("etc/gray_wood_boards4"), lrTxt("etc/gray_wood_boards5"));
        variant("gray_wood_planks_ruins", "Gray Wood Planks Ruins", lrTxt("etc/gray_wood_planks"), lrTxt("etc/gray_wood_planks1"), lrTxt("etc/gray_wood_planks2"), lrTxt("etc/gray_wood_planks3"), lrTxt("etc/gray_wood_planks4"), lrTxt("etc/gray_wood_planks5"));
        variant("gray_wood_planks_nailed_ruins", "Gray Wood Planks Nailed Ruins", lrTxt("etc/gray_wood_planks_nailed"), lrTxt("etc/gray_wood_planks_nailed1"), lrTxt("etc/gray_wood_planks_nailed2"), lrTxt("etc/gray_wood_planks_nailed3"), lrTxt("etc/gray_wood_planks_nailed4"), lrTxt("etc/gray_wood_planks_nailed5"));
        variant("plastic_blue_ruins", "Plastic Blue Ruins", lrTxt("etc/plastic_blue"), lrTxt("etc/plastic_blue1"), lrTxt("etc/plastic_blue2"), lrTxt("etc/plastic_blue3"), lrTxt("etc/plastic_blue4"), lrTxt("etc/plastic_blue5"), lrTxt("etc/plastic_blue_cracked"), lrTxt("etc/plastic_blue_cracked1"), lrTxt("etc/plastic_blue_cracked2"), lrTxt("etc/plastic_blue_cracked3"), lrTxt("etc/plastic_blue_cracked4"), lrTxt("etc/plastic_blue_cracked5"));
        variant("plastic_blue_big_bricks_ruins", "Plastic Blue Big Brick Ruins", lrTxt("etc/plastic_blue_big_bricks"), lrTxt("etc/plastic_blue_big_bricks1"), lrTxt("etc/plastic_blue_big_bricks2"), lrTxt("etc/plastic_blue_big_bricks3"), lrTxt("etc/plastic_blue_big_bricks4"), lrTxt("etc/plastic_blue_big_bricks5"), lrTxt("etc/plastic_blue_big_bricks_cracked"), lrTxt("etc/plastic_blue_big_bricks_cracked1"), lrTxt("etc/plastic_blue_big_bricks_cracked2"), lrTxt("etc/plastic_blue_big_bricks_cracked3"), lrTxt("etc/plastic_blue_big_bricks_cracked4"), lrTxt("etc/plastic_blue_big_bricks_cracked5"));
        variant("tile_irregular_ruins", "Tile Irregular Ruins", lrTxt("etc/tile_irregular"), lrTxt("etc/tile_irregular1"), lrTxt("etc/tile_irregular2"), lrTxt("etc/tile_irregular3"), lrTxt("etc/tile_irregular4"), lrTxt("etc/tile_irregular5"));
        variant("tile_pattern_ruins", "Tile Pattern Ruins", lrTxt("etc/tile_pattern"), lrTxt("etc/tile_pattern1"), lrTxt("etc/tile_pattern2"), lrTxt("etc/tile_pattern3"), lrTxt("etc/tile_pattern4"), lrTxt("etc/tile_pattern5"), lrTxt("etc/tile_pattern_cracked"), lrTxt("etc/tile_pattern_cracked1"), lrTxt("etc/tile_pattern_cracked2"), lrTxt("etc/tile_pattern_cracked3"), lrTxt("etc/tile_pattern_cracked4"), lrTxt("etc/tile_pattern_cracked5"));

        // etc rubble
        rubble("beige_tile_rubble", "Beige Tile Rubble", lrTxt("etc/beige_tile"));
        rubble("beige_tile_2_rubble", "Beige Tile 2 Rubble", lrTxt("etc/beige_tile_2"));
        rubble("blue_tile_rubble", "Blue Tile Rubble", lrTxt("etc/blue_tile"));
        rubble("gray_wood_boards_rubble", "Gray Wood Boards Rubble", lrTxt("etc/gray_wood_boards"));
        rubble("gray_wood_planks_rubble", "Gray Wood Planks Rubble", lrTxt("etc/gray_wood_planks"));
        rubble("gray_wood_planks_nailed_rubble", "Gray Wood Planks Nailed Rubble", lrTxt("etc/gray_wood_planks_nailed"));
        rubble("plastic_blue_rubble", "Plastic Blue Rubble", lrTxt("etc/plastic_blue"));
        rubble("tile_irregular_rubble", "Tile Irregular Rubble", lrTxt("etc/tile_irregular"));
        rubble("tile_pattern_rubble", "Tile Pattern Rubble", lrTxt("etc/tile_pattern"));


        // roads blocks
        variant("asphalt_ruins", "Asphalt Ruins", lrTxt("roads/asphalt"), lrTxt("roads/asphalt1"), lrTxt("roads/asphalt2"), lrTxt("roads/asphalt3"), lrTxt("roads/asphalt4"), lrTxt("roads/asphalt5"), lrTxt("roads/asphalt_cracked"), lrTxt("roads/asphalt_cracked1"), lrTxt("roads/asphalt_cracked2"), lrTxt("roads/asphalt_cracked3"), lrTxt("roads/asphalt_cracked4"), lrTxt("roads/asphalt_cracked5"));
        variant("asphalt_darker_ruins", "Asphalt Darker Ruins", lrTxt("roads/asphalt_darker"), lrTxt("roads/asphalt_darker1"), lrTxt("roads/asphalt_darker2"), lrTxt("roads/asphalt_darker3"), lrTxt("roads/asphalt_darker4"), lrTxt("roads/asphalt_darker5"), lrTxt("roads/asphalt_darker_cracked"), lrTxt("roads/asphalt_darker_cracked1"), lrTxt("roads/asphalt_darker_cracked2"), lrTxt("roads/asphalt_darker_cracked3"), lrTxt("roads/asphalt_darker_cracked4"), lrTxt("roads/asphalt_darker_cracked5"));

        // roads rubble
        rubble("asphalt_rubble", "Asphalt Rubble", lrTxt("roads/asphalt"));
        rubble("asphalt_darker_rubble", "Asphalt Darker Rubble", lrTxt("roads/asphalt_darker"));

        // END GENERATED REGISTRATION


        for (SuffixWithTextures s : Lists.newArrayList(
                SuffixWithTextures.create("complete", "", "complete"),
                SuffixWithTextures.create("mossy", " (mossy)", "complete_mossy", "complete_mossy_vines", "broken_all_mossy"),
                SuffixWithTextures.create("broken", " (broken)", "broken1", "broken2", "broken3", "broken4", "broken5", "broken_all", "broken_frame"),
                SuffixWithTextures.create("broken_mossy", " (broken, mossy)", "broken_frame_mossy", "broken_mossy"),
                SuffixWithTextures.create("vines", " (vines)", "broken_frame_vines", "broken_frame_mossy_vines", "broken_mossy_vines"))) {
            List<String> glass32_txt = Arrays.stream(s.textures()).map(t -> lrTxt("glassgray3x2/" + t)).collect(Collectors.toList());

            glass("glassgray3x2_" + s.suffix(), "Old glass 3x2" + s.languageSuffix(), glass32_txt);
            pane("glassgray3x2_pane_" + s.suffix(), "Old glass pane 3x2" + s.languageSuffix(), glass32_txt);
            // glassgray variants
            List<String> glass12l_txt = Arrays.stream(s.textures()).map(t -> lrTxt("glassgray1x2l/" + t)).collect(Collectors.toList());
            glass("glassgray1x2l_" + s.suffix(), "Old glass 1x2 Left" + s.languageSuffix(), glass12l_txt);
            pane("glassgray1x2l_pane_" + s.suffix(), "Old glass pane 1x2 Left" + s.languageSuffix(), glass12l_txt);
        }
    }

    private static record SuffixWithTextures(String suffix, String languageSuffix, String... textures) {
        public static SuffixWithTextures create(String suffix, String languageSuffix, String... textures) {
            return new SuffixWithTextures(suffix, languageSuffix, textures);
        }
    }

    public static void register() {
        IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();
        BLOCKS.register(bus);
        ITEMS.register(bus);
        TILES.register(bus);
        CONTAINERS.register(bus);
    }

    @NotNull
    public static Item.Properties createStandardProperties() {
        return LostRuins.setup.defaultProperties();
    }

    @NotNull
    public static BlockBehaviour.Properties createGlassProperties() {
        return BlockBehaviour.Properties.of(Material.GLASS).strength(0.3F).sound(SoundType.GLASS).noOcclusion();
    }

    @NotNull
    public static BlockBehaviour.Properties createRuinedProperties() {
        return BlockBehaviour.Properties.of(Material.STONE).strength(1.2F).sound(SoundType.STONE).noOcclusion();
    }

    @NotNull
    public static BlockBehaviour.Properties createDamagedProperties() {
        return BlockBehaviour.Properties.of(Material.STONE).strength(0.9F).sound(SoundType.STONE);
    }
}
