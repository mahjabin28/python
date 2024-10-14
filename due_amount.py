total=int(input("Enter your total amount: "))
paid=int(input("Enter your paid amount: "))
def pay():
    return(total-paid)
due=total-paid
print("Your due amount is", due)