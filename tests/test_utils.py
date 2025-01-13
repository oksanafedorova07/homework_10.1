import json
from unittest.mock import patch

from src.utils import get_transactions
from typing import Any


@patch("builtins.open")
def test_read_file(mock_open: Any) -> Any:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == [{"test": "test"}]
    mock_file.read.return_value = json.dumps('{"DEBUG": true, "directory": "C:/Games/MudRunner/Media}')
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []
    mock_file.read.return_value = json.dumps([])
    assert get_transactions("C:/Users/Nurlan/IT/Проекты/mask_card2/data/operations.json") == []
