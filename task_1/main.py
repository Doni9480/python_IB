"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных будет свидетельствовать пустая строка.
"""

with open('user_text_file.txt', 'a+') as user_text:
    while True:
        user_inp = input('Введите текст: ')
        if user_inp != '':
            user_text.write(user_inp + '\n')
            user_text.seek(0)
            print(f'новые данные: {user_inp}')
        else:
            user_text.seek(0)
            print(f'\n {user_text.read()}')
            break
