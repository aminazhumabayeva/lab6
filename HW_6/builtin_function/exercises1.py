#ex1

def num(list):
    answer = 1
    for i in list:
        answer *= i
    
    return answer

list = [2,3,4,6]

print(num(list))

#ex2

input1 = str(input())

cnt1 = 0
cnt2 = 0

for i in input1:
    if i.isupper():
        cnt1 += 1
    if i.islower():
        cnt2 += 1


# print(cnt1, " ", cnt2)
# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
#     for i in string:
#         if i.isupper():
#             upper_count += 1
#         elif i.islower():
#             lower_count += 1
#     return (upper_count, lower_count)
# result = count_upper_lower(input1)
# print(result)


#ex3
str = str(input())
str2=reversed(str)

if list(str)==list(str2):
    print("Palindrome")
else:
    print('Not palindrome')

#ex4
from time import sleep  
import math

number = int(input())
milliseconds = int(input())

sleep(milliseconds/1000)

print("Square root of {n} after {m} miliseconds is {sq}".format(n = number, m = milliseconds, sq = math.sqrt(number)))

#ex5
def true(tuple):
    for i in tuple:
        if not i:
            return False
    return True

tuple = (True, True)

print(true(tuple))