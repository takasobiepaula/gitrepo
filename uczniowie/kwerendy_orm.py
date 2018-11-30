#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py

from uczniowie_model import *

def kw01():
   # query = Uczen.select().where(Uczen.imie.startswith('G'))
   # query = Uczen.select().where(Uczen.imie == 'Rafał')
   # query = Uczen.select().where(Uczen.imie == 'Rafał').count()
   # print(query)
    query = (Uczen
        .select()
        .where(Uczen.egz_mat.between(30,35))
        .order_by(Uczen.egz_mat.desc())
    )
    
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_mat)

def kw02():
    query = Uczen.select(Uczen.nazwisko, Uczen.klasa.klasa).join(Klasa).where(Uczen.klasa.klasa.endswith('A')).order_by(Uczen.klasa.klasa.asc())
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)
        
def kw03():
    query = Ocena.select(Ocena.uczen.nazwisko, Ocena.ocena).join(Uczen).where(Ocena.uczen.nazwisko.startswith('B'))
    for obj in query:
        print(obj.uczen.nazwisko, obj.ocena)
        
def kw04():
    query = Ocena.select(Ocena.uczen.nazwisko, fn.Count(Ocena.ocena).alias('ile')).join(Uczen).where(Ocena.ocena == 1).group_by(Ocena.uczen.nazwisko).order_by(SQL('ile').asc())
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)

def main(args):
    baza.connect()
    
    kw04()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
