from models.match import Match
from models.player import Player
from models.game import Game

class TieBreakMatch(Match):
    def __init__(self, player1_name, player2_name, sets_to_win=2):
        super().__init__(player1_name, player2_name, sets_to_win)

    def play_game(self):
        # Check if a tie-break should start (6-6 in games)
        if self.p1.games == 6 and self.p2.games == 6:
            print("Tie-break started!")
            self.play_tie_break()
        else:
            # Normal game
            super().play_game()

    def play_tie_break(self):
        # Tie-break rules: first to 7 points, win by 2
        p1_points = 0
        p2_points = 0
        while True:
            try:
                scorer = int(input(f"Tie-break point won by (1 for {self.p1.name}; 2 for {self.p2.name}): "))
                if scorer not in [self.p1.id, self.p2.id]:
                    raise ValueError("Invalid player ID")
            except ValueError:
                print("Invalid input, try again.")
                continue

            if scorer == self.p1.id:
                p1_points += 1
            else:
                p2_points += 1

            print(f"Tie-break score: {self.p1.name} {p1_points} - {p2_points} {self.p2.name}")

            if (p1_points >= 7 or p2_points >= 7) and abs(p1_points - p2_points) >= 2:
                winner = self.p1 if p1_points > p2_points else self.p2
                winner.games += 1
                print(f"Tie-break won by {winner.name}!")
                break
