def print_msg(message):
    greeting = "Hello!"

    def printer():
        print(greeting, message)

    return printer

func = print_msg("Python is awesome")
func()

lol = print("lol")
lol