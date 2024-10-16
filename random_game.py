import random
play=True 
number=str(random.randint(1,50))
while play:
    inp=input("Guess a number\n")
    if inp==number:
        print("Congrats!Your guess is correct")
        print("The number was",number)
        break
    else:
        print("Try again")    

