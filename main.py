from player import Player
from enemy import Enemy
from item import Item
from item import get_random_loot
from map import GameMap


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

            loot = get_random_loot()
            if loot:
                player.inventory.append(loot)
                print(f"🎁 {player.name} trouve un objet : {loot.name} !")
            else:
                print("🪨 Rien d'intéressant trouvé cette fois...")
        else:
            print(f"\n💀 {player.name} a été vaincu...")



def main():
    name = input("Nom du héros : ")
    hero = Player(name)
    game_map = GameMap()

    while True:
        print("\n📍 Position actuelle :")
        game_map.display()

        print("\nDéplacement : [n] nord, [s] sud, [e] est, [w] ouest")
        print("[q] quitter, [c] combattre ennemi aléatoire")
        action = input("> ")

        if action in ["n", "s", "e", "w"]:
            game_map.move_player(action)
        elif action == "c":
            enemy = Enemy()
            combat(hero, enemy)
        elif action == "q":
            print("👋 À bientôt, aventurier !")
            break
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    main()
