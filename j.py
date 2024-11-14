
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print("List of odd numbers:", odd_numbers)

