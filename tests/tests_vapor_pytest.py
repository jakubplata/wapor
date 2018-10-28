# -*- coding: utf-8 -*-

import pytest
from vapor.vapor import wczytaj_warstwy, porownaj_warstwy, differ, parsuj_warstwy, warstwy_dane_slownik

FILE_OLD = '../_example_data/Warstwy_old'
FILE_NEW = '../_example_data/Warstwy_new'
FILE_READ = '../_example_data/file_read.txt'
FILE_READ_CONTENT = ['it is', 'simple test file', '', 'check']
CONTENT = ['0  5.66728512000000E+0006  7.58192636000000E+0006  '
          '1.79999995231628E+0000  2.79649992470963E+0002    2 "15" 7#PUG',
           '0  5.66449709623493E+0006  7.58304541673917E+0006  '
           '1.50000000000000E+0000  3.59927992503304E+0002    7 "3-270/2;2" 7#PUG']
PARSER_CONTENT = wczytaj_warstwy('../_example_data/file_parser.txt')
PARSED_PRAMS, PARSED_DATA = parsuj_warstwy(PARSER_CONTENT)
PARSER_PARAMS = ['it is', 'example file for', 'parser', '****']
PARSER_DATA = ['**', 'it divides', 'file for', 'params', '**', 'and data', '**']


def test_wczytaj_warstwy():
    data = wczytaj_warstwy(FILE_READ)
    assert data == FILE_READ_CONTENT


def test_parsuj_warstwy_parametry():
    params, _ = parsuj_warstwy(PARSER_CONTENT)
    assert params == PARSER_PARAMS


def test_parsuj_warstwy_dane():
    _, data = parsuj_warstwy(PARSER_CONTENT)
    assert data == PARSER_DATA


def test_warstwy_dane_slownik():
    dict = warstwy_dane_slownik(PARSED_DATA)
    assert dict == {'it divides': ['file for', 'params'], 'and data': ['**']}


def test_porownaj_warstwy_add():
    data_old = wczytaj_warstwy(FILE_OLD)
    data_new = wczytaj_warstwy(FILE_NEW)
    diff_add, _ = porownaj_warstwy(data_old, data_new)
    assert diff_add['EBUTN 121'][0] == CONTENT[1]


def test_differ():
    test_items1 = set(["A", "B", "C"])
    test_items2 = set(['A', 'B'])
    assert ['C'] == differ(test_items1, test_items2)
