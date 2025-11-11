"""
Zadanie 5.2 z zestawu 5
testy do zadania znajduja sie w pliku test_fracs.py
"""

from math import gcd

def simplify(frac):
    """
    Upraszcza ulamek i zapewnia ze mianownik jest dodatni.
    """
    num, den = frac
    if den == 0:
        raise ZeroDivisionError("Mianownik nie moze byc 0")
    if num == 0:
        return [0, 1]
    g = gcd(num, den)
    num = num // g
    den = den // g
    if den < 0:
        num, den = -num, -den
    return [num, den]

def add_frac(frac1, frac2):
    """
    Zwraca sume dwoch ulamkow.
    """
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def sub_frac(frac1, frac2):
    """
    Zwraca roznice dwoch ulamkow.
    """
    num = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def mul_frac(frac1, frac2):
    """
    Zwraca iloczyn dwoch ulamkow.
    """
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return simplify([num, den])

def div_frac(frac1, frac2):
    """
    Zwraca iloraz dwoch ulamkow.
    """
    if frac2[0] == 0:
        raise ZeroDivisionError("Nie mozna dzielic przez 0")
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    return simplify([num, den])

def is_positive(frac):
    """
    Zwraca True, jesli ulamek jest dodatni.
    """
    num, den = simplify(frac)
    return num > 0

def is_zero(frac):
    """
    Zwraca True, jesli ulamek jest rowny 0.
    """
    return simplify(frac)[0] == 0

def cmp_frac(frac1, frac2):
    """
    Porownuje dwa ulamki, zwraca:
    -1 jesli frac1 < frac2,
     0 jesli frac1 == frac2,
    +1 jesli frac1 > frac2
    """
    f1 = simplify(frac1)
    f2 = simplify(frac2)
    a = f1[0] * f2[1]
    b = f2[0] * f1[1]
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

def frac2float(frac):
    """
    Konwertuje ulamek na float.
    """
    num, den = simplify(frac)
    return num / den

