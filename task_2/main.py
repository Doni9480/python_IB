'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных
 о пользователе одной строкой.
'''

# def user_info(name, surname, year, city, email, telephone):
#     """
#
#     Вывод данных о пользователе одной строкой.
#
#     :param name:
#     :param surname:
#     :param year:
#     :param city:
#     :param email:
#     :param telephone:
#     :return:
#     """
#     return f'Имя: {name} || Фамилия: {surname} || Год рождения: {year} || Город проживания: {city} || Еmail: {email} || Телефон: {telephone}'


user_info = lambda name, surname, year, city, email,telephone: f'Имя: {name} || Фамилия: {surname} || Год рождения: {year} || Город проживания: {city} || Еmail: {email} || Телефон: {telephone}'

print(user_info(name='name123', surname='famile123', year='123', city='xCYTI', email='WWW.123.123.123.@GMAIL.COM',
                telephone='+996987654321'))
