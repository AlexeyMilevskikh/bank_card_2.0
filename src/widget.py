from .masks import get_mask_card_number, get_mask_account


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




from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 в формат "ДД.ММ.ГГГГ".

    :param date_str: Дата в формате "2024-03-11T02:26:18.671407".
    :return: Дата в формате "ДД.ММ.ГГГГ".
    """
    # Извлекаем строку даты
    dt = datetime.fromisoformat(date_str)

    # Форматируем дату в нужный формат
    return dt.strftime("%d.%m.%Y")