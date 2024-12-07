from typing import Iterable, Any

def filter_by_state(dictionaries: Iterable[list[dict[Any, Any]]]), state: Any='EXECUTED' -> list[list[dict[Any, Any]]]:
"""Функция для выведения данных по определенному значению"""
executed_list = []
for i in dictionaries:
    if i['state'] == state:
        executed_list.append(i)
        return executed_list
