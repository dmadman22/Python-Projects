user_input = input("Enter text to remove vowels:\n")
vowel_set = frozenset("aeiou")
user_set = []

for char in user_input:
    user_set.append(char)

user_set = set(user_set)

user_set.difference_update(vowel_set)
print(sorted(user_set))
