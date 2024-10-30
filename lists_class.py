
lst = []
i = ""
while True:
    i = input("Enter words and write 'break' at the end: ")
    if i == "break":
        break
    lst.append(i)
def match(words):
    count = 0
    result_lst = []  
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
            result_lst.append(word)
    print("Matching words:", result_lst)
    return count  
result = match(lst)
print("Number of matching words:", result)




        