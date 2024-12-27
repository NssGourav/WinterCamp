import math
 
def triplets(n):
    count = 0
    for c in range(1, n + 1):
        for b in range(1, c):
            a_sqr = c * c - b * b
            if a_sqr <= 0:
                break
            a = int(math.sqrt(a_sqr))
            if a * a == a_sqr and a <= b:
                count += 1
    return count
 
n = int(input())
print(triplets(n))
