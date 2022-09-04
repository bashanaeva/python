# class Point:
#    color = 'red'
#    circles = 2
#
#
#     def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#
#    def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
#    def get_name(self):
#         return self.x, self.y
#
# a = Point(1, 2)
# print(a.__dict__)


# ##Пример 2

## cls ссылается на сам класс Point, а  self ссылается на экземпляр класса
# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("вызов __new__ для " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self,x=0, y=0):
#         print("вызов __init__" + str(self))
#         self.x = x
#         self.y = y
#
#
# p = Point(1,2)
# print(p)


##Пример из собеседования(реализауия класса для эффективного вычисления скалярного произведения разряженных веторов)
##скалярное произведение - это сумма попарных произведений соответствующих векторов
## вектора могут иметь большой размер ,ничтожная часть из которых отлична от нуля(разряженные вектора)
# class SparseVector:
#     def __init__(self, nums:  [int]):
#         self.nums = nums
#
#     def dotProduct(self, vec: 'SparseVector') -> int:
#          return sum([x*y for x,y in zip(self.nums, vec.nums)])
#
# nums1 = [1,2,0,4]
# nums2 = [8,0,3,5]
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# print(v1)
# print(v2)





##Пример 3
# рассмотрим работу патерна проектиравания Singleton.
#Используется когда должен существовать только один экземпляр
#
# class DataBase:
#
#     __instence = None   #будет ссылкой на экземпляр класса.Если его не будет,то атрибут будет None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instence is None:
#            cls.__instence = super().__new__(cls)
#
#         return cls.__instence
#
#     def __del__(self):
#         DataBase.__instence = None
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def connect(self):
#         print(f"соединение с БД:{self.user},{self.password},{self.port}")
#
# # close read write также называют некими заглушками
#     def close(self):
#         print("прервем соединение с БД")
#
#     def read(self):
#         return "данные из БД"
#
#     def write(self,data):
#         print(f"запись в БД {data}")

# db = DataBase('root','1234',80)
# db2 = DataBase('root2','5678',40)
# print(id(db), id(db2)) # 2045650259776 2045650259776

# db.connect() #соединение с БД:root2,5678,40
# db2.connect()# соединение с БД:root2,5678,40


### DZ OOP
#1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.


# from time import sleep
# from datetime import datetime as dt
#
# class TrafficLight:
#     """ Класс светофора, реализующий свое переключение при запуске running( """
#     __color_and_time = {'red': 7, 'yellow': 2, 'green': 5}
#     __color = ''
#
#     def running(self):
#         """ Метод запусключения светофора """
#         for color, sw_time in self.__color_and_time.items():
#             self.__color = color
#             start_color_and_time = dt.now()
#
#             print(f"светофор переключился на '{self.__color}'"
#                   f"на {sw_time} сек")
#
#             sleep(sw_time)
#
#             print(f"светофор будет гореть '{self.__color}' цветом' еще "
#                   f"{(dt.now() - start_color_and_time).seconds} сек")
#
#
# if __name__ == '__main__':
#     tl = TrafficLight()
#     tl.running()


####Задание 2.
##определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
##использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна
# class Road:
#
#     def __init__(self, lenght, width):
#        self._lenght = lenght
#        self._width = width
#        self.massa_for_1m = 25
#        self.thickness = 5
#
#     def get_resullt(self):
#          return f"{self._lenght * self._width * self.massa_for_1m * self.thickness} тонн асфальта понадобиться,чтобы покрыть дорогу"
#
#
#
# p = Road(20,6)
# print(p.get_resullt())

##Задание 3
# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.


# class Worker:
#
#     def __init__(self, name, sername, position, wage, bonus):
#        self.name = name
#        self.sername = sername
#        self.position = position
#        self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def __init__(self, name, sername, position, wage, bonus):
#         super().__init__(name, sername, position, wage, bonus)

#     def get_full_name(self):
#         return self.name + ' ' + self.sername
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
# p = Position('Alexandr', 'Usachov', 'it-manager', 80000, 11000)
# print(p.get_full_name())
# print(p.get_total_income())
# print(p.position)



###Задание 4
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# class Car:
#
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def show_speed(self):
#         return f"На данный момент скорость автомобиля {self.name} составляет {self.speed }"
#
#     def go(self):
#         return f"{self.name} машина поехала"
#
#     def stop(self):
#         return f"{self.name} машина остановилась"
#
#     def turn_left(self):
#         return f"{self.name} машина повернула налево"
#
#     def turn_right(self):
#         return f"{self.name} машина повернула направо"
#
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#        super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f"На данный момент скорость автомобиля {self.name} составляет {self.speed }")
#
#         if self.speed > 60:
#             return(f'водитель автомобиля {self.name} превысил положенную скорость')
#
#         if self.speed < 60:
#             return(f'водитель автомобиля {self.name} придерживается положенной скорости')
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#        super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#        super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f"На данный момент скорость автомобиля {self.name} составляет {self.speed }")
#
#         if self.speed > 40:
#             return(f'водитель автомобиля {self.name} превысил положенную скорость')
#
#         if self.speed < 40:
#             return(f'водитель автомобиля {self.name} придерживается положенной скорости')
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} полицейская машина'
#         else:
#             return f'{self.name} не является полицейской машиной'
#
# audi = SportCar(100, 'Red', 'Audi', False)
# oka = TownCar(30, 'White', 'Oka', False)
# lada = WorkCar(70, 'Rose', 'Lada', True)
# ford = PoliceCar(110, 'Blue',  'Ford', True)
#
# print(lada.turn_left())
# print(f'Если {oka.turn_right()}, {audi.stop()}')
# print(f'{lada.go()} with speed exactly {lada.show_speed()}')
# print(f'{lada.name} is {lada.color}')
# print(f'Is {audi.name} a police car? {audi.is_police}')
# print(f'Is {lada.name}  a police car? {lada.is_police}')
# print(audi.show_speed())
# print(oka.show_speed())
# print(f'{ford.name} точно полицейская машина? {ford.is_police}')
# print(ford.show_speed())



####Задание 5
##3Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


#
# class Stationary:
#     def __init__(self,title):
#         self.title = title
#
#     def drow(self):
#         return f"Запуск отрисовки"
#
#
# class Pen(Stationary):
#      def __init__(self,title):
#          super().__init__(title)
#
#      def drow(self):
#          return f"Запуск отрисовки ручкой"
#
#
# class Pencil(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def drow(self):
#         return f"Запуск отрисовки карандашом"
#
#
# class Handle(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def drow(self):
#         return f"Запуск отрисовки маркером"
#
# pen = Pen('')
# pencil = Pencil("Карандаш")
# handle = Handle('')
# print(handle.drow())
# print(pen.drow())
# print(pencil.drow())


###############################



class MyClass:
      def __init__(self, width, height):
          self.width = width
          self.height = height

      def __add__(self, other):
        return MyClass(self.width + other.width, self.height + other.height)

      def __str__(self):
        return f"Объект с параметрами ({self.width}, {self.height})"
mc_1 = MyClass(10, 20)
mc_2 = MyClass(30, 40)
print(mc_1 + mc_2) ##Объект с параметрами (40, 60)

