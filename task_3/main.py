'''
  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
'''

number = int(input('Число n: '))
rez = 0

for i in range(1,number+1):
    r = str(number)*i
    rez += int(r)

print(rez)
