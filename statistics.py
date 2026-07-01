from database import get_sessions


def show_statistics():
    sessions = get_sessions()

    if len(sessions) == 0:
        print("\nNog geen gespeelde spellen.")
        return

    total_games = len(sessions)

    game_counts = {}
    winner_counts = {}

    for session in sessions:
        game = session["game"]
        winner = session["winner"]

        if game in game_counts:
            game_counts[game] += 1
        else:
            game_counts[game] = 1

        if winner in winner_counts:
            winner_counts[winner] += 1
        else:
            winner_counts[winner] = 1


    most_played_game = max(
        game_counts,
        key=game_counts.get
    )

    best_player = max(
        winner_counts,
        key=winner_counts.get
    )


    print("\n=== Statistieken ===")

    print(f"Totaal gespeelde spellen: {total_games}")

    print(
        f"Meest gespeeld: {most_played_game} "
        f"({game_counts[most_played_game]} keer)"
    )

    print(
        f"Beste speler: {best_player} "
        f"({winner_counts[best_player]} overwinningen)"
    )
    
def get_average_duration(game_name):

    sessions = get_sessions()

    durations = []

    for session in sessions:

        if session["game"] == game_name:

            durations.append(
                int(session["duration"])
            )


    if len(durations) == 0:
        return None


    average = sum(durations) / len(durations)

    return round(average)