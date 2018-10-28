# -*- coding: utf-8 -*-

import pytest
from vapor.vapor import wczytaj_warstwy, porownaj_warstwy, differ, parsuj_warstwy, warstwy_dane_slownik

FILE_OLD = '../_example_data/Warstwy_old'
FILE_NEW = '../_example_data/Warstwy_new'
FILE_READ = '../_example_data/file_read.txt'
FILE_READ_EMPTY = '../_example_data/file_read_empty.txt'
FILE_READ_CONTENT = ['it is', 'simple test file', '', 'check']
CONTENT = ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
           '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _']
PARSER_CONTENT = wczytaj_warstwy('../_example_data/file_parser.txt')
PARSED_PRAMS, PARSED_DATA = parsuj_warstwy(PARSER_CONTENT)
PARSER_PARAMS = ['it is', 'example file for', 'parser', '****']
PARSER_DATA = ['**', 'it divides', 'file for', 'params', '**', 'and data', '**']


def test_wczytaj_warstwy():
    data = wczytaj_warstwy(FILE_READ)
    assert data == FILE_READ_CONTENT


def test_wczytaj_warstwy_empty_file():
    data = wczytaj_warstwy(FILE_READ_EMPTY)
    assert data == []


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
    assert diff_add['TEST 23'][0] == CONTENT[0]


def test_differ():
    test_items1 = set(["A", "B", "C"])
    test_items2 = set(['A', 'B'])
    assert ['C'] == differ(test_items1, test_items2)
