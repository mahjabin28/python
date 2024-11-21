class Pair_elements():
    def sum(self,nums,target):
        store={}
        for i , num in enumerate (nums):
            if target-num in store:
                return (target-num,num)
            store[num]=i
num=(10,20,30,40,50,60,70)
value=int(input("Enter a number"))
print(Pair_elements().sum(num,value))


