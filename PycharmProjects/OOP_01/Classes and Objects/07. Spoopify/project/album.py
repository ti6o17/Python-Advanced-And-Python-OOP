from project.song import Song


class Album:
    def __init__(self, name: str, *song: Song):
        self.name = name
        self.published = False
        self.songs = list(song)


    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if self._check_song(song.name):
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song_check in self.songs:
            if song_check.name == song_name:
                self.songs.remove(song_check)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def _check_song(self, song_name: str):
        for song_check in self.songs:
            if song_check.name == song_name:
                return True
        return False

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"\nAlbum {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for song_check in self.songs:
            result += f"\n== {song_check.get_info()}"
        return result






