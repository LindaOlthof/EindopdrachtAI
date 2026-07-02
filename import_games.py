import csv
from database import save_data, load_data


def import_games(mode="overwrite"):

    games = []

    # ----------------------------
    # CSV INLEZEN
    # ----------------------------
    with open("data/games.csv", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for row in reader:

            games.append({

                "name": row["name"],
                "version": row["version"],
                "type": row["type"],
                "min_players": row["min_players"],
                "max_players": row["max_players"],
                "min_duration": row["min_duration"],
                "min_age": row["min_age"],
                "difficulty": row["difficulty"],
                "gameplay": row["gameplay"]

            })

    # ----------------------------
    # MODE: OVERWRITE OF APPEND
    # ----------------------------
    if mode == "append":

        existing = load_data("games.json")

        existing_keys = {
            (g["name"], g["version"]) for g in existing
        }

        for game in games:

            key = (game["name"], game["version"])

            if key not in existing_keys:

                existing.append(game)

        games = existing

    # ----------------------------
    # OPSLAAN
    # ----------------------------
    save_data(
        "games.json",
        games
    )

    print(
        f"{len(games)} spellen geïmporteerd ({mode})."
    )