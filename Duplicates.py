a = [1, 2, 1, 2, 3, 4, 3, 5, 4, 5, 6]
b = set([])
c = set([])
num = 0
for i in range(len(a)): 
    if a[i] in b: 
        c.add(a[i])
    else: 
        b.add(a[i])
print(a)
print(b)
print(c)

