
def match(words):
    count=0
    lst=[]
    for i in words:
        if (len(i)>1 and i[0]==i[-1]):
            count+=1            
            lst.append(i)
    print(lst)        
    return count  

result=match(["asa","sjhf","hfh"])
print(result)      




        