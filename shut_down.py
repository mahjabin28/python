from datetime import datetime
n = str(input("Enter your name: "))
current_time = datetime.now().time()
def func(n, current_time):
    print(n, "has shut down the laptop at", current_time)
func(n, current_time)
