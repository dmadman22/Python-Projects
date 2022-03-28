import sys

def user_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:  # Should really be except ValueError:
            print("You must enter an integer")
        finally:
            print("The finally clause always executes")
x = user_input("Enter first number \n")
y = user_input("Enter second number \n")

try:
    print("{} divided by {} is {}".format(x, y, str(x / y).strip(".0")))
except ZeroDivisionError:
    print("You cannot divide by zero!")
    sys.exit(2)
else:
    print("Division performed successfully")