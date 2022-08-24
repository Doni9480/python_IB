"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить её на экран.
"""
import random


def create_file(number):
    """
    Функция создаёт текстовый файл и записывает набор рандомных чисел, разделённых пробелами
    :param number: Количество чисел
    :return: None
    """
    with open('numm_file.txt', 'w') as fl:
        random_list_num = [str(random.randint(0, 100)) for i in range(number) if i != number]
        fl.write(' '.join(random_list_num))


def summation():
    """
    Функция подсчитывать сумму чисел в файле и выводить её на экран
    :return: выводит сумму чисел в файле
    """
    create_file(35)
    with open('numm_file.txt', 'r') as fl:
        text = fl.read()
        num_list = text.split()
        return sum([int(el) for el in num_list])


print(summation())
