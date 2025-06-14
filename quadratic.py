# A simple function that has a O(n^2) runtime
def quadratic(n):
    for i in range(n):
        for j in range(n):
            print(j)
        print(i)