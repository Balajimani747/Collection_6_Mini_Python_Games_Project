from Acronym_game import acronym_game
from Count_word_game import word_count
from Gusssing_number_game import Gussing_number 
from Odd_or_even_game import odd_or_even
from Paword_generator import paword_generator
from Rock_paper_scissors_game import Rock_paper_scissors

print("-------------------------------------------------------------------------------\n")
print("Welcome to the 6-Mini Games Using Python!")
print("-------------------------------------------------------------------------------")
while True:
    print("Games List: ")
    print("-------------------------------------------------------------------------------")
    print(" 1. Acronym Game\n 2. Count Word Game\n 3. Guessing Number Game\n 4. Odd Or Even Game\n 5. Password Generator\n 6. Rock Paper Scissors Game")
    print("-------------------------------------------------------------------------------")
    game = int(input("Enter the number of the game you want to play: "))

    def switch(game):
        if game == 1:
            acronym_game()
        elif game == 2:
            word_count()
        elif game == 3:
            Gussing_number()
        elif game == 4:
            odd_or_even()
        elif game == 5:
            paword_generator()
        elif game == 6:
            Rock_paper_scissors()
        else:
            print("Enter the number correctly")
    switch(game)
