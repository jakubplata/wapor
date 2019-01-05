# -*- coding: utf-8 -*-

from wapor.src.stats import *
from wapor.tests.static import SLOWNIK_DATA


def test_data_count():
    count = data_count(SLOWNIK_DATA)
    assert count == [('TEST 23', 2), ('LINIE 121', 1)]


def test_sum_elements():
    total = sum_elements(SLOWNIK_DATA)
    assert total == 3

