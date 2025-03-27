from PIL import Image
import numpy as np
from litemapy import Schematic, Region, BlockState
from data import colors, block_colors, sorted_colors


def colour(color, text):
    return f'\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m'


nome = "beia"


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
        if p == [0, 0, 0]:
            continue
        distance = (r - pr)**2 + (g - pg)**2 + (b - pb)**2
        if distance < min_distance:
            min_distance = distance
            nearest_color = (pr, pg, pb, a)
    return nearest_color


img = Image.open(f"{nome}.png").convert("RGBA")
img = img.transpose(Image.ROTATE_90).transpose(Image.FLIP_TOP_BOTTOM)
pixels = np.array(img)
new_pixels = np.zeros_like(pixels)

# new_pixels[x][y] = find_nearest_color(pixels[x][y], colors)
for x in range(pixels.shape[0]):
    for y in range(pixels.shape[1]):
        new_pixels[x, y] = find_nearest_color(tuple(pixels[x, y]), colors)

indexed_pixels = []
used_colors = []
for x in range(new_pixels.shape[0]):
    indexed_pixels.append([])
    for y in range(new_pixels.shape[1]):
        r, g, b, a = new_pixels[x, y]
        color = [int(r), int(g), int(b)]
        # if color == [0, 0, 0]:
        #     indexed_pixels[x].append(-1)
        #     continue
        color_index = colors.index(color)
        color_type = sorted_colors[color_index]
        default_block = block_colors[color_type][0]

        if not [color_type, default_block] in used_colors:
            used_colors.append([color_type, default_block])

        indexed_pixels[x].append(
            used_colors.index([color_type, default_block]))


def change_block(index, new_color, block, used_colors):
    new_colors = used_colors.copy()
    new_colors[index] = [new_color, block]
    return new_colors

# parte de trocar cores necessárias
used_colors = change_block(1, "FIRE", "redstone_block", used_colors)
used_colors = change_block(4, "PLANT", "bamboo", used_colors)
used_colors = change_block(9, "COLOR_BLUE", "blue_wool", used_colors)
used_colors = change_block(10, "COLOR_PINK", "pink_wool", used_colors)

print(colour([200, 200, 0], "### Blocks"))
for i in range(len(used_colors)-1):
    color, block = used_colors[i]
    print(i, colour(colors[sorted_colors.index(color)],
          color), block)

print(colour([200, 200, 0], f'{"#"*10} count {"#"*10}'))
counter = {}
for x in range(new_pixels.shape[0]):
    for y in range(new_pixels.shape[1]):
        color, block = used_colors[indexed_pixels[x][y]]
        if counter.get(color) == None:
            counter[color] = 1
        else:
            counter[color] += 1
for color in counter.keys():
    value = counter[color]
    print(colour(colors[sorted_colors.index(color)], color), value)
# quit()

new_img = Image.fromarray(new_pixels)
new_img.save(f"{nome}_new.png")


# Shortcut to create a schematic with a single region
reg = Region(0, 0, 0, new_pixels.shape[0], 1, new_pixels.shape[1])
schem = reg.as_schematic(name=nome, author="Nokiojyn",
                         description="Made with litemapy")

for x in range(new_pixels.shape[0]):
    for z in range(new_pixels.shape[1]):
        color, block_name = used_colors[indexed_pixels[x][z]]
        block = BlockState(f"minecraft:{block_name}")
        # print(indexed_pixels[x][y],block.blockid)
        reg[x, 0, z] = block

# Create the block state we are going to use
# block = BlockState("minecraft:light_blue_concrete")

# # Build the planet
# for x, y, z in reg.block_positions():
#     if round(((x-10)**2 + (y-10)**2 + (z-10)**2)**.5) <= 10:
#         reg[x, y, z] = block

# # Save the schematic
schem.save(f"{nome}.litematic")

# Load the schematic and get its first region
schem = Schematic.load(f"{nome}.litematic")
reg = list(schem.regions.values())[0]

# Print out the basic shape
for x in reg.xrange():
    for z in reg.zrange():
        color, block = used_colors[indexed_pixels[x][z]]
        b = reg[x, 0, z]
        if b.id == "minecraft:air":
            print(" ", end="")
        else:
            print(colour(colors[sorted_colors.index(color)], "#"), end='')
    print()
