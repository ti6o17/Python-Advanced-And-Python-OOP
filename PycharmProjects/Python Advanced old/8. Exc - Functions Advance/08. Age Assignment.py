def age_assignment(*args, **kwargs):
    result = ''
    new_dict = {}
    for j in range(len(args)):
        count = -1
        for letter in kwargs:
            # count += 1
            x = args[j]
            if letter in args[j]:
                new_dict[args[j]] = kwargs[letter]
    sorted_new_dict = sorted(new_dict.items(), key=lambda y: y[0])
    for name, age in sorted_new_dict:
        result += f"{name} is {age} years old." + "\n"
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))