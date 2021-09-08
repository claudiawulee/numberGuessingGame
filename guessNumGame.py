import random

def guessingGame():
    numChosen = intro()
    #print(numChosen)
    cnt = 0
    guessAndCheck(numChosen,cnt)
    return

def intro():
    print("Welcome to the random number guesser!")
    input("Press Enter to Continue...")
    ran_num = random.randint(1,10)
    return ran_num


def guessAndCheck(num,cnt):
    userInput = input("Guess a number between 1 and 10 (inclusive)!\n")
    cnt +=1
    try:
        convertedInput = int(userInput)
    except:
        print("Your guess has to be an integer number between 1 and 10 (inclusive)\n")
        guessAndCheck(num,cnt)

    if convertedInput == num:
        print(num, "is the correct number! Nice job!")
        print("Total number of guesses: ", cnt)
        exit()
    elif convertedInput > num:
        print("That guess is too high. Guess again.\n")
        guessAndCheck(num, cnt)
        # recursion to do over
    elif convertedInput < num:
        print("That guess is too low. Guess again.\n")  # same with this
        guessAndCheck(num, cnt)
guessingGame()