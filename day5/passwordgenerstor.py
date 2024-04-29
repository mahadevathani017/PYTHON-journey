#password generator
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to the Pypassword Generator!\n")
nr_letters=int(input("how many letters you want\n"))
nr_symbols=int(input("how many symbol you want\n"))
nr_numbers=int(input("how many numbers you want\n"))

password=""
for char in range(1,nr_letters+1):
    # random_char=random.choice(letters)
    password+=random.choice(letters)

for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)  

for char in range(1,nr_symbols+1):
    password+=random.choice(symbols) 

print(password)

