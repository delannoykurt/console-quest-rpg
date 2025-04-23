class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack_power = 10
        self.potions = 3
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 50
        self.inventory = []
        self.quests = []

    def is_alive(self):
        return self.hp > 0

    def heal(self):
        if self.potions > 0:
            heal_amount = min(20, self.max_hp - self.hp)
            self.hp += heal_amount
            self.potions -= 1
            print(f"{self.name} utilise une potion ! +{heal_amount} PV.")
        else:
            print("Plus de potions !")

    def attack(self, target):
        print(f"{self.name} attaque {target.name} pour {self.attack_power} dégâts.")
        target.hp -= self.attack_power

    def gain_xp(self, amount):
            self.xp += amount
            print(f"{self.name} gagne {amount} XP ! (Total : {self.xp}/{self.xp_to_next_level})")
            if self.xp >= self.xp_to_next_level:
                self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.max_hp += 20
        self.attack_power += 5
        self.hp = self.max_hp  # Restaure la vie au niveau supérieur
        print(f"\n🔥 {self.name} passe au niveau {self.level} !")
        print(f"💪 PV max : {self.max_hp}, Attaque : {self.attack_power}")

    def show_inventory(self):
        if not self.inventory:
            print("🎒 Inventaire vide.")
            return

        print("🎒 Inventaire :")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item.name}")

        choice = input("Choisir un objet à utiliser (ou rien pour annuler) : ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(self.inventory):
                item = self.inventory.pop(index)
                item.use(self)
            else:
                print("Choix invalide.")
        else:
            print("Action annulée.")

    def show_journal(self):
        print("\n📜 Journal de Quêtes :")
        if not self.quests:
            print("Aucune quête pour le moment.")
            return

        for i, q in enumerate(self.quests):
            status = "✔️" if q.completed else "❌"
            print(f"{i+1}. {q.title} [{status}] — {q.description}")
