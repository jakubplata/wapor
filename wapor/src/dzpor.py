# -*- coding: utf-8 -*-

#TODO oprócz porównania warstw dodac mozliwosc porownywania baz dzialek/klasouzytkow
from collections import defaultdict
from src.basic import *


def punkty_slownik(file_edz, file_acs):
    slownik_pkt = defaultdict(dict)
    dz_dane = wczytaj_warstwy(file_edz)
    pkt_dane = wczytaj_warstwy(file_acs)
    _, pkt_dane_dod = parsuj_dane(pkt_dane) # pomijam dane parametryczne
    for i in pkt_dane_dod[1:]:
        atr = i.split(',')
        nr_pkt = atr[0].replace('"', '')
        dane_dod = ','.join(atr[1:])
        slownik_pkt[nr_pkt]['dane_dod'] = dane_dod
    for row in dz_dane:
        row_list = row.split()
        if len(row_list) >= 8:
            nr_pkt = row_list[0]
            dane_pod = ' '.join(row_list[1:])
            wsp = ' '.join(row_list[1:3])
            slownik_pkt[nr_pkt]['dane_pod'] = dane_pod
            slownik_pkt[nr_pkt]['wsp'] = wsp
    return dict(slownik_pkt)





if __name__ == "__main__":
    punkty_slownik('../tests/_example_data/Dzialki.edz', '../tests/_example_data/Punkty.acs')