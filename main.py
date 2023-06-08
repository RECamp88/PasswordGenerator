#Password Generator Project
import random

#Manually loading all the characters needed for each list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Interaction with user to get the number of each type they want in their generator
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print()
#Can use random.sample to get a random number of elements from a list 
password = []
if nr_letters > 0:
    password.extend(random.sample(letters, nr_letters))
if nr_numbers > 0:
    password.extend(random.sample(numbers, nr_numbers))
if nr_symbols > 0:
    password.extend(random.sample(symbols, nr_symbols))

#Shuffles the list and then using the "*" prints the list on a single line. 
random.shuffle(password)
print(*password)