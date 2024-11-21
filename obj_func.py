class Str():
    def __init__(self):
        self.str1=""
    def get(self):
        self.str1=input("Enter a string")   
    def result(self):
        print("Converted sring:",self.str1.upper())   
s1=Str()   
s1.get()
s1.result()
  
