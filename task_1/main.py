'''
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
 Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

'''

lis = [99, '12', True, [1, 2, 3], ('3'), {'DF'}, {1: 'X', 2: 'T'},None]

print(f'Список {lis}')
for i,e in enumerate(lis):
    print(f'Индех {i} => Тип данных: {type(e)}')