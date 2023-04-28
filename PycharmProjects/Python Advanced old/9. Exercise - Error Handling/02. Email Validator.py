class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


list_domains = [".com", ".bg", ".org", ".net"]

while True:
    email = input()
    if email == "End":
        break
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    user_name, domains = email.split('@')
    if len(user_name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    flag = True
    for dmn in list_domains:
        if not flag:
            break
        if dmn not in domains:
            flag = True
        else:
            flag = False
    if flag:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(list_domains)}")
    print("Email is valid")