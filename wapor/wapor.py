# -*- coding: utf-8 -*-

"""
Aplikacja wapor [Warstwy Porównanie] porównuje
ze sobą dwa katalogi warstwy [eksport do formatu
tekstowego wielu warstw] programu EwMapa
w celu stworzenia plików zawierających różnice.
Dane które zostały dodane oraz dane które zostały usunięte.

#Postać eksportu z programu EwMapa:
- współrzędnych z pełną precyzją
- eksport operacji operatów
- eksport parametrów warstw i podwarstw
"""

from collections import defaultdict
from copy import deepcopy
import os
import sys

HELPTEXT = """
W celu uruchomienia programu w wierszu poleceń należy podać
po nazwie skryptu, ścieżkę do folderu zawierającego pliki
wejściowe: Warstwy_old oraz Warstwy_new
Przykład użycia:
>>> python wapor.py ./data
"""


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
    """
    Przetworzenie wczytanych warstw do postaci dwóch zbiorów,
    pierwszy zawiera parametry, natomiast drugi dane
    :param warstwy:
    :return:
    """
    indeks = 0
    for nr, d in enumerate(warstwy):
        if d == '****':
            indeks = nr + 1
    if indeks == 0:
        raise ValueError('Podano błędne dane do przetworzenia! - plik: ')
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
    return dict(data) # defaultdict w przypadku braku klucza zwraca wartość domyślną (pusta lista)


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


def zapis_danych(filepath, params, data):
    """
    Zapis danych do pliku wynikowego zgodnie
    ze ścieżką podaną przez użytkownika, osobno należy podać
    parametry warstw oraz dane dla warstw
    :param filepath:
    :param params:
    :param data:
    :return:
    """
    warstwy = params + data
    with open(filepath, 'w') as outfile:
        lines = '\n'.join(warstwy)
        outfile.write(lines)
    outfile.close()


def out_display(header, data):
    """
    Wyświetalnie danych na ekranie, dla użytkownika
    :param header:
    :param data:
    :return:
    """
    print(header)
    for row in data:
        print(row)


def main(data_path):
    path = data_path
    f_old = os.path.join(path, 'Warstwy_old')
    f_new = os.path.join(path, 'Warstwy_new')
    d_old = wczytaj_warstwy(f_old)
    d_new = wczytaj_warstwy(f_new)
    try:
        params_old, data_old = parsuj_warstwy(d_old)
    except AttributeError as e:
        print(str(e) + f_old)
    try:
        params_new, data_new = parsuj_warstwy(d_new)
    except AttributeError as e:
        print(str(e) + f_new)
    data_old_dict = warstwy_dane_slownik(data_old)
    data_new_dict = warstwy_dane_slownik(data_new)
    diff_add, layer_add = porownaj_warstwy(data_old_dict, data_new_dict)
    diff_remove, layer_remove = porownaj_warstwy(data_new_dict, data_old_dict)
    diff_add_zapis = slownik_to_list(diff_add)
    diff_remove_zapis = slownik_to_list(diff_remove)
    zapis_danych('./DODANE.txt', params_new, diff_add_zapis)
    zapis_danych('./USUNIETE.txt', params_old, diff_remove_zapis)
    description = 'Warstwy występujące tylko w %s katalogu:'
    out_display(description % 'NOWYM', layer_add)
    out_display(description % 'STARYM', layer_remove)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(HELPTEXT)
    else:
        main(sys.argv[1])
        print('Koniec!')

