import os
print('Exist:', os.access('/Users/amina/Desktop/lab 6/a.txt', os.F_OK))
print('Readable:', os.access('/Users/amina/Desktop/lab 6/a.txt', os.R_OK))
print('Writable:', os.access('/Users/amina/Desktop/lab 6/a.txt', os.W_OK))
print('Executable:', os.access('/Users/amina/Desktop/lab 6/a.txt', os.X_OK))
