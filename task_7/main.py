'''
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Используйте написанную ранее функцию int_func().
'''


# def int_func(text):
#     new_text = []
#     for w in text.split():
#         word = lambda text: f'{text[0].upper()}{text[1:]}'
#         new_text.append(word(w))
#     return ' '.join(new_text)


int_func = lambda text: ' '.join([f'{w[0].upper()}{w[1:]}' for w in text.split()])

print(int_func('text text text'))
