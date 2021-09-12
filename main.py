# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised (str concatenation):
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for n in range(0, nr_letters):
    password += random.choice(letters)

for n in range(0, nr_symbols):
    password += random.choice(symbols)

for n in range(0, nr_numbers):
    password += random.choice(numbers)

print("Your password is: " + password)

# Hard Level - Order of characters randomised (use list to shuffle it then convert to string ):
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)


print(password_list)
random.shuffle(password_list)
print(password_list)

# convert list to string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# def StringToList(s):
#   # initialize an empty string
#     list1 = []
#   # traverse in the list
#     for ele in s:
#       list1 += ele
#     # return string
#     return list1


# password_list = StringToList(random_password)
# # print(password_list)

# random.shuffle(password_list)
# # print(password_list)

# def listToString(l):
#     # initialize an empty string
#     str1 = ""
#     # traverse in the string
#     for ele in l:
#         str1 += ele
#     # return string
#     return str1

# password_string = listToString(password_list)
# print("Your password is: " + password_string)
