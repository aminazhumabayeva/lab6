from functools import reduce
numbers = [2, 3, 5, 7, 11]  # Sample list of numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"The product of all the numbers in the list is: {product}")
