menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# for meal in menu:
#     # print(meal)
#     for i in meal:
#         if "spam" not in i:
#             print(i, end=" ")
#     print()

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if "spam" in (meal[index]):
            del meal[index]
    print(", ".join(meal))
