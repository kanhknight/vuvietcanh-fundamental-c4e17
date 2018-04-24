# Write a program that reads a string and returns a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter
# occurs. Case should be ignored. A sample output of the program when the user enters
# the data “ThiS is String with Upper and lower case Letters”, output:
# a 2
# c 1
# d 1
# e 5
# g 1
# h 2
# i 4
# l 2
# n 2
# o 1
# p 2
# r 4
# s 5
# t 5
# u 1
# w 2
string_a = "ThiS is String with Upper and lower case Letters".lower()
alphabet = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}

string_list = list(string_a)

for string in string_list:
    if string in alphabet:
        alphabet[string] +=1

for key,value in alphabet.items():
    if value !=0:
        print(key, value)
