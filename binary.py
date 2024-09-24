inp=int(input("Enter a number"))
bit=''
while inp>0:
    result=inp%2
    bit=str(result)+bit
    inp=inp//2
print(bit)    