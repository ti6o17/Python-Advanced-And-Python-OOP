from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert



class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @staticmethod
    def __return_concert(concerts):
        for concert in concerts:
            return concert

    @staticmethod
    def __return_band(bands):
        for band in bands:
            return band


    def __check_band_members_skills(self):
        concert = self.__return_concert(self.concerts)
        band = self.__return_band(self.bands)
        for member in band.members:
            if concert.genre == "Rock":
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if 'sing high pitch notes' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if 'play rock' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
            elif concert.genre == "Metal":
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if 'sing low pitch notes' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if 'play metal' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if concert.genre == "Jazz":
                if member.__class__.__name__ == "Drummer":
                    if "play the drums with brushes" not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer":
                    if 'sing high pitch notes' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                    if 'sing low pitch notes' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist":
                    if 'play jazz' not in member.skills:
                        raise Exception(f"The {band.name} band is not ready to play at the concert!")
            return True

    @staticmethod
    def __check_bands(band_name, band_list):
        for band in band_list:
            if band.name == band_name:
                return band
    @staticmethod
    def __check_musicians(musician_name, musician_list):
        for musician in musician_list:
            if musician.name == musician_name:
                return musician
    @staticmethod
    def __check_for_correct_type_band_members(band_name, bands):
        for band in bands:
            if band.name == band_name:
                count = 0
                for member in band.members:

                    if member.__class__.__name__ == "Guitarist":
                        count += 1
                    elif member.__class__.__name__ == "Drummer":
                        count += 1
                    elif member.__class__.__name__ == "Singer":
                        count += 1
                    if count >= 3:
                        return True

    def create_musician(self, musician_type: str, name: str, age: int):
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        elif musician_type == "Singer":
            musician = Singer(name, age)
        else:
            raise ValueError("Invalid musician type!")
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if not self.__check_musicians(musician_name, self.musicians):
            raise Exception(f"{musician_name} isn't a musician!")
        if not self.__check_bands(band_name, self.bands):
            raise Exception(f"{band_name} isn't a band!")
        musician = self.__check_musicians(musician_name, self.musicians)
        band = self.__check_bands(band_name, self.bands)

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if not self.__check_bands(band_name, self.bands):
            raise Exception(f"{band_name} isn't a band!")
        if not self.__check_musicians(musician_name, self.musicians):
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = self.__check_musicians(musician_name, self.musicians)
        band = self.__check_bands(band_name, self.bands)

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        if not self.__check_for_correct_type_band_members(band_name, self.bands):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        if self.__check_band_members_skills():
            concert = self.__return_concert(self.concerts)
            profit = concert.audience * concert.ticket_price - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."






