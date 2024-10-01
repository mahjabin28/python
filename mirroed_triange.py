n = int(input("Enter the number of rows: "))
count = n*(-3)

for i in range(1, n+1):  
    for j in range(i):  
        print(count, end="")
        count += 1  
    print()  
