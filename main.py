from PIL import Image
import numpy as np
import litemapy as lt
from data import colors, block_colors, sorted_colors

used_colors = {}

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

        # pr = int(pr)
        # pg = int(pg)
        # pb = int(pb)
        # print(p)
        distance = (r - pr)**2 + (g - pg)**2 + (b - pb)**2
        if distance < min_distance:
            min_distance = distance
            nearest_color = (pr, pg, pb, a)
    index = colors.index(list(nearest_color[:3])) + 1  # ESSE 1 É IMPORTANTE
    if index != 31:
        return (0, 0, 0, 0)
    # print(r,g,b)
    # print("E")
    # print(colors[index])
    # print("/"*10)
    if used_colors.get(index) is None:
        used_colors[index] = 1
    else:
        used_colors[index] += 1
    return nearest_color


img = Image.open(f"{nome}.png").convert("RGBA")
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
    print(key, block_colors[sorted_colors[key-1]][0], used_colors[key])
# print("total", np.floor(total/64), ",", total % 64, total/64)
# print(used_colors)
# used_colors_id.append()
# used_colors_id = {}
# for i in used_colors.keys():
#     color = used_colors.keys()[i]
#     count = used_colors[color]
#     used_colors_id[colors.index(list(color[:3]))] = count
# print(find_nearest_color(tuple(pixels[x][y]), colors))

new_img = Image.fromarray(new_pixels)
new_img.save(f"{nome}_new.png")
