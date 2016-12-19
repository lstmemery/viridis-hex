from viridis_hex import *


def test_viridis_low():
    assert get_virdis()[0] == "#440154"


def test_viridis_high():
    assert get_viridis()[-1] == "FDE724"
