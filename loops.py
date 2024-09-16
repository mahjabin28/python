#name="Helloworld"
#for i in name:
    #print(i)
#for x in range(4,20):
    #print(x)  

inp=int(input("Enter your number"))
sum = 0
for i in range(2,inp+1,2):
    sum+=i
    print("sum = ", sum)
print( "toatal sum" , sum)    