#Direct Recursion
def direct_recursion(str, num):
    if num > 0:
        print(str, "Calling the recursive func with num = ", num)
        direct_recursion("Direct Recursion", num-1)
    
def main():
    direct_recursion("main", 7)

# main()

#Indirect Recursion
def func1(str, num):
    #Base Case
    if num > 0:
        print(str, "Called func1 with num =", num)
        func2("func1", num-1)

def func2(str, num):
    #Base Case
    if num > 0:
        print(str, "Called func2 with num =", num)
        func1("func2", num-1)
    
def main():
    func1("main", 7)

# main()

#Non-linear Recursion
# st = 'Ajibola'
# print(st[2:], 'b')

#Coding Exercise
# 1. Given a string, str, and a character, char, your function countChar should count the number of char characters in the string str. We have written a helper function countChar_ for you, but it only works for substring str[1:]. This means that you have to do processing for str[0] character while the rest of the answer can be found in the countChar_ function.
def countChar(str, char):
  '''
  you can call helper function as countChar_(str[1:], char)
  '''
  if len(str) <= 0:
    return 0
  if str[0] == char[0]:
    return 1 + countChar(str[1:], char)
  else:
    return countChar(str[1:], char)

# print(countChar('Ajibola', 'a'))

# 2. We are going to discuss Fibonacci numbers in the next lesson, but why don’t you take a look at the problem now that you know how simple recursion actually is!

# Fibonacci numbers are given by the following formulas:

# Fib(0) = 0Fib(0)=0

# Fib(1) = 1Fib(1)=1

# Fib(n) = Fib(n-1) + Fib(n-2)Fib(n)=Fib(n−1)+Fib(n−2)

# This results in the following sequence of numbers:

# 0,1,1,2,3,5,8,13,21,34...0,1,1,2,3,5,8,13,21,34...
# def fibonacci(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
    
# print(fibonacci(2))