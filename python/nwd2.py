#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd.py
#  znaleźc największy współny dzielnik dwóch liczb naturalnych całkowitych
# wersja optymalna 


def nwd_2(a,b):
    while a > 0:
        a = a % b
        b = b - a
    return b


def main(args):
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    assert nwd_2(5, 10) == 5
    assert nwd_2(3, 9) == 3
    assert nwd_2(11, 33) == 11

    print ("Nwd {:d}, {:d} = {:d} ".format(a, b, nwd_2(a, b)))


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
