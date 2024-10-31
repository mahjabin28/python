def palind(inp):
    s=0
    e=len(inp)-1
    while s<e:
        if inp[s]!=inp[e]:
            return False
        s+=1
        e-=1
    
    return True   
inp=input("Enter a word ")
if palind(inp):
    print("The word is palindrom")
else:
    print("The word not palindrom")    





        