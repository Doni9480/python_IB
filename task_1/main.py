'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
'''

try:

    num_1, num_2 = map(int, input('Введите 2 числа через пробел: ').split())
    #
    #
    # def division(n1, n2):
    #     """
    #     Функция выполняет деление двух чисел
    #
    #     :param n1: - позиционные аргумент
    #     :param n2: - позиционные аргумент
    #     :return: - возвращает результат деления двух чисел
    #     """
    #     if n1 and n2:
    #         return n1 / n2
    #     else:
    #         return 'Деление на ноль!'

    division = lambda n1, n2: n1 / n2 if n1 and n2 else 'Деление на ноль!'


    print(division(num_1, num_2))
except ValueError:
    print('Не число!')
