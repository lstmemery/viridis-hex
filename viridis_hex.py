import matplotlib.cm as cm


def hex_colormap(name='viridis', N=256):
    color_map = cm.get_cmap(name, N)
    hex_color_map = []
    for color in color_map.colors:
        hex_color_map.append(''.join(['#',
                                      hex_color(color[0]),
                                      hex_color(color[1]),
                                      hex_color(color[2])]))
    return hex_color_map


def hex_color(color_float):
    return str(hex(int(color_float * 255))).lstrip('0x').zfill(2).upper()
