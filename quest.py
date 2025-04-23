class Quest:
    def __init__(self, title, description, location, required_item=None):
        self.title = title
        self.description = description
        self.location = location  # symbole de la carte (ex: "🏰")
        self.required_item = required_item
        self.completed = False

    def check_completion(self, player, current_tile):
        if current_tile == self.location:
            if self.required_item is None or any(item.name == self.required_item for item in player.inventory):
                self.completed = True
                return True
        return False
