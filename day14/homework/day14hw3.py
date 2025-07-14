name = input("enter your name: ")
number_of_letters = int(input("how many letters are in your name? "))

i = 1
while i <= number_of_letters:
    print(name[:i])
    i = i + 1