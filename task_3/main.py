"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее
10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
подсчёт средней величины дохода сотрудников.
"""
with open('data.txt', 'rt', encoding='UTF-8') as data_file:
    a = data_file.readlines()
    my_dict = {}
    for e in a:
        n, val = e.split()
        my_dict[f'{n}'] = val

my_lis = [k for k, v in my_dict.items() if int(v) < 20000]
s = [int(v) for v in my_dict.values()]
print(my_lis)
print(round(sum(s) / len(s)))
