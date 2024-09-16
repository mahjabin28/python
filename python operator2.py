a = int(input("Enter a number value: "))
b=int(input("Enter a number value: "))
c=int(input("Enter a number value: "))
if a>b and a>c and b!=c :
    print( a , " is greater than " , b , "and" , c ) 
elif b>a and  b>c and a!=c:
    print( b , " is greater than " , a ,"and" , c)
elif c>a and c>b and a!=b:
    print(c , " is greater than " , a ,"and" , b )
elif a == b and a>c:
    print(a, "is equal to", b, "and greater than", c)
elif a==b and a<c:
    print(a , "is equal to " , b , "and smaller than " , c )
elif a==c and a<b:
    print(a , "is equal to " , c , "and smaller than " , b )
elif a==c and a>b:
    print(a , "is equal to " , c , "and greater than " , b )
elif b==c and c>a:
    print(b , "is equal to " , c , "and greater than " , a )
elif c==b and c<a:
    print(c , "is equal to " , b , "and smaller than " , a )
elif a==b and b==c and c==a:
    print("All numbers are equal")  
else:
    print("Number invalid . Please try again")    




