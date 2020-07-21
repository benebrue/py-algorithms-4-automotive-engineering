from pytest import approx
from my_source import euclid

def test_simple_test():
    assert(euclid([1, 1], [1, 1]) == approx(0))

def test_simple_test_2():
    assert(euclid([1, 2], [5, -1]) == approx(5))

def test_simple_test_3():
    assert(euclid([0, 0], [1, 1]) == approx(0))