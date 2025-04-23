class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10
        self.potions = 3

    def is_alive(self):
        return self.hp > 0

    def heal(self):
        if self.potions > 0:
            self.hp += 20
            self.potions -= 1
            print(f"{self.name} utilise une potion ! +20 PV.")
        else:
            print("Plus de potions !")

    def attack(self, target):
        print(f"{self.name} attaque {target.name} pour {self.attack_power} dégâts.")
        target.hp -= self.attack_power
