from player import Player
from enemy import Enemy
from item import Item


def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} PV: {player.hp} | {enemy.name} PV: {enemy.hp}")
        print("1. Attaquer")
        print("2. Utiliser une potion")
        print("3. Inventaire")
        action = input("> ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.heal()
        elif action == "3":
            player.show_inventory()
        else:
            print("Action invalide !")

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        if player.is_alive():
            print(f"\n🏆 {player.name} a vaincu le {enemy.name} !")
            xp_earned = 30
            print(f"{enemy.name} a laissé derrière {xp_earned} points d’expérience.")
            player.gain_xp(xp_earned)
        else:
            print(f"\n💀 {player.name} a été vaincu...")



def main():
    name = input("Nom du héros : ")
    hero = Player(name)

    potion_max = Item("Potion Max", "heal", 50)
    boost = Item("Potion de Force", "boost", 5)

    hero.inventory.append(potion_max)
    hero.inventory.append(boost)

    enemy = Enemy()
    combat(hero, enemy)

if __name__ == "__main__":
    main()
