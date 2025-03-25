from PIL import Image
import numpy as np
import litemapy as lt

block_colors = {'STONE': ['stone',
  'andesite',
  'polished_andesite',
  'cobblestone',
  'pale_oak_wood',
  'bedrock',
  'gravel',
  'suspicious_gravel',
  'gold_ore',
  'iron_ore',
  'coal_ore',
  'lapis_ore',
  'dispenser',
  'piston_head',
  'moving_piston',
  'mossy_cobblestone',
  'spawner',
  'diamond_ore',
  'furnace',
  'stone_pressure_plate',
  'redstone_ore',
  'stone_bricks',
  'mossy_stone_bricks',
  'cracked_stone_bricks',
  'chiseled_stone_bricks',
  'cauldron',
  'emerald_ore',
  'ender_chest',
  'hopper',
  'dropper',
  'stone_slab',
  'smooth_stone_slab',
  'cobblestone_slab',
  'stone_brick_slab',
  'smooth_stone',
  'observer',
  'smoker',
  'blast_furnace',
  'stonecutter',
  'crafter',
  'trial_spawner',
  'vault'],
 'DIRT': ['granite',
  'polished_granite',
  'dirt',
  'coarse_dirt',
  'jungle_planks',
  'jungle_wood',
  'stripped_jungle_wood',
  'farmland',
  'jukebox',
  'jungle_trapdoor',
  'brown_mushroom_block',
  'jungle_slab',
  'dirt_path',
  'hanging_roots',
  'rooted_dirt'],
 'QUARTZ': ['diorite',
  'polished_diorite',
  'pale_oak_planks',
  'pale_oak_sapling',
  'quartz_block',
  'chiseled_quartz_block',
  'quartz_pillar',
  'sea_lantern',
  'quartz_slab',
  'smooth_quartz',
  'target'],
 'GRASS': ['grass_block', 'slime_block'],
 'PODZOL': ['podzol',
  'spruce_planks',
  'mangrove_roots',
  'muddy_mangrove_roots',
  'spruce_wood',
  'stripped_spruce_wood',
  'spruce_trapdoor',
  'spruce_slab',
  'campfire',
  'soul_campfire'],
 'WOOD': ['oak_planks',
  'oak_wood',
  'stripped_oak_wood',
  'note_block',
  'dead_bush',
  'bookshelf',
  'chiseled_bookshelf',
  'chest',
  'crafting_table',
  'oak_sign',
  'oak_wall_sign',
  'spruce_wall_hanging_sign',
  'oak_trapdoor',
  'trapped_chest',
  'daylight_detector',
  'white_banner',
  'orange_banner',
  'magenta_banner',
  'light_blue_banner',
  'yellow_banner',
  'lime_banner',
  'pink_banner',
  'gray_banner',
  'light_gray_banner',
  'cyan_banner',
  'purple_banner',
  'blue_banner',
  'brown_banner',
  'green_banner',
  'red_banner',
  'black_banner',
  'white_wall_banner',
  'orange_wall_banner',
  'magenta_wall_banner',
  'light_blue_wall_banner',
  'yellow_wall_banner',
  'lime_wall_banner',
  'pink_wall_banner',
  'gray_wall_banner',
  'light_gray_wall_banner',
  'cyan_wall_banner',
  'purple_wall_banner',
  'blue_wall_banner',
  'brown_wall_banner',
  'green_wall_banner',
  'red_wall_banner',
  'black_wall_banner',
  'oak_slab',
  'petrified_oak_slab',
  'bamboo_sapling',
  'loom',
  'barrel',
  'cartography_table',
  'fletching_table',
  'lectern',
  'smithing_table',
  'composter',
  'beehive'],
 'SAND': ['birch_planks',
  'sand',
  'suspicious_sand',
  'birch_wood',
  'stripped_birch_wood',
  'sandstone',
  'chiseled_sandstone',
  'cut_sandstone',
  'birch_sign',
  'birch_wall_sign',
  'birch_hanging_sign',
  'birch_wall_hanging_sign',
  'glowstone',
  'birch_trapdoor',
  'end_stone',
  'birch_slab',
  'sandstone_slab',
  'cut_sandstone_slab',
  'smooth_sandstone',
  'end_stone_bricks',
  'bone_block',
  'turtle_egg',
  'scaffolding',
  'ochre_froglight'],
 'COLOR_ORANGE': ['acacia_planks',
  'red_sand',
  'stripped_acacia_wood',
  'orange_wool',
  'creaking_heart',
  'acacia_sign',
  'acacia_wall_sign',
  'acacia_hanging_sign',
  'acacia_wall_hanging_sign',
  'carved_pumpkin',
  'jack_o_lantern',
  'acacia_trapdoor',
  'orange_carpet',
  'terracotta',
  'red_sandstone',
  'chiseled_red_sandstone',
  'cut_red_sandstone',
  'acacia_slab',
  'red_sandstone_slab',
  'cut_red_sandstone_slab',
  'smooth_red_sandstone',
  'honey_block',
  'honeycomb_block',
  'copper_block',
  'copper_grate',
  'lightning_rod',
  'raw_copper_block'],
 'TERRACOTTA_WHITE': ['cherry_planks',
  'cherry_trapdoor',
  'white_terracotta',
  'cherry_slab',
  'calcite'],
 'COLOR_BROWN': ['dark_oak_planks',
  'dark_oak_wood',
  'stripped_dark_oak_wood',
  'brown_wool',
  'brown_mushroom',
  'soul_sand',
  'soul_soil',
  'dark_oak_trapdoor',
  'command_block',
  'brown_carpet',
  'dark_oak_slab'],
 'COLOR_RED': ['mangrove_planks',
  'mangrove_wood',
  'red_wool',
  'red_mushroom',
  'bricks',
  'mangrove_trapdoor',
  'red_mushroom_block',
  'nether_wart',
  'enchanting_table',
  'red_carpet',
  'mangrove_slab',
  'brick_slab',
  'nether_wart_block',
  'sniffer_egg',
  'fire_coral_block',
  'fire_coral',
  'fire_coral_fan',
  'fire_coral_wall_fan',
  'shroomlight'],
 'COLOR_YELLOW': ['bamboo_planks',
  'bamboo_mosaic',
  'sponge',
  'wet_sponge',
  'yellow_wool',
  'bamboo_hanging_sign',
  'bamboo_wall_hanging_sign',
  'bamboo_trapdoor',
  'hay_block',
  'yellow_carpet',
  'bamboo_slab',
  'bamboo_mosaic_slab',
  'horn_coral_block',
  'horn_coral',
  'horn_coral_fan',
  'horn_coral_wall_fan',
  'bee_nest'],
 'PLANT': ['oak_sapling',
  'spruce_sapling',
  'birch_sapling',
  'jungle_sapling',
  'acacia_sapling',
  'dark_oak_sapling',
  'mangrove_propagule',
  'short_grass',
  'fern',
  'dandelion',
  'torchflower',
  'poppy',
  'blue_orchid',
  'allium',
  'azure_bluet',
  'red_tulip',
  'orange_tulip',
  'white_tulip',
  'pink_tulip',
  'oxeye_daisy',
  'cornflower',
  'wither_rose',
  'lily_of_the_valley',
  'cactus',
  'sugar_cane',
  'vine',
  'lily_pad',
  'cocoa',
  'carrots',
  'potatoes',
  'sunflower',
  'lilac',
  'rose_bush',
  'peony',
  'tall_grass',
  'large_fern',
  'torchflower_crop',
  'pitcher_crop',
  'pitcher_plant',
  'beetroots',
  'bamboo',
  'sweet_berry_bush',
  'cave_vines',
  'cave_vines_plant',
  'spore_blossom',
  'azalea',
  'flowering_azalea',
  'pink_petals',
  'big_dripleaf',
  'big_dripleaf_stem',
  'small_dripleaf'],
 'COLOR_PINK': ['cherry_sapling',
  'cherry_leaves',
  'pink_wool',
  'pink_carpet',
  'brain_coral_block',
  'brain_coral',
  'brain_coral_fan',
  'brain_coral_wall_fan',
  'pearlescent_froglight'],
 'WATER': ['water',
  'seagrass',
  'tall_seagrass',
  'kelp',
  'kelp_plant',
  'bubble_column',
  'frogspawn'],
 'FIRE': ['lava', 'tnt', 'fire', 'redstone_block'],
 'DEEPSLATE': ['deepslate_gold_ore',
  'deepslate_iron_ore',
  'deepslate_coal_ore',
  'deepslate_lapis_ore',
  'deepslate_diamond_ore',
  'deepslate_redstone_ore',
  'deepslate_emerald_ore',
  'deepslate_copper_ore',
  'deepslate',
  'infested_deepslate',
  'reinforced_deepslate'],
 'NETHER': ['nether_gold_ore',
  'netherrack',
  'nether_bricks',
  'nether_brick_fence',
  'nether_quartz_ore',
  'nether_brick_slab',
  'magma_block',
  'red_nether_bricks',
  'crimson_fungus',
  'weeping_vines',
  'weeping_vines_plant',
  'crimson_roots',
  'chiseled_nether_bricks',
  'cracked_nether_bricks'],
 'COLOR_GRAY': ['acacia_wood',
  'gray_wool',
  'gray_carpet',
  'dead_tube_coral_block',
  'dead_brain_coral_block',
  'dead_bubble_coral_block',
  'dead_fire_coral_block',
  'dead_horn_coral_block',
  'dead_tube_coral',
  'dead_brain_coral',
  'dead_bubble_coral',
  'dead_fire_coral',
  'dead_horn_coral',
  'dead_tube_coral_fan',
  'dead_brain_coral_fan',
  'dead_bubble_coral_fan',
  'dead_fire_coral_fan',
  'dead_horn_coral_fan',
  'dead_tube_coral_wall_fan',
  'dead_brain_coral_wall_fan',
  'dead_bubble_coral_wall_fan',
  'dead_fire_coral_wall_fan',
  'dead_horn_coral_wall_fan',
  'tinted_glass'],
 'TERRACOTTA_GRAY': ['cherry_wood', 'gray_terracotta', 'tuff'],
 'TERRACOTTA_PINK': ['stripped_cherry_wood',
  'cherry_hanging_sign',
  'cherry_wall_hanging_sign',
  'pink_terracotta'],
 'TERRACOTTA_GREEN': ['pale_oak_leaves', 'green_terracotta'],
 'LAPIS': ['lapis_block'],
 'WOOL': ['cobweb', 'mushroom_stem'],
 'SNOW': ['white_wool', 'snow', 'snow_block', 'white_carpet', 'powder_snow'],
 'COLOR_MAGENTA': ['magenta_wool',
  'magenta_carpet',
  'purpur_slab',
  'purpur_block',
  'purpur_pillar'],
 'COLOR_LIGHT_BLUE': ['light_blue_wool', 'soul_fire', 'light_blue_carpet'],
 'COLOR_LIGHT_GREEN': ['lime_wool', 'lime_carpet'],
 'COLOR_LIGHT_GRAY': ['light_gray_wool',
  'light_gray_carpet',
  'structure_block',
  'jigsaw',
  'pale_moss_block'],
 'COLOR_CYAN': ['cyan_wool',
  'prismarine',
  'prismarine_slab',
  'cyan_carpet',
  'warped_fungus',
  'warped_roots',
  'nether_sprouts',
  'twisting_vines',
  'twisting_vines_plant',
  'sculk_sensor'],
 'COLOR_PURPLE': ['purple_wool',
  'mycelium',
  'purple_carpet',
  'chorus_plant',
  'chorus_flower',
  'repeating_command_block',
  'bubble_coral_block',
  'bubble_coral',
  'bubble_coral_fan',
  'bubble_coral_wall_fan',
  'amethyst_block',
  'budding_amethyst',
  'amethyst_cluster'],
 'COLOR_BLUE': ['blue_wool',
  'blue_carpet',
  'tube_coral_block',
  'tube_coral',
  'tube_coral_fan',
  'tube_coral_wall_fan'],
 'COLOR_GREEN': ['green_wool',
  'end_portal_frame',
  'green_carpet',
  'chain_command_block',
  'dried_kelp_block',
  'sea_pickle',
  'moss_carpet',
  'moss_block'],
 'COLOR_BLACK': ['black_wool',
  'obsidian',
  'basalt',
  'polished_basalt',
  'end_portal',
  'dragon_egg',
  'black_carpet',
  'coal_block',
  'end_gateway',
  'netherite_block',
  'ancient_debris',
  'crying_obsidian',
  'respawn_anchor',
  'blackstone',
  'polished_blackstone_pressure_plate',
  'sculk',
  'sculk_vein',
  'sculk_catalyst',
  'sculk_shrieker'],
 'GOLD': ['gold_block',
  'light_weighted_pressure_plate',
  'bell',
  'raw_gold_block'],
 'METAL': ['iron_block',
  'iron_door',
  'brewing_stand',
  'anvil',
  'chipped_anvil',
  'damaged_anvil',
  'heavy_weighted_pressure_plate',
  'iron_trapdoor',
  'grindstone',
  'lantern',
  'soul_lantern',
  'lodestone',
  'heavy_core'],
 'DIAMOND': ['diamond_block',
  'beacon',
  'prismarine_bricks',
  'dark_prismarine',
  'prismarine_brick_slab',
  'dark_prismarine_slab',
  'conduit'],
 'CRIMSON_STEM': ['crimson_hanging_sign',
  'crimson_wall_hanging_sign',
  'crimson_planks'],
 'WARPED_STEM': ['warped_hanging_sign',
  'warped_wall_hanging_sign',
  'warped_planks',
  'weathered_copper',
  'weathered_copper_grate',
  'weathered_copper_bulb'],
 'ICE': ['ice', 'packed_ice', 'frosted_ice', 'blue_ice'],
 'CLAY': ['clay',
  'infested_stone',
  'infested_cobblestone',
  'infested_stone_bricks',
  'infested_mossy_stone_bricks',
  'infested_cracked_stone_bricks',
  'infested_chiseled_stone_bricks'],
 'TERRACOTTA_LIGHT_GRAY': ['mud_bricks',
  'light_gray_terracotta',
  'mud_brick_slab',
  'exposed_copper',
  'exposed_copper_grate',
  'exposed_copper_bulb'],
 'GLOW_LICHEN': ['glow_lichen', 'verdant_froglight'],
 'TERRACOTTA_ORANGE': ['resin_clump',
  'resin_block',
  'resin_bricks',
  'resin_brick_slab',
  'resin_brick_wall',
  'chiseled_resin_bricks',
  'redstone_lamp',
  'orange_terracotta'],
 'EMERALD': ['emerald_block'],
 'TERRACOTTA_MAGENTA': ['magenta_terracotta'],
 'TERRACOTTA_LIGHT_BLUE': ['light_blue_terracotta'],
 'TERRACOTTA_YELLOW': ['yellow_terracotta'],
 'TERRACOTTA_LIGHT_GREEN': ['lime_terracotta'],
 'TERRACOTTA_CYAN': ['cyan_terracotta', 'mud'],
 'TERRACOTTA_PURPLE': ['purple_terracotta'],
 'TERRACOTTA_BLUE': ['blue_terracotta'],
 'TERRACOTTA_BROWN': ['brown_terracotta',
  'pointed_dripstone',
  'dripstone_block'],
 'TERRACOTTA_RED': ['red_terracotta', 'decorated_pot'],
 'TERRACOTTA_BLACK': ['black_terracotta'],
 'WARPED_HYPHAE': ['warped_hyphae', 'stripped_warped_hyphae'],
 'WARPED_NYLIUM': ['warped_nylium',
  'oxidized_copper',
  'oxidized_copper_grate',
  'oxidized_copper_bulb'],
 'WARPED_WART_BLOCK': ['warped_wart_block'],
 'CRIMSON_HYPHAE': ['crimson_hyphae', 'stripped_crimson_hyphae'],
 'CRIMSON_NYLIUM': ['crimson_nylium'],
 'RAW_IRON': ['raw_iron_block']}

