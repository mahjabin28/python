def add(num1,num2):
    sum=num1+num2
    return sum 
def sub(num1,num2):
    sum=num1-num2
    return sum
def mul(num1,num2):
    sum=num1*num2
    return sum
def div(num1,num2):
    if num2==0:
        print("We cannot divide by 0")
    else: 
        sum=num1/num2
        return sum   
    
num1=int(input("Please Enter num1 "))  
num2=int(input("Please Enter num2 "))   
choice=str(input("a.addition \n5b.subtraction\nc.multiplication \nd.divison\nChoose one "))
if choice=='a' :
    add(num1,num2)
    res=add(num1,num2)
    print("The result is", res)
elif choice=='b' :
    res=sub(num1,num2)
    print("The result is" ,res)
elif choice=='c' :
    res=mul(num1,num2)
    print("The result is" ,res)
elif choice=='d' :
    res=div(num1,num2)
    print("The result is" ,res)
else :
    print("Invalid input")               
