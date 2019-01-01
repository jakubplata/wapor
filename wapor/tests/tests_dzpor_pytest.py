# -*- coding: utf-8 -*-

import pytest
from src.dzpor import *

SLOWNIK_PUNKTY = {'5-8526': {'dane_pod': '5581853.22 7552690.34 5581853.22 7552690.34  80 N N  7 1#250/12/12/90',
                             'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581853.22 7552690.34'},
                  '5-12321': {'dane_pod': '5581860.30 7552690.88 5581860.30 7552690.88  80 N N  7 1#250/12/12/90',
                              'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581860.30 7552690.88'},
                  '5-2184': {'dane_pod': '5581861.08 7552675.91 5581861.08 7552675.91  80 N N  7 1#250/12/12/90',
                             'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581861.08 7552675.91'},
                  '5-12323': {'dane_pod': '5581863.08 7552658.23 5581863.08 7552658.23  80 N N  7 1#1498/2002',
                              'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581863.08 7552658.23'},
                  '5-8090': {'dane_pod': '5581841.93 7552656.83 5581841.93 7552656.83  80 N N  7 1#250/12/12/90',
                             'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581841.93 7552656.83'},
                  '5-8091': {'dane_pod': '5581839.15 7552672.66 5581839.15 7552672.66  80 N N  7 1#250/12/12/90',
                             'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581839.15 7552672.66'},
                  '5-13010': {'dane_pod': '5581848.67 7552673.48 5581848.67 7552673.48  80 N N  7 1#250/12/12/90',
                              'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581848.67 7552673.48'},
                  '5-13011': {'dane_pod': '5581848.00 7552689.02 5581848.00 7552689.02  80 N N  7 1#250/12/12/90',
                              'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581848.00 7552689.02'},
                  '5-13012': {'dane_pod': '5581836.69 7552687.24 5581836.69 7552687.24  80 N N  7 1#250/12/12/90',
                              'dane_dod': '"",2,8,1,1,"",""', 'wsp': '5581836.69 7552687.24'},
                  }


def test_punkty_slownik():
    dict = punkty_slownik('./Dzialki.edz', './Punkty.acs')
    assert dict == SLOWNIK_PUNKTY