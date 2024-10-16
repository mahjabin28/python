import math
try:
    inp = str(input("Write function name from math module: "))
    num = int(input("Write the number: "))
except ValueError:
    print("Something went wrong")
else:
    if inp == "square" or inp == "Square":
        print(math.sqrt(num))
    elif inp == "factorial" or inp == "Factorial":
        print(math.factorial(num))
    elif inp == "sine" or inp == "Sine":
        print(math.sin(math.pi/num)) 
    elif inp == "cosine" or inp == "Cosine":
        print(math.cos(math.pi/num))       

        


     