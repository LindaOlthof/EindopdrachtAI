class Game:

    def __init__(
        self,
        name,
        min_players,
        max_players,
        min_duration,
        min_age,
        difficulty,
        gameplay
    ):

        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.min_duration = min_duration
        self.min_age = min_age
        self.difficulty = difficulty
        self.gameplay = gameplay