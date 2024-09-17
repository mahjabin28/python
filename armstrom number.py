num= int(input("Enter a number : "))
sum=0
tm= num 
while tm >0:
    digit = tm%10
    sum += digit**3
    tm //= 10
if num==sum:
    print("Then number is an armstrom number")
else:
    print("The number is not an armstrom number")