import shelve

with shelve.open("cave_ini") as cave_init:
    loc = 1
    while True:
        availableExits = ", ".join(cave_init["exits"][loc].keys())

        print(cave_init["locations"][loc])

        if loc == 0:
            break

        direction = input("Available exits are " + availableExits + " ").upper()
        print()
        # Parse the user input, using our vocabulary dictionary if necessary
        if len(direction) > 1:   # more than one letter, so check vocab
            words = direction.split()
            for word in words:
                if word in cave_init["vocabulary"]:
                    direction = cave_init["vocabulary"][word]
                    break

        if direction in cave_init["exits"][loc]:
            loc = cave_init["exits"][loc][direction]
        else:
            print("You cannot go in that direction")
