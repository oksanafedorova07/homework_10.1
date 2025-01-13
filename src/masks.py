import logging

from src.utils import PATH_TO_PROJECT

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "masks.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


def get_mask_card_number(card: str) -> str:
    """Возвращает реквизиты карты с зашифрованным номером"""
    counter = 0
    for num in card:
        if num.isdigit():
            counter += 1
    if counter == 16 and card[-16:].isdigit():
        logger.info("Получаем реквизиты карты с зашифрованным номером")
        slice_card = card[-10:-4]
        mask_card = card.replace(slice_card, "******")
        new_mask_card = mask_card[:-12] + " " + mask_card[-12:-8] + " " + mask_card[-8:-4] + " " + mask_card[-4:]
        return new_mask_card
    else:
        logger.error("Ошибка! некорректный ввод реквизитов карты")
        return "Некорректный ввод"


def get_mask_account(acc: str) -> str:
    """Возвращает реквизиты счета с зашифрованным номером"""
    counter = 0
    for num in acc:
        if num.isdigit():
            counter += 1
    if counter == 20 and acc[-20:].isdigit():
        logger.info("Получаем реквизиты счета с зашифрованным номером")
        slice_acc = acc[-20:-4]
        mask_acc = acc.replace(slice_acc, "**")
        return mask_acc
    else:
        logger.error("Ошибка! некорректный ввод реквизитов счета")
        return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_card_number("Discover 7269000803370165"))
    # print(get_mask_account("1234567890096548321"))