import random

highest = 1000
answer = random.randint(1, highest)
tries = 1
# print(answer)   # TODO: remove after testing

print("Please guess a number between 1 and {}.\nYou have 10 guesses. ".format(highest))
guess = int(input())

while guess != answer and tries < 10:
    if guess == 0:
        break
    if guess > answer:
        print("Lower")
    else:
        print("Higher")
    guess = int(input())
    if guess == answer:
        print("Correct")
    tries += 1
if guess == answer:
    print("First try!")
if tries == 10:
    print("Better luck next time!")