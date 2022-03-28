def backwards(*args, end=' ', **kwargs):
    print(kwargs)
    try:
        for word in args[::-1]:
            print(word[::-1], end=' ', **kwargs)
    except TypeError:
        pass

with open('text.txt', 'w') as file:
    backwards("hello", "bob", "carol", "help, I've fallen and I can't get up", end='\n')

print()
print("hello", "bob", "carol", "help, I've fallen and I can't get up", end='\n', sep='|')