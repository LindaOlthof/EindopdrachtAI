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

    name = input("Naam: ")

    min_players = input(
        "Minimum aantal spelers: "
    )

    max_players = input(
        "Maximum aantal spelers: "
    )

    min_duration = input(
        "Minimum speelduur in minuten: "
    )

    min_age = input(
        "Minimum leeftijd: "
    )

    difficulty = input(
        "Moeilijkheidsscore (1-5): "
    )

    gameplay = choose_gameplay()


    game = Game(
        name,
        min_players,
        max_players,
        min_duration,
        min_age,
        difficulty,
        gameplay
    )


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

        print(
            f"Spelers: {game['min_players']} "
            f"tot {game['max_players']}"
        )

        average_duration = get_average_duration(
            game["name"]
        )

        if average_duration is None:
            print(
                f"Speelduur: vanaf "
                f"{game['min_duration']} minuten"
            )

        else:
            print(
                f"Gemiddelde speelduur: "
                f"{average_duration} minuten"
            )

        print(
            f"Leeftijd: {game['min_age']}+"
        )

        print(
            f"Moeilijkheid: "
            f"{game['difficulty']}/5"
        )

        print(
            f"Gameplay: {game['gameplay']}"
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