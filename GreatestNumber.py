a = [5,16, 23, 47, 84, 73, 69]
max = a[0]
for i in range(len(a)): 
    if max < a[i]:
        max = a[i]

print(max)

