try:
    num1,num2=eval(input("Enter two numbers separated by comma"))
    result=num1/num2
    print(result)
except ZeroDivisionError as y:
    print("Number error: ",y)    
except SyntaxError as x:
    print("Comma missing: ",x)
except:
    print("something went wrong. Please try again")
else:
    print("Everything is ok") 
finally:
    print("Try other numbers")           

