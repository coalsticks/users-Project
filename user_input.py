def username_generator() -> str:        
    name = input("your name: ")        

    while not name.isalpha():           
        name = input("your name: ")    
    if len(name) < 5:                  
        name + str(len(name))
        return name
    return name[:5] + str(len(name))    # the name is sliced so that only the first 4 digits is present


user = username_generator()

print(user)
