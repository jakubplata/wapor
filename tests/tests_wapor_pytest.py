# -*- coding: utf-8 -*-

import pytest
from wapor.wapor import *

FILE_OLD = './_example_data/Warstwy_old'
FILE_NEW = './_example_data/Warstwy_new'
FILE_READ = './_example_data/file_read.txt'
FILE_READ_EMPTY = './_example_data/file_read_empty.txt'
FILE_READ_CONTENT = ['it is', 'simple test file', '', 'check']
DATA_OLD = {'TEST 23': ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
                        '5.66443560667665E+0006  7.57924025966969E+0006       0  0.0000 _',
                        '0   20  5.66443560667665E+0006  7.57924025966969E+0006  '
                        '5.66443204588646E+0006  7.57924876935471E+0006       0  0.0000 _',
                        '0   20  5.66443204588646E+0006  7.57924876935471E+0006  '
                        '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _']}
DATA_NEW = {'TEST 23': ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
                        '5.66443560667665E+0006  7.57924025966969E+0006       0  0.0000 _',
                        '0   20  5.66443560667665E+0006  7.57924025966969E+0006  '
                        '5.66443204588646E+0006  7.57924876935471E+0006       0  0.0000 _',
                        '0   20  5.66443204588646E+0006  7.57924876935471E+0006  '
                        '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _',
                        '0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
                        '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _']}
CONTENT = ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
           '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _']
PARSER_CONTENT = ['it is', 'example file for', 'parser', '****',
                  'it divides', 'file for', 'params', '**', 'and data', '**']
PARSER_CONTENT_ERR = PARSER_CONTENT[0:3] + PARSER_CONTENT[4:]
PARSER_PARAMS = ['it is', 'example file for', 'parser', '****']
PARSER_DATA = ['**', 'it divides', 'file for', 'params', '**', 'and data', '**']

SLOWNIK_DATA = {'TEST 23': ['0 256 532', '0 256 896'], 'LINIE 121': ['0 456 789']}
WRITE_DATA = ['to write', '**', 'in a', 'test file', '**']
PARAMS_DATA = ['it is', 'test data', '****']


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


def test_parsuj_warstwy_err():
    with pytest.raises(ValueError):
        params, data = parsuj_warstwy(PARSER_CONTENT_ERR)


def test_warstwy_dane_slownik():
    dict = warstwy_dane_slownik(PARSER_DATA)
    assert dict == {'it divides': ['file for', 'params'], 'and data': ['**']}


def test_differ():
    test_items1 = set(["A", "B", "C"])
    test_items2 = set(['A', 'B'])
    assert ['C'] == differ(test_items1, test_items2)


def test_porownaj_warstwy():
    diff_add = porownaj_warstwy(DATA_OLD, DATA_NEW)
    assert diff_add['TEST 23'][0] == CONTENT[0]


def test_slownik_to_list():
    lista = slownik_to_list(SLOWNIK_DATA)
    assert lista == ['TEST 23', '0 256 532', '0 256 896', '**', 'LINIE 121', '0 456 789', '**']


def test_zapis_danych(tmpdir):
    file = tmpdir.join('ADD.txt')
    zapis_danych(file.strpath, PARAMS_DATA, WRITE_DATA)
    assert file.read() == 'it is\ntest data\n****\nto write\n**\nin a\ntest file\n**'