colors = [
    [
        127,
        178,
        56
    ],
    [
        247,
        233,
        163
    ],
    [
        199,
        199,
        199
    ],
    [
        255,
        0,
        0
    ],
    [
        160,
        160,
        255
    ],
    [
        167,
        167,
        167
    ],
    [
        0,
        124,
        0
    ],
    [
        255,
        255,
        255
    ],
    [
        164,
        168,
        184
    ],
    [
        151,
        109,
        77
    ],
    [
        112,
        112,
        112
    ],
    [
        64,
        64,
        255
    ],
    [
        143,
        119,
        72
    ],
    [
        255,
        252,
        245
    ],
    [
        216,
        127,
        51
    ],
    [
        178,
        76,
        216
    ],
    [
        102,
        153,
        216
    ],
    [
        229,
        229,
        51
    ],
    [
        127,
        204,
        25
    ],
    [
        242,
        127,
        165
    ],
    [
        76,
        76,
        76
    ],
    [
        153,
        153,
        153
    ],
    [
        76,
        127,
        153
    ],
    [
        127,
        63,
        178
    ],
    [
        51,
        76,
        178
    ],
    [
        102,
        76,
        51
    ],
    [
        102,
        127,
        51
    ],
    [
        153,
        51,
        51
    ],
    [
        25,
        25,
        25
    ],
    [
        250,
        238,
        77
    ],
    [
        92,
        219,
        213
    ],
    [
        74,
        128,
        255
    ],
    [
        0,
        217,
        58
    ],
    [
        129,
        86,
        49
    ],
    [
        112,
        2,
        0
    ],
    [
        209,
        177,
        161
    ],
    [
        159,
        82,
        36
    ],
    [
        149,
        87,
        108
    ],
    [
        112,
        108,
        138
    ],
    [
        186,
        133,
        36
    ],
    [
        103,
        117,
        53
    ],
    [
        160,
        77,
        78
    ],
    [
        57,
        41,
        35
    ],
    [
        135,
        107,
        98
    ],
    [
        87,
        92,
        92
    ],
    [
        122,
        73,
        88
    ],
    [
        76,
        62,
        92
    ],
    [
        76,
        50,
        35
    ],
    [
        76,
        82,
        42
    ],
    [
        142,
        60,
        46
    ],
    [
        37,
        22,
        16
    ],
    [
        189,
        48,
        49
    ],
    [
        148,
        63,
        97
    ],
    [
        92,
        25,
        29
    ],
    [
        22,
        126,
        134
    ],
    [
        58,
        142,
        140
    ],
    [
        86,
        44,
        62
    ],
    [
        20,
        180,
        133
    ],
    [
        100,
        100,
        100
    ],
    [
        216,
        175,
        147
    ],
    [
        127,
        167,
        150
    ]
]


