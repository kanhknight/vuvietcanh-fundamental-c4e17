from random import *
text = "champion"
character = list(text)
for i in range(len(character)):
    chon = choice(character)
    print(chon, end = " ")
    character.remove(chon)
print()

run = True
while run:
    ans = input("Your Answer: ")
    if ans == text:
        print("Hura")
        run = False
    else:
        print("Again pls!")
