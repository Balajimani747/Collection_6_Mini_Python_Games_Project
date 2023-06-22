import random
def odd_or_even():
    print("Welcome to the Odd or Even game!\n")
    print("-------------------------------------------------------------------------------")
    print("Game Rules:")
    print("1. The computer will randomly generate a number.")
    print("2. You need to guess whether the number is odd or even.")
    print("3. If your guess is correct, you win!")
    print("-------------------------------------------------------------------------------")
    while True:
        com_number=random.randint(1,100)
        print(f"Your Number is: {com_number}")
        ans=input("Guess The Number (odd/even):")
        if com_number%2==0:
            result="even"
        else:
            result="odd"
        if result==ans:
            print(f"Congratulations! Your Guess is Correct. Given Number is {result}")
        else:
            print(f"Sorry, Your Guess is Incorrect. Given Number is {result}") 
        print("-------------------------------------------------------------------------------")
        break
#odd_or_even()