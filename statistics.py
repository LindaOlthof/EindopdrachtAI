from database import get_games, get_sessions

def create_game_key(name, version):

    return f"{name} | {version}"
# ----------------------------
# STATISTIEKEN OVERZICHT
# ----------------------------
def show_statistics():

    print("\n=== STATISTIEKEN ===")

    print(
        f"Aantal spellen in bezit: "
        f"{get_total_games()}"
    )

    top_games = top_games_per_gameplay()
    best_players = best_player_per_game()

    print("\nTop 3 spellen per gameplay:")

    for gameplay, games in top_games.items():

        print(f"\n{gameplay}:")

        for name, count in games:

            best_player = best_players.get(name, "Onbekend")

            print(f"- {name} ({count} keer gespeeld)")
            print(f"   └ Beste speler: {best_player}")
            print("")  # kleine visuele scheiding
# ----------------------------
# GEMIDDELDE SPEELDUUR
# ----------------------------
def get_average_duration(game_name):

    sessions = get_sessions()

    durations = []

    for session in sessions:

        # ❗ DIRECT MATCH (geen normalisatie meer)
        if session["game"] == game_name:

            durations.append(int(session["duration"]))

    if len(durations) == 0:
        return None

    average = sum(durations) / len(durations)

    return round(average)


# ----------------------------
# AANTAL SPELLEN
# ----------------------------
def get_total_games():

    games = get_games()

    return len(games)


# ----------------------------
# TOP 3 PER GAMEPLAY
# ----------------------------
def top_games_per_gameplay():

    games = get_games()
    sessions = get_sessions()

    result = {}

    # tellen per spel
    for game in games:

        gameplay = game["gameplay"]
        name = create_game_key(
        game["name"],
        game["version"]
        )

        count = 0

        for session in sessions:

            # DIRECT MATCH
            session_key = create_game_key(
            session["game"],
            session["version"]
            )

        if session_key == name:
                count += 1

        if gameplay not in result:
            result[gameplay] = []

        result[gameplay].append((name, count))

    # sorteren NA het verzamelen
    for gameplay in result:

        result[gameplay] = sorted(
            result[gameplay],
            key=lambda x: x[1],
            reverse=True
        )[:3]

    return result


# ----------------------------
# BESTE SPELER PER GAME
# ----------------------------
def best_player_per_game():

    sessions = get_sessions()

    result = {}

    for session in sessions:

        game = create_game_key(
            session["game"],
            session["version"]
        )
        winner = session["winner"]

        if game not in result:
            result[game] = {}

        if winner not in result[game]:
            result[game][winner] = 0

        result[game][winner] += 1

    # kiezen beste speler per game
    for game in result:

        result[game] = max(
            result[game],
            key=result[game].get
        )

    return result