# -*- coding: utf-8 -*-

import pytest
from wapor.tests.static import SLOWNIK_DATA, PARSER_DATA
from wapor.src.wapor import *


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
                        '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _'],
            'TEST 121': ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
                        '5.66443560667665E+0006  7.57924025966969E+0006       0  0.0000 _'],
            'TEST2 23': []}
CONTENT = ['0   20  5.66444643561727E+0006  7.57924543273049E+0006  '
           '5.66444287482708E+0006  7.57925352857065E+0006       0  0.0000 _']
WRITE_DATA = ['to write', '**', 'in a', 'test file', '**']
PARAMS_DATA = ['it is', 'test data', '****']


def test_warstwy_dane_slownik():
    dict = warstwy_dane_slownik(PARSER_DATA)
    assert dict == {'it divides': ['file for', 'params'], 'and data': ['**']}


def test_differ():
    test_items1 = set(["A", "B", "C"])
    test_items2 = set(['A', 'B'])
    assert ['C'] == differ(test_items1, test_items2)


def test_porownaj_warstwy():
    diff_add, _ = porownaj_warstwy(DATA_OLD, DATA_NEW)
    assert diff_add['TEST 23'][0] == CONTENT[0]


def test_porownaj_warstwy_braki():
    _, diff_layer = porownaj_warstwy(DATA_OLD, DATA_NEW)
    assert diff_layer == ['TEST 121', 'TEST2 23']


def test_selektor_danych():
    sd = selektor_danych(SLOWNIK_DATA, ['TEST 23'])
    assert sd == {'TEST 23': ['0 256 532', '0 256 896']}


def test_slownik_to_list():
    lista = slownik_to_list(SLOWNIK_DATA)
    assert lista == ['TEST 23', '0 256 532', '0 256 896', '**', 'LINIE 121', '0 456 789', '**']


def test_zapis_danych(tmpdir):
    file = tmpdir.join('ADD.txt')
    zapis_danych(file.strpath, PARAMS_DATA, WRITE_DATA)
    assert file.read() == 'it is\ntest data\n****\nto write\n**\nin a\ntest file\n**'



