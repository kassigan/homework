import time
class Hero:

    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other): # атакует другого героя
        if self.is_alive():
            print(f"{self.name} attacks {other.name} with {self.attack_power} damage!")
            other.health -= self.attack_power
        else:
            print(f"{other.name} is defeated")

    def is_alive(self):
        return self.health > 0

hero1 = Hero("Arthur", attack_power=23)
hero2 = Hero("Khal", health=89)
print(f"{hero1.name} has {hero1.health} points of health and {hero1.attack_power} attack power")
print(f"{hero2.name} has {hero2.health} points of health and {hero2.attack_power} attack power")

hero1.attack(hero2)
print(f"Health {hero2.name}: {hero2.health} after damage")



class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

# начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
    def start(self):
        print("The battle begins! ")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer) # игрок атакует первым
            if not self.computer.is_alive():
                break

            time.sleep(1)

            self.computer.attack(self.player) # компьютер атакует игрока

            time.sleep(1)

        print("Battle is over!")
        if self.player.is_alive():
            print(f"{self.player.name} won!")
        else:
            print(f"{self.computer.name} won!")


game = Game(hero1, hero2)
game.start()
