"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

with open('text.txt', 'r') as text_file:
    line = text_file.readlines()
    gen_words = 0
    gen_elems = 0
    for ind, lin in enumerate(line):
        new_i = lin.replace('\n', '')
        words = len(new_i.split())
        gen_words += words
        elem = len(new_i)
        gen_elems += elem
        print(f'Число слов в строке №{ind + 1}: {words}   Число элементов: {elem}')
    print(f"{'_'*60}\nОбщее количество: {len(line)} строк, {gen_words} слов, {gen_elems} элементов в файле!")
