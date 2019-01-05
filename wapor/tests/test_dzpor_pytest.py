# -*- coding: utf-8 -*-

import pytest
import os
from wapor.src.dzpor import *
from wapor.tests.static import SLOWNIK_PUNKTY, SLOWNIK_PUNKTY_NEW, SLOWNIK_ROZNICE


def test_punkty_slownik():
    dz = os.path.join(os.getcwd(), 'wapor', 'tests', '_example_data', 'old', 'Dzialki.edz')
    pkt = os.path.join(os.getcwd(), 'wapor', 'tests', '_example_data', 'old', 'Punkty.acs')
    dict = punkty_slownik(dz, pkt)
    assert dict == SLOWNIK_PUNKTY


def test_porownaj_dzialki():
    dict_por = porownaj_dzialki(SLOWNIK_PUNKTY, SLOWNIK_PUNKTY_NEW)
    assert dict_por == SLOWNIK_ROZNICE