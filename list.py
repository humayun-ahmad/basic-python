even = []
for i in range(1,21):
    if i%2==0:
        even.append(i)
print(even)
odd = [i for i in range(1,21) if i%2]
print(odd)

