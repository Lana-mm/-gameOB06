python
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        print(f"{self.name} атакует {other.name}!")
        other.health -= self.attack_power
        print(f"{other.name} получает {self.attack_power} урона. Осталось здоровья: {other.health}")

    def is_alive(self):
        return self.health > 0
