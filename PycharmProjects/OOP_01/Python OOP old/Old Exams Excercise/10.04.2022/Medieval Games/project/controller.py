from project.core.validator import Validator
from project.player import Player

class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __check_if_name_exist_in_list(self, player_name):
        for player in self.players:
            if player.name == player_name:
                raise Exception(f"Name {player.name} is already used!")
        return True

    def __return_last_supplied_item_per_type_and_remove_from_supplies(self, supplies, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[idx]).__name__ == sustenance_type:
                item = supplies.pop(idx)
                return item
            if sustenance_type == "Drink":
                raise Exception("There are no drink supplies left!")
            elif sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            return None

    @staticmethod
    def __attack(player1, player2):
        hit_scores = player1.stamina / 2
        scores = player2.stamina
        scores -= hit_scores
        if scores < 0:
            player2.stamina = 0
        player2.stamina = scores
        if player2.stamina > player1.stamina:

            return f"Winner: {player2.name}"
        else:
            return f"Winner: {player1.name}"



    def add_player(self, *players_to_add: Player):
        for player in players_to_add:
            if self.__check_if_name_exist_in_list(player.name):
                self.players.append(player)
        return f"Successfully added: {', '.join([plr.name for plr in self.players])}"

    def add_supply(self, *supply_to_add: Player):
        for item in supply_to_add:
            self.supplies.append(item)

    def sustain(self, player_name: str, sustenance_type: str):
        for player in self.players:
            if player.name == player_name:
                if player.need_sustenance:
                    item = self.__return_last_supplied_item_per_type_and_remove_from_supplies(self.supplies, sustenance_type)
                    if item is not None:
                        player.stamina += item.energy
                        if player.stamina > 100:
                            player.stamina = 100
                        return f"{player_name} sustained successfully with {item.name}."

                return f"{player_name} have enough stamina."

    def duel(self, first_player_name: str, second_player_name: str):
        idx = 0
        player_1 = 0
        player_2 = 0
        if first_player_name == self.players[idx].name:
            player_1 = self.players[idx]
            if player_1.stamina < 1:
                return f"Player {player_1.name} does not have enough stamina."
            player_2 = self.players[idx + 1]
            if player_2.stamina < 1:
                return f"Player {player_2.name} does not have enough stamina."
        elif second_player_name == self.players[idx].name:
            player_2 = self.players[idx]
            if player_2.stamina < 1:
                return f"Player {player_2.name} does not have enough stamina."
            player_1 = self.players[idx + 1]
            if player_1.stamina < 1:
                return f"Player {player_1.name} does not have enough stamina."

        if player_1.stamina > player_2.stamina:

            return self.__attack(player_2, player_1)
        else:
            return self.__attack(player_1, player_2)



    def next_day(self):
        pass

    def __str__(self):
        pass


