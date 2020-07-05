def addition(num1,num2):
    result = num1 + num2
    print("Addition of the two numbers is:- " + str(result))


def substraction(num1,num2):
    result = num1 - num2
    print("Substraction of the two numbers is:- " + str(result))


def multiplication(num1,num2):
    result = num1 * num2
    print("Multiplication of the two numbers is:- " + str(result))


def division(num1,num2):
    result = num1 / num2
    print("Division of the two numbers is:- " + str(result))


while True:

    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice:-"))
    if choice <= 4 and choice >=1:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        if choice == 1:
            addition(num1,num2)
        elif choice == 2:
            substraction(num1,num2)
        elif choice == 3:
            multiplication(num1,num2)
        elif choice == 4:
            division(num1,num2)
    else:
        break