#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def losuj(ileliczb, maksliczb):
    liczby = []  # pusta lista

    ile = 0  # ilośc unikalnych liczb
    # for i in range(ileliczb):

    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1
    return liczby


def pobierz_typy(ileliczb):
    # pobieranie typów uzytkownika
    typy = set()  # pusty zbiór
    # for i in random(ileliczb):
    ile = 0
    while ile < ileliczb:
        typ = int(input('Podaj typ: '))
        if typ not in typy:
            typy.add(typ)
            ile += 1
    return typy


def main(args):
    ileliczb = int(input('Ile liczb chcesz zobaczyć?'))
    maksliczb = int(input('Maksymalna losowana liczba :'))

    while ileliczb > maksliczb or ileliczb < 1:
        ileliczb = int(input('Ile liczb chcesz zgadnąć z %s ?' % maksliczb))

    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)

    print(liczby)
    print(typy)

    trafione = set(liczby) & typy
    print(trafione)

    print('Trafiłeś', len(trafione))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
