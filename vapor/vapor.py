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


def porownaj_warstwy(data_first, data_second):
    dict_diff = {}
    for key, items in data_second.items():
        try:
            items_first = data_first[key]
        except KeyError:
            items_first = []
        dict_diff[key] = differ(items, items_first)
    return dict_diff


def slownik_to_list(data):
    dane_lista = []
    for nazwa_warstw, data_list in data.items():
        dane_lista.append(nazwa_warstw)
        for element in data_list:
            dane_lista.append(element)
        dane_lista.append('**')
    return dane_lista


def zapis_danych(filepath, params, data):
    warstwy = params + data
    with open(filepath, 'w') as outfile:
        lines = '\n'.join(warstwy)
        outfile.write(lines)
    outfile.close()


if __name__ == "__main__":
    file_old = '../_example_data/Warstwy_old'
    file_new = '../_example_data/Warstwy_new'
    data_old = wczytaj_warstwy(file_old)
    data_new = wczytaj_warstwy(file_new)
    params_old, data_old = parsuj_warstwy(data_old)
    params_new, data_new = parsuj_warstwy(data_new)
    data_old = warstwy_dane_slownik(data_old)
    data_new = warstwy_dane_slownik(data_new)
    diff_add = porownaj_warstwy(data_old, data_new)
    diff = slownik_to_list(diff_add)
    zapis_danych('./test.txt', params_new, diff)
