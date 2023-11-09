user_input = int(input("Gimme a number that is greater than 100: "))

while user_input >= 100:
    print(str(user_input) + " is less than 100, try again...")
    user_input = int(input("Nope, not what I asked for... Gimme a number greater than 100 plz: "))

print(str(user_input) + " is greater than 100! Good job!")