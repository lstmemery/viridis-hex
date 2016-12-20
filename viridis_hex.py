import matplotlib.cm as cm


def hex_colormap(name='viridis', N=256):
    """Convert the a matplotlib colormap into a list of hexadecimal codes.

    Args:
        name (str): The name of the colormap within matplotlib (default: Viridis)
        N (int): The number of different colors in the colormap you wish (colors will be evenly spread)

    Returns:
        list: A list of hexcodes representing different colors.
    """

    def hex_color(color_float):
        return str(hex(int(color_float * 255))).lstrip('0x').zfill(2).upper()

    color_map = cm.get_cmap(name, N)
    hex_color_map = []
    for color in color_map.colors:
        hex_color_map.append(''.join(['#',
                                      hex_color(color[0]),
                                      hex_color(color[1]),
                                      hex_color(color[2])]))
    return hex_color_map

if __name__ == '__main__':
    print(hex_colormap('magma', N=3))