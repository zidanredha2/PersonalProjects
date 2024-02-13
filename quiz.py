print("Welcome to Computer Quiz")
play = input("Do you wanna play?")
if play.lower() != "yes":
    quit 
name = input("What is your name?")
print("Let's play, " + name + "!")
score = 0
cpu = input("What does CPU stand for?")
if  cpu.lower() == "central processing unit":
    score = score + 1
    print("Correct! your current score is " + str(score))
else:
    print("Incorrect!\nMake sure your answer is in lowercase and there is no typos!")
gpu = input("What does GPU stand for?")
if gpu.lower() == "graphics processing unit":
    score = score + 1
    print("Correct! your current score is " + str(score))
else:
    print("Incorrect!\nMake sure your answer is in lowercase and there is no typos!")
ram = input("What does RAM stand for?")
if ram.lower() == "random access memory":
    score = score + 1
    print("Congrats! your scored " + str(score) + "/3 in this quiz.")
else:
    print("Incorrect!\nMake sure your answer is in lowercase and there is no typos!")