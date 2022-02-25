numbers_list = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numbers_list)): 
    is_even = (numbers_list[i]%2 == 0)
    if i==0:
        if is_even:
            print("The 1st term of list A is even.")
        else:
            print("The 1st term of list A is odd.")
    elif i==1:
        if is_even:
            print("The 2nd term of list A is even.")
        else:
            print("The 2nd term of list A is odd.")
    elif i==2:
        if is_even:
            print("The 3rd term of list A is even.")
        else:
            print("The 3rd term of list A is odd.")
    else:
        if is_even:
            print("The "+str(i)+"th term of list A is even.")
        else:
            print("The "+str(i)+"th term of list A is odd.")

number = [10,3,8,11,5,6]

for x in number: 
    if x % 2 == 0: 
        print(str(x) + " is even. ")
    else: 
        print(str(x) + " is odd. ")

"docstring"

List_Of_Integers = [int(x) for x in input().split()]
for x in List_Of_Integers: 
    b=(x%2)
    if (b==0): 
        print(str(x)+" is even")
    else: 
        print(str(x)+" is odd.") 


        
