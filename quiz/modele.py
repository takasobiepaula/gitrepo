#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

baza_nazwa = 'quiz.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza

class Kategorie(BazaModel):
    kategoria = CharField(null=False)
    
class Pytania(BazaModel):
    pytanie = CharField(null=False)
    id_kat = ForeignKeyField(Kategoria, related_name='id')

class Odpowiedzi(BazaModel):
   id_p = ForeignKeyField(Kategorie, related_name='id')
   odpowiedzi = CharField(null=False)
   odpok = BooleanField(Default=0)
   

def main(args):
    if os.path.existics(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()
    baza.create_tables([Kategoria,Pytanie,Odpowiedzi])
    
    return 0
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))  

