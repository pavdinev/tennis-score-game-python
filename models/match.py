
from models.player import Player
from models.game import Game



class Match:
    def __init__(self, player1_name, player2_name, sets_to_win=2):
        self.p1 = Player(1, player1_name)
        self.p2 = Player(2, player2_name)
        self.sets_to_win = sets_to_win

    def play_game(self):
        game = Game(self.p1, self.p2)
        while True:
            tmp_scorer = input(f"Point won by (1 for {self.p1.name}; 2 for {self.p2.name}): ").strip()
            try:
                scorer = int(tmp_scorer)
                if int(scorer) not in [self.p1.id, self.p2.id]:
                    raise TypeError("Player id does not match, try again!")
                game_over = game.point_won_by(scorer)
                if game_over:
                    break
            except ValueError:
                print("Invalid player, try again.")
                continue
            except TypeError as e:
                print(e)
                continue

    def check_set(self):
        # Check set winner
        if self.p1.games >= 6 or self.p2.games >= 6:
            if abs(self.p1.games - self.p2.games) >= 2:
                if self.p1.games > self.p2.games:
                    set_winner = self.p1
                else:
                    set_winner = self.p2
                print(f"Set won by {set_winner.name}!\n")
                set_winner.sets += 1
                self.p1.games = 0
                self.p2.games = 0


    def check_match_won(self):
        # Check match winner
        if self.p1.sets == self.sets_to_win:
            print(f"🎉 Match won by {self.p1.name}! 🎉")
            return True
        elif self.p2.sets == self.sets_to_win:
            print(f"🎉 Match won by {self.p2.name}! 🎉")
            return True
        return False
    
    def print_current_score(self):
        print(f"Current sets: {self.p1.name} {self.p1.sets} - {self.p2.sets} {self.p2.name}")
        print(f"Current games: {self.p1.name} {self.p1.games} - {self.p2.games} {self.p2.name}\n")

    def start(self):
        while True:
            self.play_game()
            self.check_set()
            
            if self.check_match_won():
                break

            self.print_current_score()