from player import Player
from enemy import Enemy
from item import get_random_loot
from map import GameMap
from keyboard_input import get_arrow_key

import random



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

        """ ------------------/ remove after checking verification.
        print("\nDéplacement : [n] nord, [s] sud, [e] est, [w] ouest")
        print("[q] quitter, [c] combattre ennemi aléatoire")
        action = input("> ")
        """

        print("Utilise les flèches directionnelles pour te déplacer.")
        print("Touche 'c' pour combattre, 'q' pour quitter.")
        action = get_arrow_key()

        if action is None:
            action = input("Commande : ").strip()

        # doesn't touch this event because is be checking from keyboard_input.py for mapping the keyboard with the differents arrow directionnal
        if action in ["n", "s", "e", "w"]:
            tile = game_map.move_player(action)
            if tile == "🏰":
                print("🏰 Tu arrives au château. Un mystère t’attend...")
            elif tile == "🗻":
                print("🗻 Une montagne bloque le chemin... mais un cri provient du sommet.")
            elif tile == "💰":
                print("💰 Tu trouves un coffre ! Tu gagnes un objet.")
                loot = get_random_loot()
                if loot:
                    hero.inventory.append(loot)
                    print(f"🎁 Tu obtiens : {loot.name}")
            elif tile == "🌀":
                print("🌀 Un portail magique t’enveloppe... et te téléporte ailleurs !")
                game_map.player_pos = [random.randint(0, game_map.height - 1), random.randint(0, game_map.width - 1)]
            elif tile and random.random() < 0.3:
                print("👾 Un ennemi t’attaque pendant ton exploration !")
                combat(hero, Enemy())
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
