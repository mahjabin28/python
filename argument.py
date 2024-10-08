def bill_pay(bill,tip):
    total=bill*(1+0.001*tip)
    total=round(total)
    return total
pay=bill_pay(150,20)
print(f"Please pay $ ",pay )