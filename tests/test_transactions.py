from unittest.mock import mock_open, patch

import pandas as pd
from typing_extensions import AnyStr

from src.transactions import read_csv, read_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="Date,Description,Amount\n2025-01-01,Salary,3000\n2025-01-05,Groceries,-150\n",
)
def test_read_csv(mock_file):
    """Тест для функции read_csv с использованием mock"""
    expected_result = [
        {"Date": "2025-01-01", "Description": "Salary", "Amount": "3000"},
        {"Date": "2025-01-05", "Description": "Groceries", "Amount": "-150"},
    ]
    result = read_csv("mock_file.csv")
    assert result == expected_result


test_read_csv()


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    """Тест для функции read_excel с использованием mock"""
    mock_read_excel.return_value = pd.DataFrame(
        {"Date": ["2025-01-01", "2025-01-05"], "Description": ["Salary", "Groceries"], "Amount": [3000, -150]}
    )

    result = read_excel("mock_file.xlsx")

    expected_result = ["Date", "Description", "Amount"]
    assert list(result.keys()) == expected_result


test_read_excel()
