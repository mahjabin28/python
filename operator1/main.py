amount = float(input("PLease enter Amount in multiplication of 5,10, 50 or 100 for withdraw: "))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
note_4=(((amount%100)%50)%10)//5

print("notes of 100 Tk", note_1)
print("notes of 50 Tk", note_2)
print("notes of 10 Tk", note_3)
print("notes of 5 Tk", note_4)