import random

class GameMap:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.map = [["." for _ in range(width)] for _ in range(height)]
        self.player_pos = [0, 0]  # Ligne, Colonne
        self._place_special_tiles()

    def _place_special_tiles(self):
            # Coordonnées fixes ou aléatoires pour divers éléments
            self._place_symbol("🏰", 1)
            self._place_symbol("🗻", 1)
            self._place_symbol("💰", 2)
            self._place_symbol("🌀", 1)

    def _place_symbol(self, symbol, count):
        for _ in range(count):
            y, x = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            while self.map[y][x] != "." or [y, x] == self.player_pos:
                y, x = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            self.map[y][x] = symbol

    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if [y, x] == self.player_pos:
                    row += "👤 "  # Joueur
                else:
                    row += f"{self.map[y][x]}  "
            print(row)

    def move_player(self, direction):
        y, x = self.player_pos
        new_y, new_x = y, x

        if direction == "n" and y > 0:
            new_y -= 1
        elif direction == "s" and y < self.height - 1:
            new_y += 1
        elif direction == "e" and x < self.width - 1:
            new_x += 1
        elif direction == "w" and x > 0:
            new_x -= 1
        else:
            print("⛔ Déplacement impossible.")
            return None

        self.player_pos = [new_y, new_x]
        return self.map[new_y][new_x]
