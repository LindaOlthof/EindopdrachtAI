class PlaySession:

    def __init__(
        self,
        game,
        date,
        players,
        duration,
        winner,
        winner_score
    ):

        self.game = game
        self.date = date
        self.players = players
        self.duration = duration
        self.winner = winner
        self.winner_score = winner_score