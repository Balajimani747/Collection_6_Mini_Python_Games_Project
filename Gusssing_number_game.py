import random
def Gussing_number():
    print("Welcome to Gussing the Number Game\n")
    print(
    "Game Rules:\n 1.The Gussing the Number must be 1 to 50\n 2.Only Type Numbers\n 3.You have 6 Chance to Guss the Number\n")
    computer_num=random.randint(1,50)
    print(computer_num)
    count=0
    while True:
        user_num=int(input("Guss a Number :"))
        if count<6:
            if user_num>computer_num:
                print("You Gussed To High")
                count+=1
            elif user_num<computer_num:
                print("You Gussed To Low")
                count+=1
            elif user_num==computer_num:
                print(f"congratulations You Guss the Number correctly={computer_num}")
                print(f"you take totaly {count} chance to Guss the Number")
        else:
            print(f"You Tryped Your {count} Chance by game rules only 6 chance you not Guss correct number so You Loose the Game")
            break      
            