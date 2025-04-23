class GameMap:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.map = [["." for _ in range(width)] for _ in range(height)]
        self.player_pos = [0, 0]  # Ligne, Colonne

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
        if direction == "n" and y > 0:
            self.player_pos[0] -= 1
        elif direction == "s" and y < self.height - 1:
            self.player_pos[0] += 1
        elif direction == "e" and x < self.width - 1:
            self.player_pos[1] += 1
        elif direction == "w" and x > 0:
            self.player_pos[1] -= 1
        else:
            print("⛔ Déplacement impossible.")
