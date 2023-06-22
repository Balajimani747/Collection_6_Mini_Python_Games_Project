def word_count():
    print("Welcome Word Count Game!\n")
    print("-------------------------------------------------------------------------------")
    while True:
        text = input("Enter The Sentence: ")
        count = 0
        if text == "":
            print("you need to Enter the sentence")
            count = 0
        else:
            for i in text:
                if i == " ":
                    count = count + 1
            count = count + 1
            print(f"Total Word Count in the Sentence: {count}")
            print("-------------------------------------------------------------------------------")
            break

#word_count()
