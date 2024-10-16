import random
print("Let's Play ")
while True:
    user=input("Rock,Paper or Scissors")
    choice=["Rock","Paper","Scissors"]
    com=random.choice(choice)
    if com==user:
        print("Both the players chose  " ,com,"It's a tie")
    elif com=="Rock":
        if user=="Scissors":
            print("You win")  
        else:
            print("You loose . Try again") 
    elif com=="Scissors":
        if user=="Rock":
            print("You win")  
        else:
            print("You loose . Try again")  
    elif com=="Paper":
        if user=="Scissors":
            print("You win")  
        else:
            print("You loose . Try again")    
    play=input("Wanna Play again y/n  ")  
    if play=="n":
        break                        

        