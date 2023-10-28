#!/usr/bin/env python3.11
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import zip_longest

def superscript(n: int) -> str:
    def inner(n: int) -> str:
        assert 0 <= n <= 9
        s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        return  s[n]
    return "".join(inner(int(c)) for c in str(n))


class Polynomial:
    """Store polynomials as a list of coefficients with a non-zero leading coefficient.
    The zero polynomial is represented by an empty list."""

    def __init__(self, coefficients: str | list[Fraction | float | int] | None = None):
        if not coefficients:
            self.coefficients = []
            return

        if isinstance(coefficients, str):
            self.coefficients = [Fraction(el) for el in coefficients.split(",")]
        else:
            self.coefficients = [Fraction(el) for el in coefficients]

        while self.coefficients and self.coefficients[0] == 0:
            self.coefficients.pop(0)


    def __str__(self) -> str:
        if not self.coefficients:
            return "0"
        out = []
        for i, val in enumerate(reversed(self.coefficients)):
            if val == 0:
                continue

            if i == 0:
                x_part = ""
            elif i == 1:
                x_part = "x"
            else:
                x_part = f"x{superscript(i)}"

            if val == 1 and i != 0:
                coeff = ""
            else:
                coeff = f"{val}"

            out.append(f"{coeff}{x_part}")
        return "+".join(reversed(out))


    def __add__(self, other: Polynomial) -> Polynomial:
        return Polynomial([
            sum(pair) for pair in
            reversed(list(zip_longest(
                reversed(self.coefficients),
                reversed(other.coefficients),
                fillvalue = Fraction(0))))
            ])


    @staticmethod
    def _divide(p1: Polynomial, p2: Polynomial) -> tuple[Polynomial, Polynomial]:
        raise NotImplementedError

    def __mod__(self, other: Polynomial) -> Polynomial:
        return self._divide(self, other)[1]

    def __floordiv__(self, other: Polynomial) -> Polynomial:
        return self._divide(self, other)[0]
