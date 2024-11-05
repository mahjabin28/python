lis = {'banana': 2, 'grapes': 2, 'apple': 2}  
res = 0
k = 2

for key, value in lis.items():  
    if value == k: 
        res += 1  

print(res)
