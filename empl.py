class Bird():
    def __init__(self):
        print("Classbird created")
    def __del__(self):
        print("Class bird deleted")   
def func() :
    print("Function created")
    obj=Bird()      
    print("calling class") 
    return obj
print("First print") 
obj=func()  
print(obj) 
print("Programme end")
