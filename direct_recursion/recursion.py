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

main()