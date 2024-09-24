n=int(input("Enter the number of row: "))
count=1
for i in range(n):
    for j in range(i+1):
        print(count,end="")
        count= count+1
    print()    
      