n = int(input())
ans=0
while n>9:
    n -= 9
    ans += 9 + n%10
    n = n//10
    
print(ans+n)