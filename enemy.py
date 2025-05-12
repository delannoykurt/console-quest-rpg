import random

class Enemy:
    def __init__(self, name="Gobelin"):
        self.name = name
        self.hp = random.randint(30, 50)
        self.attack_power = random.randint(5, 12)

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        print(f"{self.name} attaque {target.name} pour {self.attack_power} dégâts.")
        target.hp -= self.attack_power
