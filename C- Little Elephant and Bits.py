def delete(a):
    for i in range(len(a)):
        if a[i] == '0':
            return a[:i] + a[i+1:]
    return a[:-1]
a = input().strip()
print(delete(a))
