from typing import Any

import pytest

from src.decorators import log, result_function


def test_log_func() -> Any:
    """Функция, тестирующая функцию возведения в степень с выводом в консоль"""

    @log("")
    def result_function(x: int, y: int) -> Any:
        return x**y

    result = result_function(2, 3)
    assert result == 8


def test_2_log_func() -> None:
    with pytest.raises(Exception):
        result_function()


def test_3_log_func() -> Any:
    """Функция, тестирующая функцию возведения в степень с выводом информации в файл"""

    @log("func_log.txt")
    def result_function(x: int, y: int) -> Any:
        return x**y

    result = result_function(1, 5)
    assert result == 1


def test_4_log_func(capsys: Any) -> Any:
    @log()
    def result_function(x: int, y: int) -> Any:
        return x**y

    result = result_function(2, 1)
    captured = capsys.readouterr()
    assert result == 2
    assert captured.out
