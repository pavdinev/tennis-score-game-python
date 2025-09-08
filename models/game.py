from models.player import Player


class Game:
    point_names = ["0", "15", "30", "40", "Advantage"]

    def __init__(self, player1: Player, player2: Player):
        self.p1 = player1
        self.p2 = player2

    def point_won_by(self, player_id):
        if player_id == self.p1.id:
            self.p1.points += 1
        else:
            self.p2.points += 1
        self.print_score()
        if self.is_game_over():
            winner = self.p1 if self.p1.points > self.p2.points else self.p2
            print(f"Game won by {winner.name}!\n")
            winner.games += 1
            self.p1.points = 0
            self.p2.points = 0
            return True
        return False

    def print_score(self):
        p1_score = self.point_names[min(self.p1.points, 4)]
        p2_score = self.point_names[min(self.p2.points, 4)]

        # Handle deuce / advantage
        if self.p1.points >= 3 and self.p2.points >= 3:
            if self.p1.points == self.p2.points:
                score = "Deuce"
            elif self.p1.points > self.p2.points:
                score = f"Advantage {self.p1.name}"
            else:
                score = f"Advantage {self.p2.name}"
            print(score)
        else:
            print(f"{self.p1.name}: {p1_score}, {self.p2.name}: {p2_score}")

    def is_game_over(self):
        if self.p1.points >= 4 or self.p2.points >= 4:
            if abs(self.p1.points - self.p2.points) >= 2:
                return True
        return False
