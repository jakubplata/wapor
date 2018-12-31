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

import datetime
import logging
import os
import sys
import traceback
from src.wapor import *
#from wapor.src.wapor import *

HELPTEXT = """
W celu uruchomienia programu w wierszu poleceń należy podać
po nazwie skryptu, ścieżkę do folderu zawierającego pliki
wejściowe: Warstwy_old oraz Warstwy_new
Przykład użycia:
>>> python wapor.py ./data
"""


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


def handler(exectype, value, tb):
    """
    Obsługa wszelkiego rodzaju wyjątków, zapisywanych do pliku .log
    :param exectype:
    :param value:
    :param tb:
    :return:
    """
    log = logging
    log.basicConfig(filename='./wapor.log', level=log.DEBUG, format='%(asctime)s %(message)s')
    log.critical('Error info')
    log.critical('Type: %s' % exectype)
    log.critical('Value: %s' % value)
    log.critical('Traceback: %s' % ''.join(traceback.format_tb(tb)))


def war_por(path, out_path):
    f_old = os.path.join(path, 'old', 'Warstwy')
    f_new = os.path.join(path, 'new', 'Warstwy')
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
    filenames_dict = {'dod': 'DODANE.txt', 'usu': 'USUNIETE.txt'}
    filenames_paths_dict = {k: os.path.join(out_path, v) for k, v in filenames_dict.items()}
    zapis_danych(filenames_paths_dict['dod'], params_new, diff_add_zapis)
    zapis_danych(filenames_paths_dict['usu'], params_old, diff_remove_zapis)
    return layer_add, layer_remove


def main(data_path):
    sys.excepthook = handler

    out_path = os.path.join(os.getcwd(), 'out')
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    out_path_date = os.path.join(out_path, date)
    os.mkdir(out_path_date)

    layer_add, layer_remove = war_por(data_path, out_path_date)

    description = 'Warstwy występujące tylko w %s katalogu:'
    out_display(description % 'NOWYM', layer_add)
    out_display(description % 'STARYM', layer_remove)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(HELPTEXT)
    else:
        main(sys.argv[1])
        print('Koniec!')