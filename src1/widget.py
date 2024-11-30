from src1.masks import get_mask_account, get_mask_card_number


def mask_account_cart(info: str) -> str:
    """Функция, которая маскирует номер карты или счета."""
    parts = info.split()
    if len(parts) < 2:
        return "Ошибка: некорректный вод."

    identifier = " ".join(parts[:-1])
    number = parts[-1]

    if identifier.lower().startswith("счет"):
        masked_info = get_mask_account(number)
        return f"{identifier} **{masked_info}"
    else:
        masked_info = get_mask_card_number(number)
        return f"{identifier} {masked_info}"


def get_date(date_str: str) -> str:
    """Функция, преобразует строку даты а нужный формат."""
    date_part = date_str.split("Т")[0]  # Берем только дату
    year, month, day = date_str.split("-")
    return f"{day}.{month}.{year}"


user_input = input("Введите номер карты или номер счета: ")
masked_output = mask_account_cart(user_input)
print(masked_output)

print((get_date("2024-03-11T02:26:18.671487")))
