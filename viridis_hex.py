import matplotlib.cm as cm

if __name__ == '__main__':
    color_map = cm.get_cmap('viridis')
    for r, g, b in color_map.colors:
        print(hex(int(r*255)), hex(int(g*255)), hex(int(b*255)))
    pass

