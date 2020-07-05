import random

def getNumber(number):
    if number == 1:
        return "Number is 1"
    elif number == 2:
        return "Number is 2"
    elif number == 3:
        return "number is 3"
    elif number == 4:
        return "number is 4"
    else:
        return "number is 5"



random_number = random.randint(1,5)
pick = getNumber(random_number)
print(pick)