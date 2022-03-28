panagram = """The quick brown
 fox jumps\tover 
 the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in seperators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6']

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)
new = []
for num in values_list:
    new.append(int(num))
print(type(new[1]))
print(new)
for num in values_list:
    print(int(num))

values_list = int(values_list)