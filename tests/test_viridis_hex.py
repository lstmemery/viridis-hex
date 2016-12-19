from viridis_hex import *


def test_viridis_low():
    assert hex_colormap()[0] == "#440154"


def test_viridis_high():
    assert hex_colormap()[-1] == "#FDE724"
