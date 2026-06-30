from game import Game
from player import Player
from session import PlaySession
from database import add_game as save_game, get_games


def show_menu():
    print("\n=== Bordspellen Beheer ===")
    print("1. Bordspel toevoegen")
    print("2. Bordspellen bekijken")
    print("3. Speelbeurt registreren")
    print("4. Statistieken bekijken")
    print("5. Programma afsluiten")


def main():
    running = True

    while running:
        show_menu()

        choice = input("Kies een optie: ")

        if choice == "1":
            add_game()

        elif choice == "2":
            view_games()

        elif choice == "3":
            register_session()

        elif choice == "4":
            show_statistics()

        elif choice == "5":
            running = False
            print("Programma afgesloten.")

        else:
            print("Ongeldige keuze, probeer opnieuw.")


def add_game():
    print("\nNieuw bordspel toevoegen")

    name = input("Naam: ")
    players = input("Aantal spelers: ")
    duration = input("Speelduur in minuten: ")

    game = Game(name, players, duration)

    save_game(game)

    print(f"{game.name} is opgeslagen.")


def view_games():
    print("\nBordspellen:")

    games = get_games()

    if len(games) == 0:
        print("Er zijn nog geen bordspellen opgeslagen.")
        return

    for game in games:
        print("----------------")
        print(f"Naam: {game['name']}")
        print(f"Aantal spelers: {game['players']}")
        print(f"Speelduur: {game['duration']} minuten")

def register_session():
    print("\nSpeelbeurt registreren")

    game = input("Welk spel is gespeeld? ")
    date = input("Datum: ")
    winner = input("Winnaar: ")

    session = PlaySession(game, date, winner)

    print("Speelbeurt opgeslagen.")


def show_statistics():
    print("\nStatistieken")

    print("Hier komen later de statistieken.")


main()