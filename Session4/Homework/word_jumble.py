# Hint
text = "Overnight"
character = list(text)
print(character)

from random import choice
# print(choice(character))

for i in character:
    print("{0} {1}".format(choice(character)," "))