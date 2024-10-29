import random
play=True 
number=str(random.randint(1,10))
while play:
    inp=input("Guess a number from 1 to 10\n")
    if inp==number:
        print("Congrats!Your guess is correct")
        print("The number was",number)
        break
    else:
        print("Try again")    

