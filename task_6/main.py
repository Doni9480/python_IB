'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
'''

# def int_func(text):
#     text = f'{text[0].upper()}{text[1:]}'
#     return text

int_func = lambda text: f'{text[0].upper()}{text[1:]}'

print(int_func('text'))
