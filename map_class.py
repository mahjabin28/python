number1=[2,7,8,7,9]
number2=[8,9,4,3,8]
result=map(lambda x,y:x+y,number1,number2) 
print(list(result))
nums=[3,4,7,8]
def square(nums):
    return nums*nums
result2=list(map(square,nums))
print(result2)