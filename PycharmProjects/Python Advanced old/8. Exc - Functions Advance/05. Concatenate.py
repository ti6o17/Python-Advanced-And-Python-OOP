def concatenate(*args, **kwargs):
    conc_string = ''
    for word in args:
        conc_string += word
    for element, new_element in kwargs.items():
        if element in conc_string:
            conc_string = conc_string.replace(element, new_element)
    return conc_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))