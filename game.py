"""
Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
не изменяя существующий код бойцов или механизм боя.

Исходные данные:

Есть класс Fighter, представляющий бойца.
Есть класс Monster, представляющий монстра.
Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

Шаг 1: Создайте абстрактный класс для оружия
Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().

Шаг 2: Реализуйте конкретные типы оружия
Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
Каждый из этих классов реализует метод attack() своим уникальным способом.

Шаг 3: Модифицируйте класс Fighter
Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
Добавьте метод change_weapon(), который позволяет изменить оружие бойца.

Шаг 4: Реализация бояРеализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
Требования к заданию:

Код должен быть написан на Python.
Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять,
не изменяя существующие классы бойцов и механизм боя. Программа должна выводить результат боя в консоль.

Пример результата:

Боец выбирает меч.
Боец наносит удар мечом.
Монстр побежден!
Боец выбирает лук.
Боец наносит удар из лука.
Монстр побежден!

"""

from abc import ABC, abstractmethod

class Weapon(ABC): # aбстрактный класс
    @abstractmethod
    def attack(self, target, force=0, range=0): # aбстрактный метод не иметь реализацию (print)
        pass

class Fighter:

    def __init__(self, name, health, weapon: Weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, target):
        print(f"{self.name} attacks {target.name} using {self.weapon.__class__.__name__}")
        self.weapon.attack(target)

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} change {weapon} to the {weapon}")

class Monster:

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, amount):
        self.amount = amount
        print(f"{self.name} took {amount} damage! Remaining health: {self.health}")


class Sword1(Weapon):
    def attack(self, target, force=10, range=3):
        print(f"Swinging sword with force {force} and range {range}!")

class Sword2(Weapon):
    def attack(self, target, force=15, range=4):
        print(f"Swinging sword with force {force} and range {range}!")

class Bow(Weapon):
    def attack(self, force=5, range=10):
        print(f"Shooting arrow with force {force} and range {range}!")


goblin = Monster("Goblin", 50, 3)
sword1 = Sword1()
sword2 = Sword2()
bow = Bow()

warrior = Fighter("Aragorn", 50, sword1)
archer = Fighter("Legolas", 35, bow)

warrior.attack(goblin)
goblin.take_damage(warrior)
archer.attack(goblin)
goblin.take_damage(archer)
warrior.change_weapon(sword2)
warrior.attack(goblin)
goblin.take_damage(warrior)