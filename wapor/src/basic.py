# -*- coding: utf-8 -*-


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


def parsuj_dane(dane):
    """
    Przetworzenie wczytanych warstw lub plików *.acs do postaci dwóch zbiorów,
    pierwszy zawiera parametry, natomiast drugi dane
    :param warstwy:
    :return:
    """
    indeks = 0
    for nr, d in enumerate(dane):
        if d == '****':
            indeks = nr + 1
    if indeks == 0:
        raise ValueError('Podano błędne dane do przetworzenia! - plik: ')
    warstwy_param = dane[0:indeks]
    warstwy_data = dane[indeks:]
    warstwy_data.insert(0, '**') # uzpelnienie wartosci bazowej dla listy
    return warstwy_param, warstwy_data