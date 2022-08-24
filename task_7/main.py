"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
 название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

with open('data.txt', encoding='UTF-8') as file:
    lt = len(file.readlines())
    file.seek(0)
    my_list = []
    new_dict = {}
    sum_income = 0
    for i in range(lt):
        name, form, proceeds, costs = file.readline().split()
        summ = int(proceeds) - int(costs)
        if summ > 0:
            sum_income += summ
            new_dict[name] = summ
    my_list.append(new_dict)
    gen = int(sum_income / len(new_dict))
    my_list.append({'average_profit': gen})

with open('my_json_file.json', 'w') as fl:
    json.dump(my_list, fl)

print(my_list)
