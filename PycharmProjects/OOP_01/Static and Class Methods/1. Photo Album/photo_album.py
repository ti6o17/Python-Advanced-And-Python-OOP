from math import floor, ceil


class PhotoAlbum:
    PHOTOS_FOR_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    def __init_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_FOR_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for i in range(self.pages):
            if len(self.photos[i]) < PhotoAlbum.PHOTOS_FOR_PAGE:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        result = '-----------\n'
        picture = '[] '
        for i in range(self.pages):
            count_pictures = len(self.photos[i])
            result += f'{count_pictures * picture}' + '\n' + f"{'-----------'}" + '\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
