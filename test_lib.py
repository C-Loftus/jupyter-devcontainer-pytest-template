from lib import Adder, Multiplier
import pytest

# Test your lib code here before using it interactively in your notebook

def test_adder():
    adder = Adder()

    assert adder.add(1, 1) == 1 + 1

    with pytest.raises(TypeError):
        adder.add("4", 3)


def test_multiplier():

    multi = Multiplier()

    assert multi.mult(3, 3) == 9

    with pytest.raises(TypeError):
        multi.mult("4", 3)