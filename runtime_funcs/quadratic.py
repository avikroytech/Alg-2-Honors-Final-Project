# A simple function that has a O(n^2) runtime
def quadratic(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += j
        sum += i
        
    return sum