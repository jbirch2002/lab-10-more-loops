maximum_stories = 20

floor = int(input("On what floor of the building is your office? "))

while floor > maximum_stories:
    print("You entered " + str(floor) + ", but the building only has " + str(maximum_stories) + " floors. Try again...")
    floor = int(input("That's not a valid floor. The building has " + str(maximum_stories) + " floors. Try again..."))

print("Congrats! you work on floor: " + str(floor))