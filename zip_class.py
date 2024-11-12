num1={6,9,9}
num2={8,9,6}
num3=list(zip(num1,num2))
print(num3)
li1=[6,9,7]
li2=[5,8,6]
for x,y in zip (li1,li2[::-1]):
    print(x,y)
    