used_colors = {}
def find_nearest_color(color, palette):
    r, g, b, a = color
    r = int(r)
    g = int(g)
    b = int(b)
    a = int(a)
    if a == 0:
        return (0, 0, 0, 0)
    min_distance = float("inf")
    nearest_color = None
    for p in palette:
        pr, pg, pb = p


        # pr = int(pr)
        # pg = int(pg)
        # pb = int(pb)
        # print(p)
        distance = (r - pr)**2 + (g - pg)**2 + (b - pb)**2
        if distance < min_distance:
            min_distance = distance
            nearest_color = (pr, pg, pb, a)
    index = colors.index(list(nearest_color[:3])) + 1
    # if index != 20:
    #     return (0, 0, 0, 0)
        # print(r,g,b)
        # print("E")
        # print(colors[index])
        # print("/"*10)
    if used_colors.get(index) is None:
        used_colors[index] = 1
    else:
        used_colors[index] += 1
    return nearest_color

img = Image.open("beia.png").convert("RGBA")
pixels = np.array(img)
new_pixels = np.zeros_like(pixels)

x = 0
y = 0
# new_pixels[x][y] = find_nearest_color(pixels[x][y], colors)
for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        new_pixels[i, j] = find_nearest_color(tuple(pixels[i, j]), colors)


keys = list(used_colors.keys())
keys.sort()
total = 0
for key in keys:
    total += used_colors[key]
    print(key, used_colors[key])
print("total", np.floor(total/64),",", total%64, total/64)
# print(used_colors)
# used_colors_id.append()
# used_colors_id = {}
# for i in used_colors.keys():
#     color = used_colors.keys()[i]
#     count = used_colors[color]
#     used_colors_id[colors.index(list(color[:3]))] = count
# print(find_nearest_color(tuple(pixels[x][y]), colors))

new_img = Image.fromarray(new_pixels)
new_img.save("beia_new.png")        