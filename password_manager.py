import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [0,1,2,3,4,5,6,7,8,9]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("Welcome to the pypassword generator!")

nr_letters = int(input("How many letter would you like in your password?\n"))
nr_numbers = int(input("How many number would you like in your password?\n"))
nr_symbol = int(input("How many symbol would you like in your password?\n"))

password = []

for char in range (0, nr_letters):
    lett = random.choice(letter)
    password += lett


for char in range (0, nr_numbers):
    num = str(random.choice(number))
    password += num


for char in range (0, nr_symbol):
    sym = str(random.choice(symbol))
    password += sym

random.shuffle(password)

password = "".join(password)

print(password)
