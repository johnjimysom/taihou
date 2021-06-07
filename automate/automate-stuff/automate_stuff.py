
#how to automate in python, based on "how to automate the boring stuff" by al sweigart
#few lessons how to do stuff

#example
passwordFile = open('secretpasswordfile.txt')
secretPassword = passwordFile.read
print('Enter your password')
typedPassword = input()
if typedPassword == secretPassword
    print('Access granted')
    if typedPassword =='123456':
        print("That passoword is one that an idiot puts on theie luggage.")
else:
    print("access denied")