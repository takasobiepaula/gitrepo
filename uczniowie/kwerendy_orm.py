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
    query = (Uczen
    .select(Uczen.nazwisko, Uczen.klasa.klasa)
    .join(Klasa)
    .where(Uczen.klasa.klasa.endswith('A'))
    .order_by(Uczen.klasa.klasa.asc())
    )
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)
        
def kw03():
    query = (Ocena
    .select(Ocena.uczen.nazwisko, Ocena.ocena)
    .join(Uczen)
    .where(Ocena.uczen.nazwisko.startswith('B'))
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ocena)
        
def kw04():
    query =( Ocena
    .select(Ocena.uczen.nazwisko, fn.Count(Ocena.ocena).alias('ile'))
    .join(Uczen).where(Ocena.ocena == 1)
    .group_by(Ocena.uczen.nazwisko)
    .order_by(SQL('ile').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)
        
def kw05():
    query = (Uczen
    .select(Uczen.klasa.klasa, fn.Count(Uczen.id).alias('ile'))
    .join(Klasa)
    # .where(Ocena.ocena == 1)
    .group_by(Uczen.klasa.klasa)
    .order_by(SQL('ile').asc())
    )
    for obj in query:
        print(obj.klasa.klasa, obj.ile)
        
def kw06():
    fn.AVG()
    query = (Ocena
    .select(Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('srednia'))
    .join(Przedmiot)
    # .where(Ocena.ocena == egz.hum)
    .group_by(Ocena.przedmiot.przedmiot)
    .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.przedmiot.przedmiot, obj.srednia)
        
def kw07():
    fn.AVG()
    query = (Ocena
    .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
    .join(Uczen)
    # .where(Ocena.ocena == egz.hum)
    .group_by(Ocena.uczen.nazwisko)
    .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.srednia)
        
def kw08():
    fn.AVG()
    query = (Ocena
    .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
    .join(Uczen)
    .where(Uczen.nazwisko == "Szymczak")
    .group_by(Ocena.uczen.nazwisko)
    .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.srednia)

def main(args):
    baza.connect()
    
    kw08()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
