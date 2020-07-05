def calculator(choice):
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    if choice == 1:
        result = num1 + num2
        print("Addition of the two numbers is:- " + str(result))
    elif choice == 2:
        result = num1 - num2
        print("Substraction of the two numbers is:- " + str(result))
    elif choice == 3:
        result = num1 * num2
        print("Multiplication of the two numbers is:- " + str(result))
    elif choice == 4:
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
        calculator(choice)
    else:
        break