import random
print("Welcome to Rock, Paper, Scissors")
user_score = 0
pc_score = 0
user_win = int(user_score) - int(pc_score)
pc_win = int(pc_score) - int(user_score)
outcomes = ["rock", "paper", "scissors", "end", "quit"]
game = input("Do you wanna play? :")
if game.lower() != "yes":
    quit()
while True:
    user_input = input("Type rock/paper/scissors or enter end to end game: ").lower()
    if user_input not in outcomes:
        continue
    if user_input == "quit":
        quit()
    random_number = random.randint(0,2)
    computer_pick = outcomes[random_number]
    if user_input == "rock" and computer_pick == "rock":
        print("You both chose rock!")
        continue
    if user_input == "rock" and computer_pick == "paper":
        print("You lost! the computer picked paper")
        pc_score += 1
        continue
    if user_input == "rock" and computer_pick == "scissors":
        print("You won! the computer picked scissors")
        user_score += 1
        continue
    if user_input == "paper" and computer_pick == "paper":
        print("You both chose paper!")
        continue
    if user_input == "paper" and computer_pick == "scissors":
        print("You lost! the computer picked scissors")
        pc_score += 1
        continue
    if user_input == "paper" and computer_pick == "rock":
        print("You won! the computer picked rock")
        user_score += 1
        continue
    if user_input == "scissors" and computer_pick == "scissors":
        print("You both chose scissors!")
        continue
    if user_input == "scissors" and computer_pick == "rock":
        print("You lost! the computer picked rock")
        pc_score += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("You won! the computer picked paper")
        user_score += 1
        continue
    if user_input == "end":
        if user_score > pc_score:
            print("Congrats! you won with " + str(user_score) + " points!")
        if pc_score > user_score:
            print("Oops! you lost to pc with " + str(pc_score) + " points.\nGood Luck next time!")
        quit()