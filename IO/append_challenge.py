with open("sample.txt", 'a') as jabber:
    for n in range(1, 13):
        print(n, "times 2 is", n * 2, file=jabber)
    else:
        print("-" * 25, file=jabber)