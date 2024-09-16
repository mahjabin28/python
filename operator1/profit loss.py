actual_cost= float(input("Enter your buying cost"))
sale_amount=float(input("Enter your sale amount"))
if sale_amount>actual_cost:
    amount=sale_amount-actual_cost
    print("Total profit = {}".format(amount))
else:
    amount=actual_cost-sale_amount
    print(amount)