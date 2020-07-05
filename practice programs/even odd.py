def even_odd(number):
    if number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"


print("To exit the program press x")

while True:
    number = input("Enter the number.")
    if number == 'x':
        break
    else:
        print(even_odd(int(number)))