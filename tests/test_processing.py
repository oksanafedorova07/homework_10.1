import pytest  # noqa

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(dict_correct_date: list) -> None:
    assert filter_by_state(dict_correct_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
    ]


def test_filter_by_state1(dict_correct_date1: list) -> None:
    assert filter_by_state(dict_correct_date1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "gjfkuyojl"},
        {"id": 939719570, "state": "EXECUTED", "date": "********"},
    ]


def test_sort_by_date(list_of_dicts: list) -> None:
    assert sort_by_date(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
