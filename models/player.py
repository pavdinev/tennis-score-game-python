class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0  # Points in current game
        self.games = 0   # Games won in current set
        self.sets = 0    # Sets won