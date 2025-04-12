# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
#    Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
#    Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
#    которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("игого")

    def eat(self):
        print("cat food")

class Bird(Animal):
    def make_sound(self): # переопределение метода
        print('курлык')

    def eat(self):
        print("seeds")

class Mammal(Animal):
    def make_sound(self):
        print('different sounds')

class Reptile(Animal):
    def make_sound(self):
        print('RRRRRR')

# ПОЛИМОРФИЗМ
animals = [Bird("nightingale",1), Mammal("dog",5), Reptile("iguana",3)]
for animal in animals:
    animal.make_sound()

class Employee:
    def __init__(self, employee_type):
        self.employee_type = employee_type

class ZooKeeper(Employee):

    def feed_animal(self):
        print("animal was fed")

class Veterinarian(Employee):

    def heal_animal(self):
        print("animal was healed")

class Zoo:
    def __init__(self):
        self.animals = []  # <- список объектов Animal (и его подклассов) - композиция
        self.employees = []  # <- список объектов Employee (и его подклассов) - композиция

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self,employee):
        self.employees.append(employee)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} years old")


zoo = Zoo()
zoo.add_animal(Bird('owl Buckly', 2))
zoo.add_animal(Mammal("Dog Tixsi",3))
zoo.add_employee(ZooKeeper("Derek"))
zoo.add_employee(Veterinarian("Frank"))





