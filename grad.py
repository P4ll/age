import math
from typing import List


def der_sin(x: float) -> float:
    return math.cos(x)

def der_cos(x: float) -> float:
    return -math.sin(x)

def der_exp(x: float) -> float:
    return math.exp(x)

def der_sqrt(x: float) -> float:
    return 1 / (2 * math.sqrt(x))

def der_log(x: float) -> float:
    return 1 / x

def der_div(x: float) -> float:
    return -1 / x * x

def der_mul(x: str, a: float) -> float:
    n = int(x[1:])
    return n

def der_pow(s: str, x: float) -> float:
    n = int(s[1:])
    return n * math.pow(x, n - 1)

def der_add(x: str, a: float) -> float:
    return 0;

der_dict = {
    "sin": der_sin,
    "cos": der_cos,
    "exp": der_exp,
    "sqrt": der_sqrt,
    "1/x": der_div,
    "log": der_log,
    "^": der_pow,
    "*": der_mul,
    "+": der_add,
}

op_dict = {
    "sin": math.sin,
    "cos": math.cos,
    "exp": math.exp,
    "sqrt": math.sqrt,
    "1/x": lambda x: 1 / x,
    "log": math.log,
    "^": lambda x, s: math.pow(x, int(s[1:])),
    "*": lambda x, s: float(s[1:]) * x,
    "+": lambda x, s: float(s[1:]) + x,
}

def grad(f: List[str], x: float) -> float:
    if len(f) == 0:
        return 1;

    if f[0] in der_dict:
        der_op = der_dict[f[0]]
        op = op_dict[f[0]]
        val = der_op(x)
        return val * grad(f[1:], op(x))
    
    if f[0][0] in der_dict:
        der_op = der_dict[f[0][0]]
        op = op_dict[f[0][0]]
        val = der_op(f[0], x)
        return val * grad(f[1:], op(x, f[0]))

    raise NotImplementedError(f"Used not implemented op {f[0]}")

def eq_float(x: float, y: float, e: float) -> bool:
    return abs(x - y) < e

def test1():
    f = ["sin", "^2"]
    x = 10
    e = 0.00001

    assert eq_float(grad(f, x), 2 * math.sin(x) * math.cos(x), e)

def test2():
    f = ["^2", "sin"]
    x = 1.5
    e = 0.00001

    assert eq_float(grad(f, x), math.cos(x * x) * 2 * x, e)

def test3():
    f = ["^2", "*3"]
    x = 4
    e = 0.00001

    assert eq_float(grad(f, x), 6 * x, e)

def test4():
    f = ["exp", "^3"]
    x = 2
    e = 0.00001

    assert eq_float(grad(f, x), 3 * math.exp(3 * x), e)

def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
