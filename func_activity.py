cityinp=input("Enter the city name")
nightinp=(int(input("Enter how many nights you want to stay: ")))
def travel(cityinp):
    if cityinp=="Dhaka":
        return 10000
    elif cityinp=="Sylhet":
        return 9000
    elif cityinp=="Chattogram":
        return 7000
    elif cityinp=="Khulna":
        return 6000
    else:
        print("Wrong input")
def hotel(nightinp):
    if nightinp>=7:
        return 4000*nightinp 
    elif nightinp<7 and nightinp>=3:
        return 5000*nightinp
    elif nightinp>3:
        return 6000*nightinp
    else:
        print("wrong input")
trav=travel(cityinp) 
hot=hotel(nightinp)  
print("total bill",trav+hot)  
    
      





    