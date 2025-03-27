from PIL import Image
import numpy as np
import litemapy as lt
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
        distance = (r - pr)**2 + (g - pg)**2 + (b - pb)**2
        if distance < min_distance:
            min_distance = distance
            nearest_color = (pr, pg, pb, a)
    return nearest_color


img = Image.open(f"{nome}.png").convert("RGBA")
pixels = np.array(img)
new_pixels = np.zeros_like(pixels)

# new_pixels[x][y] = find_nearest_color(pixels[x][y], colors)
for x in range(pixels.shape[0]):
    for y in range(pixels.shape[1]):
        new_pixels[x, y] = find_nearest_color(tuple(pixels[x, y]), colors)

indexed_pixels = []
used_colors = {}
for x in range(new_pixels.shape[0]):
    indexed_pixels.append([])
    for y in range(new_pixels.shape[1]):
        r, g, b, a = new_pixels[x, y]
        color = [int(r), int(g), int(b)]
        color_index = colors.index(color)
        color_type = sorted_colors[color_index]
        default_block = block_colors[color_type][0]

        if used_colors.get(color_type) == None:
            used_colors[color_type] = default_block

        indexed_pixels[x].append(list(used_colors.keys()).index(color_type))

print(colour([200,200,0],"### Blocks"))
for color in used_colors.keys():
    print(colour(colors[sorted_colors.index(color)], color), used_colors[color])

print(colour([200,200,0],f'{"#"*10} count {"#"*10}'))
counter = {}
for x in range(new_pixels.shape[0]):
    for y in range(new_pixels.shape[1]):
        color = list(used_colors.keys())[indexed_pixels[x][y]]
        if counter.get(color) == None:
            counter[color] = 1
        else:
            counter[color] += 1

for color in counter.keys():
    value = counter[color]
    print(colour(colors[sorted_colors.index(color)], color), value)

# keys = list(used_colors.keys())
# keys.sort()
# total = 0

# for key in keys:
#     total += used_colors[key]
#     print(key, block_colors[sorted_colors[key-1]][0], used_colors[key])

new_img = Image.fromarray(new_pixels)
# new_img.save(f"{nome}_new.png")

