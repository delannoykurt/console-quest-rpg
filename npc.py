class NPC:
    def __init__(self, name, dialogue, location, gives_quest=None):
        self.name = name
        self.dialogue = dialogue
        self.location = location  # Exemple : [2, 1]
        self.gives_quest = gives_quest
        self.interacted = False

    def interact(self, player):
        if not self.interacted:
            print(f"\n👤 {self.name} : « {self.dialogue} »")
            if self.gives_quest:
                player.quests.append(self.gives_quest)
                print(f"📜 Tu reçois une nouvelle quête : {self.gives_quest.title}")
            self.interacted = True
        else:
            print(f"{self.name} n’a plus rien à dire pour le moment.")
