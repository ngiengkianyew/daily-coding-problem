import math
from fractions import Fraction


def get_egypt_frac(fraction, prev_fracs=list()):
    if fraction.numerator == 1:
        prev_fracs.append(fraction)

        return prev_fracs

    egpyt_frac = Fraction(1, math.ceil(
        fraction.denominator / fraction.numerator))
    prev_fracs.append(egpyt_frac)

    new_frac = fraction - egpyt_frac
    return get_egypt_frac(new_frac, prev_fracs)


# Tests
assert get_egypt_frac(Fraction(4, 13)) == \
    [Fraction(1, 4), Fraction(1, 18), Fraction(1, 468)]
