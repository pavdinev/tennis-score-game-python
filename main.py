from models.match import Match


def main():
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")

    print("Pick the tournament:\n    1. Grand Slam\n    2. Davis Cup\n    3. Others\n")
    tournament = input("Choice: ")

    if tournament in ['1', '2']:
        print("Pick gender:\n    1. Male\n    2. Female\n")

        sex = input("Choice: ")

        if sex == '1':
            match = Match(player1, player2, 3)
        else:
            match = Match(player1, player2, 2)
    else:
        match = Match(player1, player2)

    print("\nTova shte igraem: \n")

    match.start()

if __name__ == "__main__":
    main()