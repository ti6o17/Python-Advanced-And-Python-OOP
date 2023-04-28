from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for album_check in self.albums:
            if album_check.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album_check in self.albums:
            if album_check.name == album_name:
                if album_check.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album_check)
                return f"Album {self.name} has been removed."
        return f"Album {self.name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for album_check in self.albums:
            result += f"\n{album_check.details()}"
        return result
