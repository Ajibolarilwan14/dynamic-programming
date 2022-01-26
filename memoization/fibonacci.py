calculated = {}

def fibonnaci(num):
    if num == 0:
        return 0 #base case 1
    if num == 1:
        return 1 #base case 1
    elif num in calculated:
        return calculated[num]
    else:
        calculated[num] = fibonnaci(num - 1) + fibonnaci(num - 2)
        return calculated[num]
    
print(fibonnaci(50))
# print(calculated)