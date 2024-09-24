n=int(input("Enter the number of row : "))
print("The symbol of the patter is *")
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()    
      