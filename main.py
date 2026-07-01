from game import Game
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
            show_statistics()
    
        elif choice == "5":
            running = False
            print("Programma afgesloten.")

        else:
            print("Ongeldige keuze, probeer opnieuw.")


def add_game():

    print("\nNieuw bordspel toevoegen")

    # 1. Basisinformatie
    name = input("Naam van het spel: ")

    version = input("Versie (bijv. Basisspel, Europe, Märklin): ")

    game_type = input(
        "Type (Basis / Uitbreiding / Reisspel): "
    )

    # 2. Spel eigenschappen (per versie)
    min_players = input("Minimum aantal spelers: ")
    max_players = input("Maximum aantal spelers: ")
    min_duration = input("Minimum speelduur: ")
    min_age = input("Minimum leeftijd: ")
    difficulty = input("Moeilijkheid (1-5): ")

    gameplay = choose_gameplay()


    # 3. Opslaan als versie-object
    game = {
        "name": name,
        "version": version,
        "type": game_type,
        "min_players": min_players,
        "max_players": max_players,
        "min_duration": min_duration,
        "min_age": min_age,
        "difficulty": difficulty,
        "gameplay": gameplay
    }

    save_game(game)

    print(f"{name} ({version}) opgeslagen.")


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


    game = input(
        "Welk spel is gespeeld? "
    )


    date = input(
        "Datum: "
    )


    players_input = input(
        "Welke spelers deden mee? "
    )


    players = players_input.split(",")


    duration = input(
        "Speelduur van het potje in minuten: "
    )


    winner = input(
        "Winnaar: "
    )


    winner_score = input(
        "Score van winnaar: "
    )


    session = PlaySession(
        game,
        date,
        players,
        duration,
        winner,
        winner_score
    )


    save_session(session)


    print(
        "Speelbeurt opgeslagen."
    )


def show_statistics():

    print("\n=== STATISTIEKEN ===")

    print(
        f"Aantal spellen in bezit: "
        f"{get_total_games()}"
    )

    print("\nTop 3 spellen per gameplay:")

    top_games = top_games_per_gameplay()

    for gameplay, games in top_games.items():

        print(f"\n{gameplay}:")

        for name, count in games:

            print(
                f"- {name} ({count} keer gespeeld)"
            )

    print("\nBeste speler per spel:")

    best_players = best_player_per_game()

    for game, player in best_players.items():

        print(
            f"- {game}: {player}"
        )

main()