class Item:
    def __init__(self, name, effect, effect_value):
        self.name = name
        self.effect = effect  # "heal" ou "boost"
        self.effect_value = effect_value

    def use(self, target):
        if self.effect == "heal":
            heal_amount = min(self.effect_value, target.max_hp - target.hp)
            target.hp += heal_amount
            print(f"{target.name} utilise {self.name} et récupère {heal_amount} PV.")
        elif self.effect == "boost":
            target.attack_power += self.effect_value
            print(f"{target.name} utilise {self.name} et gagne +{self.effect_value} ATK temporairement.")
