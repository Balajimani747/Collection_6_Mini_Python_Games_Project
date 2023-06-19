import random
print("Welcome to Rock-Paper-Scissors Game\n")
print("Game Rules:\n 1.Rock Vs Paper ---> Paper Win \n 2.Scissors Vs Rock ---> Rock Win \n 3.Paper Vs Scissors ---> Scissors Win\n")
while True:
    def Rock_paper_scissors():
        print("Enter Your Choice")
        print ("1.Rock\n2.Paper\n3.Scissors\n")
################################ user part #######################################################
        def Switch_case_(user_data):
            if user_data==1:
                print("User Choice: Rock\n")
                a="Rock"
                return a
            elif user_data==2:
                print("User Choice: Paper\n")
                b="Paper"
                return b 
            else:
                print("User Choice: Scissors\n")
                c="Scissors"
                return c
        user_data=int(input("User Turn Enter Your Choice: "))
        ud=Switch_case_(user_data)
        
################################## Computer part #########################################################    
        choice_list=["Rock","Paper","Scissors"]
        cd=random.choice(choice_list)
        print("Computer Turn Enter Your Choice:")
        print("Computer Choice:",cd)
# #################################### logic ################################################################
        if ud==cd:
            print("\n")
            print("Game Was Tie Play Again")
            print("--------------------------------------------------------------------\n")
        elif(
             (ud=="Rock" and cd=="Scissors")or 
             (ud=="Scissors" and cd=="Paper") or
             (ud=="Paper" and cd=="Rock")):
            print("\n")
            print("YOU WIN!!")
            print("--------------------------------------------------------------------\n")
        else:
            print("\n")
            print("COMPUTER WIN!!\n")
            print("--------------------------------------------------------------------")            

