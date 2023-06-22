import random
data=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1',
'2','3','4','5','6','7','8','9','@','&','*','_','!','#']

def paword_generator():
    print("Welcome To Password Generator!\n")
    print("-------------------------------------------------------------------------------")
    print("It Will Generator Password Automatically\n")
    print("-------------------------------------------------------------------------------")
    while True:
        num=int(input("Enter The Number Of Digit Required In Your Password: "))
        pas_gem=""
        for i in range(1,num+1):
            ans=random.choice(data)
            pas_gem=pas_gem+ans  
        print(f"Password Generatoe For You: {pas_gem}")
        print("-------------------------------------------------------------------------------")
        break
#paword_generator()