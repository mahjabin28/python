import random

print("Let's Play!")

try:
    while True:
        user = input("Rock, Paper, or Scissors? ").capitalize()
        choice = ["Rock", "Paper", "Scissors"]
        com = random.choice(choice)
        
        if user not in choice:
            print("Your answer is invalid, try again.")
            continue
        
        print(f"Computer chose: {com}")

        if com == user:
            print(f"Both players chose {user}. It's a tie!")
        elif com == "Rock":
            if user == "Paper":
                print("You win! Paper covers Rock.")
            else:
                print("You lose! Rock crushes Scissors.")
        elif com == "Scissors":
            if user == "Rock":
                print("You win! Rock crushes Scissors.")
            else:
                print("You lose! Scissors cut Paper.")
        elif com == "Paper":
            if user == "Scissors":
                print("You win! Scissors cut Paper.")
            else:
                print("You lose! Paper covers Rock.")
        
        play = input("Wanna play again? (y/n): ")
        if play == 'n':
            break
except Exception as e:
    print(f"Something went wrong: {e}, please try again.")
