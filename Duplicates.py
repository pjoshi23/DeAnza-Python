original_list = [1, 2, 1, 2, 3, 4, 3, 5, 4, 5, 6]
nonduplicates_list = set([])
duplicates_list = set([])
num = 0
for i in range(len(original_list)): 
    if original_list[i] in nonduplicates_list: 
        duplicates_list.add(original_list[i])
    else: 
        nonduplicates_list.add(original_list[i])
print(original_list)
print(nonduplicates_list)
print(duplicates_list)

