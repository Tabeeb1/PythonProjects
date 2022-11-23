import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

total_letter = int(input("How many letters would you like in your password: "))
total_symbols = int(input("How many symbols would you like?: "))
total_numbers = int(input("How many numbers would you like?: "))

password = []

for i in range(total_letter):
    password.append(random.choice(letters))

for i in range(total_numbers):
    password.append(random.choice(numbers))

for i in range(total_symbols):
    password.append(random.choice(symbols))

final_password = ""

for element in password:
    final_password += element

final_password = "".join(random.sample(final_password,len(final_password)))
print(final_password)
