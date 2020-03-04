import random

print ("Do you want to create a password?")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input ("Password length? \n")
length = int (length)

print ('Here is your passowrd: ')

for l in range(length):
    password = random.choice(characters)
    print(password, sep=' ', end='', flush=True)
