'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''


def my_func(n1,n2,n3):
    new_lis = []
    new_lis.append(n1)
    new_lis.append(n2)
    new_lis.append(n3)
    print(new_lis)
    new_lis=sorted(new_lis)
    return f'{new_lis[-1]} + {new_lis[-2]} = {sum(new_lis[-2::])}'


print(my_func(3, 1, 2))
