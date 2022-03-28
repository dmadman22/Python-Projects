low = 1
high = 100

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    print("\t Guessing in the range of {} and {}.".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?\n "
                     "Enter h or l, or c if my guess it correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess high. Low end of range becomes 1 greater than guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. High end of range becomes one less than guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses = guesses + 1

else:
    print("Your number is {}".format(low))
    print("It took {} guesses".format(guesses))