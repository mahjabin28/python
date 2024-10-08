x=int(input("Enter your number: "))
def func(x):
    if x==0 or x==1:
        return 1 
    else:
        return x*func(x-1)
        
print("The result is" , func(x))        
