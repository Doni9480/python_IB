'''
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]

while True:

    user_inp = int(input('Введите новый элемент рейтинга: '))

    if user_inp in my_list:
        my_list.insert(my_list.index(user_inp),user_inp)
    else:
        if user_inp > my_list[0]:
            my_list.insert(0,user_inp)
        elif user_inp < my_list[-1]:
            my_list.append(user_inp)
        else:
            for i,el in enumerate(my_list):
                if user_inp > el:
                    my_list.insert(i,user_inp)
                    break
                else:
                    continue
    print(my_list)
