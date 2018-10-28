# -*- coding: utf-8 -*-

"""
Aplikacja vapor [VVarstwy Porównanie] porównuje ze sobą dwa katalogi warstwy [eksport do formatu
tekstowego wielu warstw] programu EwMapa w celu stworzenia plików zawierających różnice.
Dane które zostały dodane oraz dane które zostały usunięte.

#Eksport współrzędnych z pełną precyzją, eksport operacji operatów, eksport parametrów warstw i podwarstw
"""

from collections import defaultdict


def wczytaj_warstwy(filename):
    """
    Wczytwanie plików z formatu tekstowego dla wielu warstw do postaci listy
    :param filename:
    :return:
    """
    with open(filename, 'r') as infile:
        file_data = [i.strip() for i in infile.readlines()]
    infile.close()
    return file_data


def parsuj_warstwy(warstwy):
    indeks = 0
    for nr, d in enumerate(warstwy):
        if d == '****':
            indeks = nr + 1
    warstwy_param = warstwy[0:indeks]
    warstwy_data = warstwy[indeks:]
    warstwy_data.insert(0, '**') # uzpelnienie wartosci bazowej dla listy
    return warstwy_param, warstwy_data


def warstwy_dane_slownik(warstwy_dane):
    data = defaultdict(list)
    for nr, row in enumerate(warstwy_dane):
        if row == '**' and nr < len(warstwy_dane)-1:
            key = warstwy_dane[nr+1]
        else:
            if row != key:
                data[key].append(row)
    return data


def differ(items1, items2):
    return list(set(items1).difference(set(items2)))


def porownaj_warstwy(file_old_data, file_new_data):
    param_old, data_old = parsuj_warstwy(file_old_data)
    param_new, data_new = parsuj_warstwy(file_new_data)
    data_old = warstwy_dane_slownik(data_old)
    for k, v in data_old.items():
        print(k, v,)
    data_new = warstwy_dane_slownik(data_new)
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
    data1 = wczytaj_warstwy(f1)
    data2 = wczytaj_warstwy(f2)
    porownaj_warstwy(data1, data2)