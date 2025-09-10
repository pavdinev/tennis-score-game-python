from models.match import Match
from models.tiebreaker2 import TieBreaker

def main():
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")

    print("Pick the tournament:\n    1. Grand Slam\n    2. Davis Cup\n    3. Others\n")
    tournament = input("Choice: ").strip()
    sets_to_win = 2  # Default value
    if tournament in ['1', '2']:
        print("Pick match type:\n    1. Male\n    2. Female\n")

        gender = input("Choice: ").strip()
        if gender == '1':
            sets_to_win = 3
            match = Match(player1, player2, sets_to_win)
            print("Long match selected (best of 3 sets).")
        else:
            sets_to_win = 2
            match = Match(player1, player2, sets_to_win)
            print("Short match selected (best of 2 sets).")
    else:
        sets_to_win = input("Choice (default 2): ").strip()

        try:
            sets_to_win = int(sets_to_win)
            if sets_to_win > 0:
                match = Match(player1, player2, sets_to_win)
            else:
                raise ValueError("Number of sets must be positive.")
        except ValueError:
            print("Invalid input, using default of 2 sets.")
            match = Match(player1, player2, 2)
    
    print(f"\nMatch will be played in {sets_to_win} set(s).Begin! \n")

    match.start()
    if match.p1.games == 6 and match.p2.games == 6:
        print("Tie-break time!")
        tiebreak = TieBreaker(player1, player2)
        tiebreak.play_tiebreak()

if __name__ == "__main__":
    main()