from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, возвращая замаскированный номер.

    :param info: Строка с типом и номером карты или счета.
    :return: Замаскированный номер в формате, соответствующем типу.
    """
    # Убираем пробелы и разбиваем строку на части
    parts = info.split()

    # Предполагаем, что номер будет последним элементом
    number = parts[-1]

    # Проверяем, является ли последний элемент числом
    if number.isdigit():
        if "счет" in info.lower():
            masked_account = get_mask_account(number)
            return f"Счет {masked_account}"

        # Если это не счет, предполагаем, что это карта
        masked_card = get_mask_card_number(number)
        return info.replace(number, masked_card)
    return "Неверный формат информации"


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты в формат 'дд.мм.гггг'.

    :param date_string: Дата в формате ISO 8601.
    :return: Дата в формате 'дд.мм.гггг'.
    """
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
