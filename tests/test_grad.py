import math

from lib import eq_float
from grad import grad


def test1():
    f = ["sin", "^2"]
    x = 10
    e = 0.00001

    left_val = grad(f, x)
    right_val = 2 * math.sin(x) * math.cos(x)

    assert eq_float(left_val, right_val, e)

def test2():
    f = ["^2", "sin"]
    x = 1.5
    e = 0.00001

    left_val = grad(f, x)
    right_val = math.cos(x * x) * 2 * x

    assert eq_float(left_val, right_val, e)

def test3():
    f = ["^2", "*3"]
    x = 4
    e = 0.00001

    left_val = grad(f, x)
    right_val = 6 * x

    assert eq_float(left_val, right_val, e)

def test4():
    f = ["exp", "^3"]
    x = 2
    e = 0.00001

    left_val = grad(f, x)
    right_val = 3 * math.exp(3 * x)

    assert eq_float(left_val, right_val, e)

def test5():
    f = ["*3", "exp"]
    x = 0.002
    e = 0.00001

    left_val = grad(f, x)
    right_val = 3 * math.exp(3 * x)

    assert eq_float(left_val, right_val, e)
