'''
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input()
'''

new_lis = input('Введите данные через пробел: ').split()

print(new_lis)
for i in range(0, len(new_lis) - 1, 2):
    i1 = new_lis[i]
    new_lis[i] = new_lis[i + 1]
    new_lis[i + 1] = i1
print(new_lis)
