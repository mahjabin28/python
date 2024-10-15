try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError as y:
    print("Number error:", y)
except SyntaxError as x:
    print("Comma missing or invalid input:", x)
except Exception as e:
    print("Something went wrong. Please try again. Error:", e)
else:
    print("Everything is ok")
finally:
    print("Try other numbers")
