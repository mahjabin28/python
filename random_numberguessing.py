import random
import time
number=random.randint(1,100)
def intro():
    global name
    name=input("May I know your name , please?")
    print(name,"Let's play a game. I am thinking about a number between 1 to 100")
    if number%2==0:
        x="even"
    else:
        x="odd"  
    print("The number is an",x,"number")   
    time.sleep(.5)   
    print("Go ahead ! guess")
def pick():  
    guesstaken=0
    while guesstaken<6 :
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess<100 and guess<0:
                guesscount=guesscount+1
                if guess<6:
                    if guess<number:
                        print("The number is too low")    
                    if guess>number:
                        print("The number is too high") 
                    if guess!= number:
                        time.sleep(.5)   
                        print("Try again!") 
                    if guess==number:
                        break  
            if guess>100 or guess<0:
                print("Your guess is out of the range")     
        except:   
            print("I don't think that",guess,"is a number") 
    if guess==number:
        guesstaken=str(guesstaken)
        print("You have tried ",guesstaken,"times")    
    if guess!=number:
        print("Nope!The number i guessed was",str(number))
ply="yes"
while ply=="Yes" or ply=="YES"  or ply=="yes"or ply=="Y" or ply=="y" :
    intro()
    pick()
    print("Do you want to play again?")




