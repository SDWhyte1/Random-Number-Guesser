import random
ranNum = random.randint(0,9)
print(ranNum)
userQuest = None
counter = 0
while userQuest != ranNum:
    userQuest = input("Please guess a number between 0-9: ")
    counter = counter+1
    try:
        userQuestInt = int(userQuest)
    except:
        print("Please enter a number, you have entered a non-int")
        continue
    if userQuestInt == ranNum:
        print("You have successfuly guessed the correct number")
        break
    elif userQuestInt > ranNum:
        print("Your guess is too big, please try a smaller number")
        continue
    elif userQuestInt < ranNum:
        print("Your guess is too small, please try a bigger number")
        continue

print("You successfully guessed the correct number in",+counter,"guesses")
