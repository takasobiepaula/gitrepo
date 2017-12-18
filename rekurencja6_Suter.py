#!/usr/bin/env python
# -*- coding: utf-8 -*-



    
def nwd_v3(a, b):
    if b == 0:
        return a
    return nwd_v3(b, a % b)


def main(args):
    a = int(input("podaj liczbę naturalą: "))
    b = int(input("podaj drugą liczbę naturalną: "))
    assert nwd_v3(5, 10) == 5
    assert nwd_v3(3, 9) == 3
    assert nwd_v3(11, 33) == 11
    print("NWD({:d}, {:d}) = {:d}".format(a, b, nwd_v3(a, b)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
