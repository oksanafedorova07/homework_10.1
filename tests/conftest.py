import pytest


@pytest.fixture()
def dict_correct_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
    ]


@pytest.fixture()
def dict_correct_date1() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "gjfkuyojl"},
        {"id": 939719570, "state": "EXECUTED", "date": "********"},
    ]


@pytest.fixture()
def list_of_dicts() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def trans_list() -> list:
    return [
        {"currency": {"name": "USD", "code": "USD"}},
        {"currency": {"name": "USD", "code": "USD"}},
        {"currency": {"name": "руб.", "code": "RUB"}},
        {"currency": {"name": "USD", "code": "USD"}},
        {"currency": {"name": "руб.", "code": "RUB"}}
    ]