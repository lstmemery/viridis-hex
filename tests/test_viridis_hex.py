from viridis_hex import *
import pytest

def test_viridis_low():
    assert hex_colormap()[0] == "#440154"


def test_viridis_high():
    assert hex_colormap()[-1] == "#FDE724"

def test_viridis_n_3():
    assert hex_colormap(N=3) == ['#440154', '#20908C', '#FDE724']

def test_magma_n_3():
    assert hex_colormap(name='magma', N=3) == ['#000003', '#B63679', '#FBFCBF']
