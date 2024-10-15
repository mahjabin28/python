try:
    inp=int(input("Enter a number: "))
except ValueError :
    print( "Something went wrong")
except :
    print("Something went wrong")     
if inp%2==0:
    print("Your age is an even number")  
else:
    print("your age is an odd number")





