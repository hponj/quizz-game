print("Welcome to my quizz game!!!")

playing = input("do you want to play? ")

if playing != "yes":
    sure = input("Are you sure? ")
    if sure == "yes":
        print("OK, Good bye")
        quit()

    else:
        playing = input("So, Do you want to play now? ")

print("Okay, lets play: ")
score = 0
# First question
answer = input('what does it stand for "LoL"? ').lower()

if answer == "laughing out loud":
    print("Correct")
    score = score + 1
    print("let's move on to the second question")
else:
    print("Incorrect")

# Second question

answer = input('2+2= ')

if answer == "4":
    print("Correct")
    score = score + 1
    print("let's move on to the Last question")
else:
    print("Incorrect")

# Third question
answer = input('who am I?').lower()

if answer == "human":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("quiz completed")
print("You solved " + str(score) + " question correctly!!")



