def username_generator() -> str:        # using type-hinting to indicate that the return value is a string
    name = input("your name: ")         # input function will allow user to write their name

    while not name.isalpha():           # while loop is used to iterate the name input in case value
        name = input("your name: ")     # inserted is numeric instead of alphabetical
    if len(name) < 5:                   # if the length of the name input is less than 5 characters
        name + str(len(name))
        return name
    return name[:5] + str(len(name))    # the name is sliced so that only the first 4 digits is present


user = username_generator()

print(user)