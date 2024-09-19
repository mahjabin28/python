word= str(input("Enter your word "))
char= str(input("Write your characarter "))
i=0
count=0
while i<len(word):
    if word[i]==char:
        count+=1
    i+=1

print( "The character ",char, "is repeated" , count , "times")        

