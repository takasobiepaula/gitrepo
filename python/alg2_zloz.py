#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = 0
    while a < 1 or a > 99:
        a = int(input("Podaj liczbę (1-99) : "))
        # for i in range(2, a + 3, 2):
        #     if a == i:
        #         print("Liczba jest parzysta")
        #         break
        # if i  > a:
        #     print("Liczba nieparzysta")

        # if i == 100:
        #     print("Liczba jest nieparzysta")

        i = 2
        while i <= a:
            if a == i:
                print("Liczba jest parzysta")
                break
            i += 2
        if i > a:
            print("Liczba jest nieparzysta")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
