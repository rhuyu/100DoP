#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Define an empty string for user input to populate with
password = ""
#_ is a placeholder since the variable isn't going to be used
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_symbols):
    password += random.choice(numbers)
for _ in range(nr_numbers):
    password += random.choice(symbols)

#Takes current password and turns each string into a string via converting to a list    
password_shuffle = list(password)
#Use random.shuffle to change the order
random.shuffle(password_shuffle)
#Concatenates the list of strings together into one string with no space as the seperator
password = ''.join(password_shuffle)

#Used the old password variable to give new shuffled
print(f"Your new password is: {password}")
