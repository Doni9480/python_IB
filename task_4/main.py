"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

with open('file_a.txt', 'r', encoding='UTF-8') as file1:
    s_line = len(file1.readlines())
    file1.seek(0)
    while s_line - 1 != -1:
        line = file1.readline()
        with open('file_b.txt', 'a+', encoding='UTF-8') as file2:
            if 'One' in line:
                file2.write(line.replace('One', 'Один'))
            elif 'Two' in line:
                file2.write(line.replace('Two', 'Два'))
            elif 'Three' in line:
                file2.write(line.replace('Three', 'Три'))
            elif 'Four' in line:
                file2.write(line.replace('Four', 'Четыре'))
            file2.seek(0)
            rez = file2.read()
        s_line -= 1
    print(rez)
