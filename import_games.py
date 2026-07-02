import csv
from database import save_data, load_data

GAMEPLAY_OPTIONS = [
    "Coöperatief",
    "Sociale interactie",
    "Strategie & puzzel",
    "Economie & ontwikkeling",
    "Kaartoptimalisatie",
    "Geluk & Dobbelstenen",
    "Slagenspel"
]

import csv

from database import load_data, save_data


GAMEPLAY_OPTIONS = [
    "Coöperatief",
    "Sociale interactie",
    "Strategie & puzzel",
    "Economie & ontwikkeling",
    "Kaartoptimalisatie",
    "Geluk & Dobbelstenen",
    "Slagenspel"
]
TYPE_OPTIONS = [
    "Basisset",
    "Uitbreiding",
    "Reisspel"
]

def import_games(mode="overwrite"):

    games = []

    added = 0
    skipped = 0
    seen_games = set()

    # ----------------------------
    # CSV INLEZEN
    # ----------------------------
    with open(
        "data/games.csv",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            # Naam controleren
            if row["name"].strip() == "":
                print(
                    f"⚠ Rij {row_number}: naam ontbreekt."
                )
                skipped += 1
                continue

            # Gameplay controleren
            if row["gameplay"].strip() not in GAMEPLAY_OPTIONS:
                print(
                    f"⚠ Rij {row_number}: "
                    f"onbekende gameplay "
                    f"'{row['gameplay']}'."
                )
                skipped += 1
                continue
            # Type controleren
            if row["type"].strip() not in TYPE_OPTIONS:

                print(
                    f"⚠ Rij {row_number}: "
                    f"onbekend type '{row['type']}'."
                )

                skipped += 1
                continue
            
            # Moeilijkheid controleren
            try:

                difficulty = int(row["difficulty"])

                if difficulty < 1 or difficulty > 5:

                    print(
                        f"⚠ Rij {row_number}: "
                        "moeilijkheid moet tussen 1 en 5 liggen."
                    )

                    skipped += 1
                    continue

            except ValueError:

                print(
                    f"⚠ Rij {row_number}: "
                    "moeilijkheid is geen getal."
                )

                skipped += 1
                continue
            
            # Spelersaantal controleren
            try:

                min_players = int(row["min_players"])
                max_players = int(row["max_players"])

                if min_players > max_players:

                    print(
                        f"⚠ Rij {row_number}: "
                        "minimum spelers is groter dan maximum spelers."
                    )

                    skipped += 1
                    continue

            except ValueError:

                print(
                    f"⚠ Rij {row_number}: "
                    "ongeldig aantal spelers."
                )

                skipped += 1
                continue
            
            key = (
                row["name"].strip(),
                row["version"].strip()
            )

            if key in seen_games:

                print(
                    f"⚠ Rij {row_number}: "
                    "dubbel spel in CSV."
                )

                skipped += 1
                continue

            seen_games.add(key)

            # Spel toevoegen
            games.append({

                "name": row["name"].strip(),
                "version": row["version"].strip(),
                "type": row["type"].strip(),
                "min_players": row["min_players"].strip(),
                "max_players": row["max_players"].strip(),
                "min_duration": row["min_duration"].strip(),
                "min_age": row["min_age"].strip(),
                "difficulty": row["difficulty"].strip(),
                "gameplay": row["gameplay"].strip()

            })

            added += 1

    # ----------------------------
    # MODE: OVERWRITE OF APPEND
    # ----------------------------
    if mode == "append":

        existing = load_data("games.json")

        existing_keys = {
            (g["name"], g["version"])
            for g in existing
        }

        for game in games:

            key = (
                game["name"],
                game["version"]
            )

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

    # ----------------------------
    # RESULTAAT
    # ----------------------------
    print("\nImport voltooid.")
    print(f"✓ {added} spellen toegevoegd.")
    print(f"⚠ {skipped} rijen overgeslagen.")