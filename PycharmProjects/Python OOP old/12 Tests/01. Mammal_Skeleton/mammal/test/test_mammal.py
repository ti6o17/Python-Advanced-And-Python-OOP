from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    def test_proper_init_initialized(self):
        name = "Gogo"
        mammal_type = "Pig"
        sound = "Gruh"

        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound_string(self):
        name = "Gogo"
        mammal_type = "Pig"
        sound = "Gruh"
        mammal = Mammal(name, mammal_type, sound)

        result = mammal.make_sound()

        self.assertEqual("Gogo makes Gruh", result)

    def test_get_kingdom_type(self):
        name = "Gogo"
        mammal_type = "Pig"
        sound = "Gruh"
        mammal = Mammal(name, mammal_type, sound)
        result = mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info_returns_string(self):
        name = "Gogo"
        mammal_type = "Pig"
        sound = "Gruh"
        mammal = Mammal(name, mammal_type, sound)
        result = mammal.info()
        expected = "Gogo is of type Pig"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()

