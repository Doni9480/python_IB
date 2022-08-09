'''
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и dict
'''
while True:
    try:
        option = input('\nЧтобы выйти из цикла введите - stop \nВыберите вариант list>(1) или dict>(2): ')

        if option == 'stop':
            break
        else:
            user = int(input('Введите месяц в виде целого числа от 1 до 12: '))
            if int(option) == 2:
                months = {
                    'зима': [12, 1, 2],
                    'весна': [3, 4, 5],
                    'лето': [6, 7, 8],
                    'осень': [9, 10, 11]
                }

                for name, new_lis in months.items():
                    if user in new_lis:
                        print(name)

            elif int(option) == 1:

                months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

                if user in months[0:3]:
                    print('зима')
                elif user in months[3:6]:
                    print('весна')
                elif user in months[6:9]:
                    print('лето')
                elif user in months[9:]:
                    print('осень')
    except ValueError:
        print('Правельно введите значения!')
        continue
