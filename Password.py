import re
specialCharacters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
numbers = re.compile('[0-9]')
uppercase = re.compile('[A-Z]')

print ("Enter your password:")
password = input()
count = 0

if (len(password)<8):
    print("Password is too short")
else:
    print ("Password is at minimal length")
    count += 1

if (uppercase.search(password) == None):
    print("There is no uppercase being used")
else:
    print("There is at least 1 uppercase being used")
    count += 1

if (numbers.search(password) == None):
    print("No numbers")
else:
    print("There are numbers")
    count += 1

if(specialCharacters.search(password) == None):
    print("No special characters")
else:
    print("At least 1 special character")
    count += 1

if count == 0:
    print("\nVery weak password")
elif count == 1:
    print("\nWeak password")
elif count == 2:
    print ("\nOK password")
elif count == 3:
    print ("\nGood password")
elif count == 4:
    print ("\nVery strong password")
