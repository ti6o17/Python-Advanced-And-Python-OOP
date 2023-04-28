from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGES = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGES)
        return cls(pages)

    @staticmethod
    def __init_photos(pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    def add_photo(self, label):
        sht = 0
        for page in self.photos:
            sht += 1
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGES:
                page.append(label)
                return f"{label} photo added successfully on page {sht} slot {len(page)}."
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = ''
        result = separator + '\n'

        for page in self.photos:
            pages_ = len(page) * "[] "
            result += f"{pages_}\n" + separator + '\n'
        return result.strip()




album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

