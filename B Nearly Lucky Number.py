n = input().strip()
lucky = 0
for i in n:
    if i == '4' or i == '7':
        lucky += 1
 
str_luck = str(lucky)
is_lucky = "YES"
for j in str_luck:
    if j != '4' and j != '7':
        is_lucky = "NO"
        break
 
if is_lucky == "YES":
    print("YES")
else:
    print("NO")
