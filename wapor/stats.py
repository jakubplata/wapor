# -*- coding: utf-8 -*-

from operator import itemgetter


def data_count(data):
    """
    Zwraca posortowane ilości elementów dla poszczególnych warstw
    :param data:
    :return:
    """
    stats = []
    for nazwa_warstwy, data_list in data.items():
        stats.append((nazwa_warstwy, len(data_list)))
    return sorted(stats, key=itemgetter(1), reverse=True)