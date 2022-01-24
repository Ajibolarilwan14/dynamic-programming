#Problem Statement
# Given a string, str, you are required to output an array containing all the possible permutations of that string. By permutation, we simply mean all the different arrangements of the characters of that string.
# Input#
# Your input will be a single string str.

# str = "abc"
# Output#
# Your function should return a list of all possible permutations of the string str.

# permutations(str) = ["abc", "acb", "bac", "bca", "cab", "cba"]
from os import stat
import string


def toString(list):
    return ''.join(list)

# Solution 1
# def permutations(list, start, end):
# #     #base case
#     if start == end:
#         return toString(list)
#     #recurse function
#     else:
#         for i in range(start, end+1):
#             list[start], list[i] = list[i], list[start]
#             permutations(list, start+1, end)
#             temp = list[start], list[i] = list[i], list[start]
#             return temp
# string = 'ABC'
# n = len(string)
# a = list(string)

# print(permutations(a, 0, n-1))

# def temp(list, s, e):
#     for i in range(s, e+1):
#         list[0], list[i] = list[i], list[0]
#         temp(list, s+1, e)
#         t = list[0], list[i] = list[i], list[0]
#         return t

# print(temp(['A', 'B', 'C'], 0, 2))

# Solution 2
def permutations(str) -> list :
    #base case
    if str is "":
        return [""]
    
    permutation = []
    for char in str:
    #recursive function/step
        subpermutation = permutations(str.replace(char, "", 1))
        for each in subpermutation:
            permutation.append(char + each)
    return permutation
    #return type must be a list

print(permutations('abcd'))


