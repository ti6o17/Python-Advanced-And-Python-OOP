from project.player import Player


class Guild:
    def __init__(self, name:str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != player.DEFAULT_CONSTANT:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        Player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player_name == self.players:
                self.players.remove(player_name)
                player.guild = player.DEFAULT_CONSTANT
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name}"

    def guild_info(self):
        result = f"Guild: {self.name}"
        for player in self.players:
            result += "\n" + player.player_info()
        return result


