import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
fruit['orange'] = "a sweet orange citrus"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour yellow citrus"
fruit['grape'] = "a sweet orb, grows in bunches"
fruit['lime'] = " a sour green citrus"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with salsa"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
# while True:
#     dict_key = input("Please enter a fruit \n")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We dont have a " + dict_key)
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + ": " + fruit[f])
for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())
fruit.close()
