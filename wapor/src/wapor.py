# -*- coding: utf-8 -*-
from collections import defaultdict
from copy import deepcopy


def warstwy_dane_slownik(warstwy_dane):
    data = defaultdict(list)
    for nr, row in enumerate(warstwy_dane):
        if row == '**' and nr < len(warstwy_dane)-1:
            key = warstwy_dane[nr+1]
        else:
            if row != key:
                data[key].append(row)
    return dict(data) # defaultdict w przypadku braku klucza zwraca wartość domyślną pusta lista


def differ(items1, items2):
    return list(set(items1).difference(set(items2)))


def porownaj_warstwy(data_first, data_second):
    """
    Porównanie dwóch zbiorów danych w celu wychwycenia różnic
    Elementy dodane na warstwach otrzymamy gdy jako pierwszy
    zbiór podamy dane dotychczasowe a jako drugi zbiór dane aktualne.
    Dla elementów usuniętych kolejność zbiorów danych musi być odwrotna
    :param data_first:
    :param data_second:
    :return:
    """
    dict_diff = {}
    layers = []
    for key, items in data_second.items():
        try:
            items_first = data_first[key]
        except KeyError:
            layers.append(key)
            items_first = []
        dict_diff[key] = differ(items, items_first)
    return dict_diff, layers


def selektor_danych(data, selektor):
    """
    Możliwość wybrania danych tylko dla części warstw, selektor zawiera listę
    warstw które mają pozostać
    :param data:
    :param selektor:
    :return:
    """
    copy_data = deepcopy(data)
    if len(selektor) > 0:
        for nazwa_warstw, data_list in data.items():
            if nazwa_warstw not in selektor:
                del copy_data[nazwa_warstw]
        return copy_data
    else:
        return data


def slownik_to_list(data):
    """
    Przetworzenie słownika z danymi z warstw na listę
    w celu późniejszego zapisu do pliku
    :param data:
    :return:
    """
    dane_lista = []
    for nazwa_warstw, data_list in data.items():
        dane_lista.append(nazwa_warstw)
        for element in data_list:
            dane_lista.append(element)
        dane_lista.append('**')
    return dane_lista




