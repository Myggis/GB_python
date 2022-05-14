# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

#time.sleep для задержки сигнала (import time)



class TrafficLight:
    # Атрибут класса
    __trafficLight_color = ['Красный', 'Жёлтый', 'Зелёный']

    # Метод класса
    def running(self):
        import time
        print(f'Загорается {self.__trafficLight_color[0]} цвет светофора')
        time.sleep(7)
        print(f'Загорается {self.__trafficLight_color[1]} цвет светофора')
        time.sleep(2)
        print(f'Загорается {self.__trafficLight_color[2]} цвет светофора')
        time.sleep(5)


# Объект (экземпляр) класса
t1 = TrafficLight()
t1.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    # Конструктор
    def __init__(self, _lenght,  _width):
        self._lenght = _lenght     # атрибут экземпляра
        self._width = _width     # атрибут экземпляра
        result = int((self._width * self._lenght * 25 * 5))
        if result < 1000:
            print(f'необходимая масса асфальта - {result} кг.')
        else:
            result = int(result/1000)
            print(f'необходимая масса асфальта - {result} т.')

r1 = Road(20, 5000)




# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
    # Атрибут класса - Нет

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name    # Атрибут экземпляра
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}



class Position(Worker):
    pass

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_full_salary(self):
        full_salary = self._income['wage'] + self._income['bonus']
        print(f'Полная заработная плата (с премией): {full_salary}')


p1 = Position('Iggy', 'Myg', 'Analist', 100, 25)

p1.get_full_name()
p1.get_full_salary()

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def car_go(self):
        print(f'машина {self.name} поехала')

    def car_stoped(self):
        print(f'машина {self.name} остановилась')

    # Если направление через инпут
    # def car_turn(self):
    #     while True:
    #         try:
    #             qwe = int(input('Напишите куда повернуть "1" - налево, "2" - направо: '))
    #             if qwe == 1:
    #                 print(f'машина {self.name} повернула налево')
    #                 break
    #             if qwe == 2:
    #                 print(f'машина {self.name} повернула направо')
    #                 break
    #             if qwe != 1 and qwe != 2:
    #                 print('НЕВЕРНЫЙ ВВОД!ВЫ ВВЕЛИ НЕ 1 и НЕ 2')
    #         except ValueError:
    #             print('НЕВЕРНЫЙ ВВОД!ВЫ ВВЕЛИ НЕ ЧИСЛО')

    # если направление передаем параметром
    def car_turn(self, turn):
        print(f'машина {self.name} повернула {turn}')

    def show_speed(self):
        print(f'текущая скорость машины {self.name} - {self.speed}')

class Town_car(Car):

    def show_speed(self):
        if self.speed > 60:
            print('ВЫ ПРЕВЫСИЛИ СКОРОСТЬ!!!')
        print(f'текущая скорость машины {self.name} - {self.speed}')

class Sport_car(Car):
    pass

class Work_car(Car):

    def show_speed(self):
        if self.speed > 40:
            print('ВЫ ПРЕВЫСИЛИ СКОРОСТЬ!!!')
        print(f'текущая скорость машины {self.name} - {self.speed}')

class PoliceCar(Car):
    pass



car1 = Car(200, 'белая', 'Mazda', False)

town_car1 = Town_car(70, 'белая', 'Reno', False)
town_car2 = Town_car(50, 'синяя', 'Lada', False)

work_car1 = Work_car(70, 'черная', 'Камаз', False)
work_car2 = Work_car(30, 'красная', 'Зил', False)



car1.car_go()
car1.car_stoped()
# car1.car_turn()   # если направление через инпут
car1.car_turn('налево') # если направление передаем параметром
car1.show_speed()

town_car1.car_go()
town_car1.car_stoped()
town_car1.car_turn('налево')
town_car1.show_speed()

town_car2.car_go()
town_car2.car_stoped()
town_car2.car_turn('направо')
town_car2.show_speed()

work_car1.car_go()
work_car1.car_stoped()
work_car1.car_turn('налево')
work_car1.show_speed()

work_car2.car_go()
work_car2.car_stoped()
work_car2.car_turn('направо')
work_car2.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():

    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки РУЧКОЙ')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки КАРАНДАШОМ')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки МАРКЕРОМ')

pen1 = Pen('red')
pen1.draw()

Pencil1 = Pencil('red')
Pencil1.draw()

Handle1 = Handle('red')
Handle1.draw()
