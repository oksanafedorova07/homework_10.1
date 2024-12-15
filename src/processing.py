from typing import Any, Iterable


def filter_by_state(dictionaries: Iterable[dict[Any, Any]], state: Any = "EXECUTED") -> list[dict[Any, Any]]:
    """Функция для выведения данных по определенному значению"""
    executed_list = []
    for index in dictionaries:
        if index["state"] == state:
            executed_list.append(index)
    return executed_list


def sort_by_date(dictionaries: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки по датам"""
    list_for_date = sorted(dictionaries, key=lambda x: x["date"], reverse=reverse)
    return list_for_date
