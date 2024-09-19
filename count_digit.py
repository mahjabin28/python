inp= int(input("Enter a number"))
count_digit= 0
temp=inp
while temp>0:
    temp//=10
    count_digit+=1
print(count_digit)    
