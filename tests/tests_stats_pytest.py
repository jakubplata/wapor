# -*- coding: utf-8 -*-

from wapor.stats import *
from tests.static import SLOWNIK_DATA


def test_data_count():
    count = data_count(SLOWNIK_DATA)
    assert count == [('TEST 23', 2), ('LINIE 121', 1)]



