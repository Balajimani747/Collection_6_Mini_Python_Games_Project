def acronym_game():
    print("Welcome to Acronym's Game\n")
    print("-------------------------------------------------------------------------------")
    print("Game Rules:\n")
    print("1. One Player Game Mode")
    print("2. User To Enter The Full Form Of An Acronym Word.\n (Example:Enter the full form:central processing unit.\n Guess the acronym:CPU)\n")
    print("-------------------------------------------------------------------------------")
    while True:
        text= input ("Enter Full Form Of Acronym: ")
        user_ans=input("Guess the acronym: ")
        up_user_ans=user_ans.upper()
        setan_to_word=text.split()
        output=""
        for i in setan_to_word:
            output=output+i[0]
        up_case=output.upper()
        if up_case==up_user_ans:
            print(f"Congratulations! Your guess is correct. {up_case}")
        else:
            print(f"Sorry, your guess is incorrect. The correct acronym is: {up_case}")
        print("-------------------------------------------------------------------------------")
        break
#acronym_game()