import math
n = int(input())
if n%2==0:
    a = b = n//2;
else:
    a = n//2;
    b = n-n//2
for i in range(1000):
    if math.gcd(a,b)==1:
        break
    else:
        a-=1
        b+=1
print(a,b)
    