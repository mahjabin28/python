inp= int(input("Enter your age"))
if inp>0 and 10>inp:
    print("Your age is less than 10")
elif inp>10 and 20>inp:
    print("Your age is between  10 to 20 years")
elif inp>20:
    print("Your age is greater than 20") 
else:
    print("Error . Try again")       