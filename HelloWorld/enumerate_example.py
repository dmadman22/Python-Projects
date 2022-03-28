# for index, char in enumerate("abcdefgh"):
#     print(index, char)

for t in enumerate("abcdefgh"):
    index, char = t
    print(index, char)

index, char = (0, 'a')
print(index)
print(char)