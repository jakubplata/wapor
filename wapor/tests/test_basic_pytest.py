# -*- coding: utf-8 -*-

import pytest
import os
from wapor.src.basic import *
from wapor.tests.static import PARSER_DATA

FILE_READ = os.path.join(os.getcwd(), 'wapor', 'tests', '_example_data', 'file_read.txt')
FILE_READ_EMPTY = os.path.join(os.getcwd(), 'wapor', 'tests', '_example_data', 'file_read_empty.txt')
FILE_READ_CONTENT = ['it is', 'simple test file', '', 'check']
PARSER_CONTENT = ['it is', 'example file for', 'parser', '****',
                  'it divides', 'file for', 'params', '**', 'and data', '**']
PARSER_CONTENT_ERR = PARSER_CONTENT[0:3] + PARSER_CONTENT[4:]
PARSER_PARAMS = ['it is', 'example file for', 'parser', '****']
WRITE_DATA = ['to write', '**', 'in a', 'test file', '**']
PARAMS_DATA = ['it is', 'test data', '****']


def test_wczytaj_warstwy():
    data = wczytaj_warstwy(FILE_READ)
    assert data == FILE_READ_CONTENT


def test_wczytaj_warstwy_empty_file():
    data = wczytaj_warstwy(FILE_READ_EMPTY)
    assert data == []


def test_parsuj_warstwy_parametry():
    params, _ = parsuj_dane(PARSER_CONTENT)
    assert params == PARSER_PARAMS


def test_parsuj_warstwy_dane():
    _, data = parsuj_dane(PARSER_CONTENT)
    assert data == PARSER_DATA


def test_parsuj_warstwy_err():
    with pytest.raises(ValueError):
        params, data = parsuj_dane(PARSER_CONTENT_ERR)


def test_zapis_danych(tmpdir):
    file = tmpdir.join('ADD.txt')
    zapis_danych(file.strpath, PARAMS_DATA, WRITE_DATA)
    assert file.read() == 'it is\ntest data\n****\nto write\n**\nin a\ntest file\n**'