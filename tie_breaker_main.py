
from models.tie_breaker import TieBreakMatch  # Our new subclass

def main():
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")

    print("Pick the tournament:\n    1. Grand Slam\n    2. Davis Cup\n    3. Others\n")
    tournament = input("Choice: ")

    if tournament in ['1', '2']:
        print("Pick match type:\n    1. Short Match\n    2. Long Match\n")
        match_type = input("Choice: ")

        # Use TieBreakMatch to automatically handle tie-breaks
        if match_type == '1':
            match = TieBreakMatch(player1, player2, 2)  # Short match (best of 3 sets)
        else:
            match = TieBreakMatch(player1, player2, 3)  # Long match (best of 5 sets)
    else:
        match = TieBreakMatch(player1, player2)  # Default match (2 sets)

    print("\nThe match will start now!\n")
    match.start()

if __name__ == "__main__":
    main()
