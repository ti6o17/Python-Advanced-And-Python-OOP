def add_songs(*tuple_):
    new_dict = {}
    songs_list = []
    result = ''
    for elem in tuple_:
        if elem[0] not in new_dict:
            new_dict[elem[0]] = []

        new_dict[elem[0]].extend(elem[1])

    for song_title, text in new_dict.items():
        songs_list.append("- " + song_title)
        if text:
            songs_list.extend(text)
    result = '\n'.join(songs_list)
    return result


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
