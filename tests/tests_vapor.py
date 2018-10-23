# -*- coding: utf-8 -*-

import pytest
from vapor.vapor import wczytaj_warstwy, porownaj_warstwy, differ

FILE_OLD = '../_example_data/Warstwy_old'
FILE_NEW = '../_example_data/Warstwy_new'
CONTENT = ['0  5.66728512000000E+0006  7.58192636000000E+0006  '
          '1.79999995231628E+0000  2.79649992470963E+0002    2 "15" 7#PUG',
           '0  5.66449709623493E+0006  7.58304541673917E+0006  '
           '1.50000000000000E+0000  3.59927992503304E+0002    7 "3-270/2;2" 7#PUG']


def test_wczytaj_warstwy():
    _, data = wczytaj_warstwy(FILE_OLD)
    assert data['EADTD 121'][0] == CONTENT[0]


def test_porownaj_warstwy_add():
    diff_add, _ = porownaj_warstwy(FILE_OLD, FILE_NEW)
    assert diff_add['EBUTN 121'][0] == CONTENT[1]


def test_differ():
    test_items1 = set(["A", "B", "C"])
    test_items2 = set(['A', 'B'])
    assert ['C'] == differ(test_items1, test_items2)
