import math

original_list = [10, 22, 44, 23, 4]
new_list2 = list(original_list)
print(original_list)
print(new_list2)

original_list.extend([5,6])
print(original_list)

original_list2 = original_list.copy()
print(original_list2)

original_list.clear()
print(original_list)

#find the middle index of an array

original_list = [10, 22, 44, 23, 4, 7, 1, 1, 6, 1, 3]

findMiddleIndex = math.floor(len(original_list) / 2)

print(findMiddleIndex)
print(original_list[findMiddleIndex])

removeFirstIndex = original_list.pop(0)
original_list.append(removeFirstIndex)
print(original_list)