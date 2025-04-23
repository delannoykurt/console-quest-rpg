from player import Player
from enemy import Enemy

def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} PV: {player.hp} | {enemy.name} PV: {enemy.hp}")
        print("1. Attaquer")
        print("2. Utiliser une potion")
        action = input("> ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.heal()
        else:
            print("Action invalide !")

        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print(f"\n🏆 {player.name} a vaincu le {enemy.name} !")
    else:
        print(f"\n💀 {player.name} a été vaincu...")

def main():
    name = input("Nom du héros : ")
    hero = Player(name)
    enemy = Enemy()
    combat(hero, enemy)

if __name__ == "__main__":
    main()
