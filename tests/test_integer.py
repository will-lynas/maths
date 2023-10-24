import pytest

from maths_py.extended_gcd.integer import main

@pytest.mark.parametrize("inp, expected", (
    ("24 8", "8 = 0*24 + 1*8"), # Normal
    ("8 24", "8 = 1*8 + 0*24"), # Reversed
    ("1 1", "1 = 1*1 + 0*1"), # Same number
    ))
def test_main(capfd, inp, expected):
    main(inp.split(" "))
    stdout, _ = capfd.readouterr()
    assert stdout.strip() == expected
