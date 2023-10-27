#!/usr/bin/env python3.11
import argparse
from dataclasses import dataclass

def main(cmdline: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args(cmdline)
    result = extended_gcd(args.a,args.b)
    print(f"{result.gcd} = {result.coefficients[0]}*{args.a} + {result.coefficients[1]}*{args.b}")

@dataclass
class GcdResult:
    gcd: int
    coefficients: tuple[int, int]

def extended_gcd(a: int, b: int) -> GcdResult:
    def inner(a: int, b: int) -> GcdResult:
        assert a >= b > 0
        old_r, r = a, b
        s = 0
        old_s = 1
        t = 1
        old_t = 0

        while r != 0:
            q = old_r // r
            old_r, r = r, old_r % r
            old_s, s = s, old_s - q*s
            old_t, t = t, old_t - q*t

        return GcdResult(gcd=old_r, coefficients=(old_s, old_t))
    if a > b:
        return inner(a, b)
    result = inner(b, a) # pylint: disable=arguments-out-of-order
    result.coefficients = (result.coefficients[1], result.coefficients[0])
    return result

if __name__ == "__main__":
    main()
