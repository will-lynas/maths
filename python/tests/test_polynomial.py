from fractions import Fraction

import pytest

from maths_py.extended_gcd import polynomial

@pytest.mark.parametrize("test_input, expected", (
    ("0,0,2", [Fraction(2)]), # Leading zeros should be stripped
    ))
def test_polynomial_generation(test_input, expected):
    my_poly = polynomial.Polynomial(test_input)
    assert my_poly.coefficients == expected

@pytest.mark.parametrize("test_input, expected", (
    ("2,3,4", "2x²+3x+4"), # Normal
    ("3,2,1", "3x²+2x+1"), # 1 as a constant
    ("3,2,0", "3x²+2x"), # 0 as a constant
    ("", "0"), # Empty list
    ("0,0,0", "0"), # Just 0s
    ("0,2,2", "2x+2"), # 0 as leading coefficient
    ("1,1,1", "x²+x+1"), # 1s
    ("42,0,0,0,0,0,0,0,0,0,0,0,0,0,42", "42x¹⁴+42"), # Multi-digit superscript
    ))
def test_polynomial_representation_good(test_input, expected):
    my_poly = polynomial.Polynomial(test_input)
    assert str(my_poly) == expected

@pytest.mark.parametrize("a, b, result", (
    ("1,2,3", "7,8,9", "8x²+10x+12"), # Normal
    ("1,2", "7,8,9,10", "7x³+8x²+10x+12"), # Different lengths
    ))
def test_polynomial_addition(a, b, result):
    poly_a = polynomial.Polynomial(a)
    poly_b = polynomial.Polynomial(b)
    assert str(poly_a + poly_b) == result
