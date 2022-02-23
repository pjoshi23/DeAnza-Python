"docstring"

List_Of_Integers = [int(x) for x in input().split()]
for x in List_Of_Integers: 
    b=(x%2)
    if (b==0): 
        print(str(x)+" is even")
    else: 
        print(str(x)+" is odd.") 
