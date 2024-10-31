rainy=0
suny=0
tup=(0,1,0,1,0,1,0,1,0)
for i in range(len(tup)):
    if (tup[i]==0):
        rainy+=1
    else:
        suny+=1
if rainy<suny:
    print("Sunny day")
else:
    print("Rainy day")            
