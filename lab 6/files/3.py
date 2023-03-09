import os
print("Test a path exists or not:")
path = '/Users/amina/Desktop/lab 6/a.txt'
print(os.path.exists(path))
path = '/Users/amina/Desktop/lab 6/a.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))