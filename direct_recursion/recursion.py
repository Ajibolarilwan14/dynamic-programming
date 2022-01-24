def direct_recursion(str, num):
    if num > 0:
        print(str, "Calling the recursive func with num = ", num)
        direct_recursion("Direct Recursion", num-1)
    
def main():
    direct_recursion("main", 7)

main()