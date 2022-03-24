class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
        self.wanted_nationality = []
        self.top_scorers = []

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        self.wanted_nationality = filter(lambda player: player.nationality == nationality, players)

        self.top_scorers = sorted(self.wanted_nationality, key=lambda player: player.total, reverse=True)

        return self.top_scorers