import json
import os


DATA_FOLDER = "data"


def create_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


def get_file_path(filename):
    return os.path.join(DATA_FOLDER, filename)


def save_data(filename, data):
    create_data_folder()

    file_path = get_file_path(filename)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_data(filename):
    create_data_folder()

    file_path = get_file_path(filename)

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        content = file.read()

        if content == "":
            return []

        return json.loads(content)


def add_game(game):
    games = load_data("games.json")

    games.append({
        "name": game.name,
        "players": game.players,
        "duration": game.duration
    })

    save_data("games.json", games)


def get_games():
    return load_data("games.json")


def add_session(session):
    sessions = load_data("sessions.json")

    sessions.append({
        "game": session.game,
        "date": session.date,
        "winner": session.winner
    })

    save_data("sessions.json", sessions)


def get_sessions():
    return load_data("sessions.json")