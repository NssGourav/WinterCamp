def questions(n, a):
    sorted_a = sorted(a)
    start, end = -1, -1
    for i in range(n):
        if a[i] != sorted_a[i]:
            if start == -1:
                start = i
            end = i
    if start == -1:
        return "yes\n1 1" 
    a[start:end+1] = a[start:end+1][::-1]  
    if a == sorted_a:
        return f"yes\n{start+1} {end+1}" 
    else:
        return "no"
 
n = int(input())
a = list(map(int, input().split()))
print(questions(n, a))
