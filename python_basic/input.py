str = input()
n = len(str)
cnt=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if str[i]=='Q' and str[j]=='A' and str[k]=='Q':
                cnt += 1
print(cnt)
            