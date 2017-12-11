#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#


def potega_it(x,n):

    i = 1
    wynik = 1
    while i <= n:
        i = i + i

    return wynik

# potega_rek(a, 0) = 1  dla a różnego od 0
# potega_rek(a,n ) = potega_rek(a, n-1) * a dla n = N+

def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a



def main(args):
    x = float(input("Podaj podstawę"))
    n = int(input("Podaj wykładnik potęgi"))
    assert potega_it(1,2) == 1
    assert potega_it(2,2) == 4
    assert potega_it(3,3) == 27
    assert potega_it(4,2) == 16
    print("Wynik:")
    print("Potega:")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
