from src.masks import get_mask_account, get_mask_card_number


def mask_account_cart(info: str) -> str:
    """Функция, которая маскирует номер карты или счета."""
    parts = info.split()
    if len(parts) < 2:
        return "Ошибка: некорректный вод."

    identifier = " ".join(parts[:-1])
    number = parts[-1]

    if identifier.lower().startswith("счет"):
        masked_info = get_mask_account(number)
        return f"{identifier} {masked_info}"
    else:
        masked_info = get_mask_card_number(number)
        return f"{identifier} {masked_info}"


def get_date(user_data: str) -> str:
    """Функция, которая изменяет формат даты"""
    if user_data.strip() == "":
        raise ValueError("Некорректная дата!")
    data_day = user_data.split("Т")[0]
    s1 = data_day.split("-")
    s2 = s1[2].split("T")[0]
    return s2 + "." + s1[1] + "." + s1[0]


print((get_date("2024-03-11T02:26:18.671487")))
print(mask_account_cart("Visa Platinum 8990922113665229"))
