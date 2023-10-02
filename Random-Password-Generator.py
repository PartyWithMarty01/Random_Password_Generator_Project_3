import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = letters
for random_letters in range(nr_letters):
  random_l = random.sample(letters, nr_letters)
  random.shuffle(random_l)

random_numbers = numbers
for random_numbers in range(nr_numbers):
  random_n = random.sample(numbers, nr_numbers)
  random.shuffle(random_n)

random_symbols = symbols
for random_symbols in range(nr_symbols):
  random_s = random.sample(symbols, nr_symbols)
  random.shuffle(random_s)


letters_str = ''.join(random_l)

numbers_str = ''.join(random_n)

symbols_str = ''.join(random_s)


password = letters_str + numbers_str + symbols_str
password_list = list(password)
random.shuffle(password_list)
new_password = ''.join(password_list)

print("Here is your new password: " + new_password)
