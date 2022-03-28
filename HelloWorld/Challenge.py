# options = ["1.\tLearn Python", "2.\tLearn Java","3.\tGo swimming", "4.\tHave dinner",
#            "5.\tGo to bed", "0.\tExit"]
# selection = 1
# print("Please choose from your options in the list below:")
# while selection != 0:
#     for i in options:
#         print(i)
#     selection = int(input("What is your selection? "))
#     if selection >= 1:
#         print("You have chosen {}".format(selection))
#         print("Excellent choice. Enjoy!\n")
#     else:
#         print("You have chosen {}".format(selection))
#
# print("Goodbye")


choice = 9
while True:

    if choice == 0:
        break
    elif 1 <= choice <= 5:
        print("You chose {}".format(choice))
    else:
        print("Please choose your option")
        print("1.\tLearn Python")
        print("2\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print(("0.\tExit"))

    choice = int(input())