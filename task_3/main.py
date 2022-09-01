"""
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def detailed_information(self):
        get_full_name = f'* Полное имя: {self.name} {self.surname}'
        get_total_income = f'* Дохода с учётом премии: {self._income["wage"] + self._income["bonus"]}'
        return f'Подробное информатция:\n {get_full_name}\n {get_total_income}'


obj = Position(name='a1', surname='a2', position='a3', income={"wage": 1000, "bonus": 2000})
print(obj.detailed_information())
