# -*- coding: utf-8 -*-

"""
Aplikacja vapor [VVarstwy Porównanie] porównuje ze sobą dwa katalogi warstwy [eksport do formatu
tekstowego wielu warstw] programu EwMapa w celu stworzenia plików zawierających różnice.
Dane które zostały dodane oraz dane które zostały usunięte.

#Eksport współrzędnych z pełną precyzją, eksport operacji operatów, eksport parametrów warstw i podwarstw
"""

from collections import defaultdict


def wczytaj_warstwy(filename):
    data = defaultdict(list)
    with open(filename, 'r') as infile:
        file_data = [i.strip() for i in infile.readlines()]
    infile.close()
    indeks = 0
    for nr, d in enumerate(file_data):
        if d == '****':
            indeks = nr + 1
    param = file_data[0:indeks]
    rest = file_data[indeks:]
    rest.insert(0, '**') # uzpelnienie wartosci bazowej dla listy
    for nr, row in enumerate(rest):
        if row == '**' and nr < len(rest)-1:
            key = rest[nr+1]
        else:
            if row != key:
                data[key].append(row)
    return param, data


def differ(items1, items2):
    return list(set(items1).difference(set(items2)))


def porownaj_warstwy(file_old, file_new):
    param_old, data_old = wczytaj_warstwy(file_old)
    param_new, data_new = wczytaj_warstwy(file_new)
    dict_diff_add = {}
    dict_diff_remove = {}
    for key, items in data_new.items():
        try:
            items_old = data_old[key]
        except KeyError:
            print('W pierwotnych danych brak warstwy: {key}'.format(key=key))
        else:
            dict_diff_add[key] = differ(items, items_old)
            dict_diff_remove[key] = differ(items_old, items)
    return dict_diff_add, dict_diff_remove


if __name__ == "__main__":
    f1 = '../_example_data/Warstwy_old'
    f2 = '../_example_data/Warstwy_new'
    porownaj_warstwy(f1, f2)