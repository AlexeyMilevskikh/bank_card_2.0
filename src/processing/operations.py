from datetime import datetime
from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с операциями
        reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный список операций
    """

    def get_date(op: Dict) -> datetime:
        return datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(operations, key=get_date, reverse=reverse)
