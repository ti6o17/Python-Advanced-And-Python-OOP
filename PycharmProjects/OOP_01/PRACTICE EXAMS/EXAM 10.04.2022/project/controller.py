from collections import deque


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *add_players):
        # for player in add_players:
        #     if player.name in [p.name for p in self.players]:
        #         list(add_players)
        #         continue
        #     else:
        #         self.players.append(player)
        # names_que = (deque(player.name for player in self.players))
        # name = names_que.popleft()
        # result = f"Successfully added: {name}"
        # while names_que:
        #     name = names_que.popleft()
        #     result += f", {name}"
        # return result
        successful_added_player = []
        for p in add_players:
            if p not in self.players:
                self.players.append(p)
                successful_added_player.append(p.name)
        return f"Successfully added: {', '.join(successful_added_player)}"

    def add_supply(self, *supplies):
        for item in supplies:
            self.supplies.append(item)

    @staticmethod
    def __if_player_lost(player_object):
        if player_object.stamina <= 0:
            return True

    def __get_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __get_last_supply_and_return_exception_if_none(self, sustenance_type):
        for supply in reversed(self.supplies):
            x = supply.__class__.__name__
            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop()
                return supply
        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name, sustenance_type):
        player = self.__get_player_by_name(player_name)
        if player.need_sustenance:
            supply = self.__get_last_supply_and_return_exception_if_none(sustenance_type)
            player.stamina += supply.energy
            if player.stamina > 100:
                player.stamina = 100
            return f"{player_name} sustained successfully with {supply.name}."
        else:
            return f"{player_name} have enough stamina."

    def duel(self, first_player_name, second_player_name):
        player_one = self.__get_player_by_name(first_player_name)
        player_two = self.__get_player_by_name(second_player_name)
        if player_one.stamina <= 0:
            return f"Player {player_one.name} does not have enough stamina."
        if player_two.stamina <= 0:
            return f"Player {player_two.name} does not have enough stamina."
        x = player_one.stamina
        y = player_two.stamina
        counter = 0
        first_attack = ''
        while player_one.stamina > 0 or player_two.stamina > 0:
            if counter == 0:
                if player_one.stamina < player_two.stamina:
                    a = player_two.stamina
                    a -= player_one.stamina / 2
                    if a < 0:
                        player_two.stamina = 0
                    else:
                        player_two.stamina = a
                    # self.__if_stamina_negative(player_two)
                    first_attack = "player_one"
                    counter += 1
                    if self.__if_player_lost(player_one):
                        return f"Winner: {player_two.name}"
                    if self.__if_player_lost(player_two):
                        return f"Winner: {player_one.name}"
                    continue
                a = player_one.stamina
                a -= player_two.stamina / 2
                if a < 0:
                    player_one.stamina = 0
                else:
                    player_one.stamina = a
                # self.__if_stamina_negative(player_one)
                first_attack = "player_two"
                counter += 1
                if self.__if_player_lost(player_one):
                    return f"Winner: {player_two.name}"
                if self.__if_player_lost(player_two):
                    return f"Winner: {player_one.name}"
                continue
            if first_attack == "player_one":
                first_attack = "player_two"
                a = player_one.stamina
                a -= player_two.stamina / 2
                if a < 0:
                    player_one.stamina = 0
                else:
                    player_one.stamina = a
                if self.__if_player_lost(player_one):
                    return f"Winner: {player_two.name}"
                if self.__if_player_lost(player_two):
                    return f"Winner: {player_one.name}"
                continue
            else:
                first_attack = "player_one"
                a = player_two.stamina
                a -= player_one.stamina / 2
                if a < 0:
                    player_two.stamina = 0
                else:
                    player_two.stamina = a
                # self.__if_stamina_negative(player_two)
                if self.__if_player_lost(player_one):
                    return f"Winner: {player_two.name}"
                if self.__if_player_lost(player_two):
                    return f"Winner: {player_one.name}"
                continue

    def next_day(self):
        new_players = []
        for player in self.players:
            a = player.stamina
            a -= player.age * 2
            if a < 0:
                player.stamina = 0
            else:
                player.stamina = a

            for i in range(len(self.supplies)):
                if self.supplies[i].__class__.__name__ == "Food":
                    player.stamina += self.supplies[i].energy
                    self.supplies.pop(i)
                if self.supplies[i].__class__.__name__ == "Drink":
                    player.stamina += self.supplies[i].energy
                    self.supplies.pop(i)
                    break
            new_players.append(player)
        self.players = new_players

    def __str__(self):
        result = ''
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}\n"
        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}"
        return result
    