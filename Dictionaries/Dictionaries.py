fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit grows in bunches",
         "lime": "a sour green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmm... lovely",
       "spinach": "can I have some more fruit, please?"}

print(veg)

veg.update(fruit)
print(veg)

print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

print 