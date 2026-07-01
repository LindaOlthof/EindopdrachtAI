from player import Player
from session import PlaySession
from database import (
    add_game as save_game,
    get_games,
    add_session as save_session
)
from statistics import (
    show_statistics as display_statistics,
    get_average_duration,
    get_total_games,
    top_games_per_gameplay,
    best_player_per_game
)

GAMEPLAY_OPTIONS = [
    "Coöperatief",
    "Deck-building",
    "Engine-building",
    "Worker-placement",
    "Sociale deductie/bluffen",
    "Area control/route building",
    "Roll/flip & write"
]

def choose_gameplay():

    print("\nKies gameplay:")

    for index, option in enumerate(GAMEPLAY_OPTIONS, start=1):
        print(f"{index}. {option}")


    while True:

        choice = input(
            "Kies nummer: "
        )


        if choice.isdigit():

            number = int(choice)


            if 1 <= number <= len(GAMEPLAY_OPTIONS):

                return GAMEPLAY_OPTIONS[number - 1]


        print(
            "Ongeldige keuze, probeer opnieuw."
        )


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
            display_statistics()
    
        elif choice == "5":
            running = False
            print("Programma afgesloten.")

        else:
            print("Ongeldige keuze, probeer opnieuw.")


def add_game():

    print("\nNieuw bordspel toevoegen")

    game = {
        "name": input("Naam: "),
        "version": input("Versie: "),
        "type": input("Type: "),
        "min_players": input("Min spelers: "),
        "max_players": input("Max spelers: "),
        "min_duration": input("Min speelduur: "),
        "min_age": input("Min leeftijd: "),
        "difficulty": input("Moeilijkheid (1-5): "),
        "gameplay": choose_gameplay()
    }

    save_game(game)

    print(f"{game['name']} opgeslagen.")


def view_games():

    print("\nBordspellen:")

    games = get_games()

    if len(games) == 0:
        print("Geen spellen gevonden.")
        return


    # 1. Groeperen per spelnaam
    grouped = {}

    for game in games:

        name = game["name"]

        if name not in grouped:
            grouped[name] = []

        grouped[name].append(game)


    # 2. Output per spel
    for name, versions in grouped.items():

        print("\n----------------")
        print(name)


        for v in versions:

            print(
                f"  - {v['version']} ({v['type']})"
            )

            print(
                f"    Spelers: {v['min_players']} - {v['max_players']}"
            )

            print(
                f"    Speelduur: {v['min_duration']} min"
            )

            print(
                f"    Leeftijd: {v['min_age']}+"
            )

            print(
                f"    Moeilijkheid: {v['difficulty']}/5"
            )

            print(
                f"    Gameplay: {v['gameplay']}"
            )
        
def register_session():

    print("\nSpeelbeurt registreren")

    games = get_games()

    if len(games) == 0:
        print("Geen spellen beschikbaar.")
        return


    print("\nBeschikbare spellen:")

    for index, game in enumerate(games, start=1):

        print(
            f"{index}. {game['name']} - {game['version']}"
        )


    while True:

        choice = input("Kies nummer: ")

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(games):

                selected_game = games[number - 1]
                break


        print("Ongeldige keuze, probeer opnieuw.")

    date = input("Datum: ")

    players_input = input("Welke spelers deden mee? ")

    players = players_input.split(",")

    duration = input("Speelduur van het potje in minuten: ")

    winner = input("Winnaar: ")

    winner_score = input("Score van winnaar: ")

    session = {
        "game": selected_game["name"],
        "version": selected_game["version"],
        "date": date,
        "players": players,
        "duration": int(duration),
        "winner": winner,
        "winner_score": int(winner_score)
    }

    save_session(session)

    print("Speelbeurt opgeslagen.")




main()