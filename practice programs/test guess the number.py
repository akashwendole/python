import random
def guess_the_number_game(number):
   
    for i in range(3):
        user_number = int(input("Enter the number between 1-20:"))
        #print(number)
        if user_number < number:
            print("Your guessed number is too low")
        elif user_number > number:
            print("Your guessed number is too big")
        else:
            break
    
    if user_number == number:
        return "You have won the game!!!"
    else:
        print("The correct number was " + str(number))
        return "Better luck next time *_*"


secret_number = random.randint(1,20)
print(guess_the_number_game(secret_number))  