from random import *
text_list = ["champion", "angle", "future", "learning", "specture"]
text_item = choice(text_list)
character = list(text_item)
for i in range(len(character)):
    chon = choice(character)
    print(chon, end = " ")
    character.remove(chon)
print()
run = True
while run:
    ans = input("Your Answer: ")
    if ans == text_item:
        print("Hura")
        run = False
    else:
        print("Again pls!")