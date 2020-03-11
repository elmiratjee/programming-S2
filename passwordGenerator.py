import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
specialCharacters = '[@_!#$%^&*()<>?/\|}{~:]'
numbers = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

print ("Do you want to create a password?")
length = input ("Password length? \n")
length = int (length)

answerSettings = input("Do you want to add extra settings?\n")
if answerSettings == "yes":
    answerNumbers = input("Do you want numbers? \n")
    if answerNumbers == "yes":
        answersNumbersYes = answerNumbers

    answerUppercase = input("Do you want uppercases? \n")
    if answerUppercase == "yes":
        answersUppercaseYes = answerUppercase

    answerLowercase = input("Do you want lowercases? \n")
    if answerLowercase == "yes":
        answerLowercaseYes = answerLowercase

    answerSpecialchar = input("Do you want special characters? \n")
    if answerSpecialchar == "yes":
        answerSpecialcharYes = answerSpecialchar

    for l in range (length):
        answersNumbersYes = random.choice(numbers)
        answersUppercaseYes = random.choice(uppercase)
        answerLowercaseYes = random.choice(lowercase)
        answerSpecialcharYes = random.choice(specialCharacters)
        print(answersNumbersYes, sep=' ', end='', flush=True)
        print(answersUppercaseYes, sep=' ', end='', flush=True)
        print(answerLowercaseYes, sep=' ', end='', flush=True)
        print(answerSpecialcharYes, sep=' ', end='', flush=True)

else:
    print ('Here is your password: ')
    for r in range(length):
        passwordNoSettings = random.choice(characters)
        print(passwordNoSettings, sep=' ', end='', flush=True)
