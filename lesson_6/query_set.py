class QuerySet:
    def __init__(self):
        ...

    def __len__(self):
        """Длина QuerySet + Проверка того, является ли QuerySet пустым"""

    def filter(self, **kwargs):
        """Фильтрация запроса по полям"""
        ...

    def exclude(self, **kwargs):
        ...





    def __contains__(self, item):
        """*"""
