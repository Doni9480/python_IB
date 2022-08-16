"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём
формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо
запускать скрипт с параметрами.
"""
from sys import argv

script_nate, param1, param2, param3 = argv


def calculation(production=8, bid=150, premium=100):
    """
    Функция расчёта заработной платы сотрудника

    :param production: - выработка в часах
    :param bid: - ставка в час
    :param premium: - премия
    :return: (production * bid) + premium
    """
    return (production * bid) + premium


# calculation = lambda production=8, bid=150, premium=100: (production * bid) + premium

print(calculation(production=int(param1), bid=int(param2), premium=int(param3)))
