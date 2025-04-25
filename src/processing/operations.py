from typing import List, Dict, Optional


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
