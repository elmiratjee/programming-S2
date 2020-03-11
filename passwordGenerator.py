import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
specialCharacters = '[@_!#$%^&*()<>?/\|}{~:]'
numbers = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
count = 0
password = []

print("Do you want to create a password?")

answerSettings = input("Do you want to add extra settings?\n")
if answerSettings == "yes":
    answerNumbers = input("Do you want numbers? \n")
    if answerNumbers == "yes":
        countNumbers = input("How many numbers do you want? \n")
        countNumbers = int(countNumbers)
        while count < countNumbers:
            passwordNumbers = random.choice(numbers)
            password += (passwordNumbers)
            count += 1
    count = 0

    answerUppercase = input("Do you want uppercases? \n")
    if answerUppercase == "yes":
        countUppercase = input("How many uppercases do you want? \n")
        countUppercase = int(countUppercase)
        while count < countUppercase:
            passwordUppercase = random.choice(uppercase)
            password += (passwordUppercase)
            count += 1
    count = 0

    answerLowercase = input("Do you want lowercases? \n")
    if answerLowercase == "yes":
        countLowercase = input("How many lowercases do you want? \n")
        countLowercase = int(countLowercase)
        while count < countLowercase:
            passwordLowercase = random.choice(lowercase)
            password += (passwordLowercase)
            count += 1
    count = 0

    answerSpecialchar = input("Do you want special characters? \n")
    if answerSpecialchar == "yes":
        countSpecialchar = input("How many special characters do you want? \n")
        countSpecialchar = int(countSpecialchar)
        while count < countSpecialchar:
            passwordSpecialchar = random.choice(specialCharacters)
            password += (passwordSpecialchar)
            count += 1
    count = 0

    random.shuffle(password)
    listToStr = ''.join([str(elem) for elem in password])
    print( "Here is your password: " + listToStr)

else:
    length = input ("Password length? \n")
    length = int (length)
    print ('Here is your password: ')
    for r in range(length):
        passwordNoSettings = random.choice(characters)
        print(passwordNoSettings, sep=' ', end='', flush=True)
