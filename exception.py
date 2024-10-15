try:
    var=int(input("Enter a number"))
    print(var)
except ValueError as x:
    print("Error",x) 
