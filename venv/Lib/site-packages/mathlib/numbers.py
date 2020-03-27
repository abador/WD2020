import math
from typing import Iterator


def lcm(a: int, b: int) -> int:
    """
    Find the least common multiple of a and b.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.
    """
    return a * b // math.gcd(a, b)


def modular_inverse(n: int, mod: int) -> int:
    """
    Find the modular inverse of n modulo mod.

    The algorithm is based on using the Extended Euclid Algorithm,
    to solve the diophantine equation n*x + mod*y = 1.
    """
    original_modulo = mod
    x = 1
    y = 0

    while n > 1:
        x, y = y, x - (n // mod) * y
        n, mod = mod, n % mod

    if x < 0:
        x += original_modulo

    return x


def fibonacci(n: int, a: int = 1, b: int = 1) -> int:
    """
    Return the nth Fibonacci number.

    n can be a negative integer as well.
    """
    values = {0: a, 1: b}

    def fib(m):
        if m in values:
            return values[m]

        k = m // 2
        if m & 1 == 1:
            value = fib(k) * (fib(k + 1) + fib(k - 1))
        else:
            value = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
        values[m] = value
        return value

    if n < 0:
        return ((-1) ** (1 - n)) * fib(-n)
    return fib(n)


def fibonacci_numbers(a: int = 0, b: int = 1) -> Iterator[int]:
    """
    Make an iterator that returns the Fibonacci numbers.

    The Fibonacci sequence is configurable, in the sense that the two
    initial values of it can be passed as arguments.
    """
    while True:
        yield a
        a, b = b, a + b


def binomial(n: int, k: int) -> int:
    """
    Calculate n choose k.

    Calculation is using the multiplicative formula, and is performed
    from the side that will minimise the number of calculations.
    """
    output = 1
    k = min(k, n - k)
    for t in range(k):
        output = (n - t) * output // (t + 1)

    return output
