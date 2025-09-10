from models.match import Match
from models.player import Player

class TieBreaker(Match):
    def __init__(self, player1_name, player2_name):
        super().__init__(player1_name, player2_name)
        self.tiebreak_points_to_win = 7

    def play_tiebreak(self):
        self.p1.points = 0
        self.p2.points = 0
        while True:
            tmp_scorer = input(f"Tie-break point won by (1 for {self.p1.name}; 2 for {self.p2.name}): ").strip()
            try:
                scorer = int(tmp_scorer)
                if scorer not in [self.p1.id, self.p2.id]:
                    raise TypeError("Player id does not match, try again!")
                if scorer == self.p1.id:
                    self.p1.points += 1
                else:
                    self.p2.points += 1
                print(f"Score: {self.p1.name} {self.p1.points} - {self.p2.points} {self.p2.name}")
                if self.is_tiebreak_over():
                    winner = self.p1 if self.p1.points > self.p2.points else self.p2
                    print(f"Tie-break won by {winner.name}!\n")
                    winner.games += 1
                    self.p1.points = 0
                    self.p2.points = 0
                    break
            except ValueError:
                print("Invalid player, try again.")
                continue
            except TypeError as e:
                print(e)
                continue

    def is_tiebreak_over(self):
        if (self.p1.points >= self.tiebreak_points_to_win or self.p2.points >= self.tiebreak_points_to_win) and \
           abs(self.p1.points - self.p2.points) >= 2:
            return True
        return False