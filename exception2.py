valid=False
try:
    while not valid:
        n=int(input("Enter a number: "))
        while n%2==0:
            print("bye")
except ValueError as x:
    print(x)            
        

