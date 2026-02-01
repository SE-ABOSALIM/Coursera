# Unit tests by pytest
import math_op
import pytest

#pass
def test_add():
    assert math_op.add(4, 11) == 15

#pass ||| to test just this func use -> python -m pytest 'Testing/test_math_op.py::test_sub'
def test_sub():
    assert math_op.sub(4, 11) == -7

#fail
def test_mul():
    assert math_op.mul(5, 4) == 20

#fail
def test_div():
    assert math_op.sub(10, 2) == 5