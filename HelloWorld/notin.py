name = input("What is your name? ")
age = int(input("What is your age? "))

if age < 18 or age > 30:
    print("You're not the right age, Sorry " + name)
else:
    print("Welcome aboard {}".format(name))

if 18 <= age < 31:
    print("Good")
else:
    print("sorry")