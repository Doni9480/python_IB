"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"

    def show_speed(self, speed=40):
        return f"Скорость {speed}"


class TownCar(Car):
    def show_speed(self, speed=40):
        if speed > 60:
            return f"Превышения скорости!\n Скорость: !{speed}!"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed=40):
        if speed > 40:
            return f"Превышения скорости!\n Скорость: !{speed}!"


class PoliceCar(Car):
    pass


ob = Car(80, 'red', 'bmw', True)
print(ob.show_speed(60))
print(ob.is_police)
print(ob.go())
print(ob.stop())
print(ob.turn('лево'))
ob2 = TownCar(600, 'red', 'BMW', False)
print(ob2.show_speed(61))
