# Given and array of integers, reorder its entries so that the even entries appear first
from collections import Counter


def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    return arr


print(even_odd([1, 2, 3, 4, 5, 6]))

# Given a list of names (duplicates allowed), return a dictionary with key as name and value as number of occurences of that particular name in the list

names = ['Ravi', 'Yatin', 'Sahil', 'Yatin', 'Vikas', 'Ravi', 'Yatin', 'Vikas']
counter = Counter(names)
print(counter)


# Given a dictionary having key as name of employee and value as Employee object, print all employees with their attributes
employee = {'Yatin': 'Engineer', 'Sahil': 'Plumber', 'Prateek': 'Sweeper'}

for key, value in employee.items():
    print(key, value)


# to remove dupolicates from a list
mylist = [1, 3, 3, 4, 4, 6, 7, 2]  # it will not sort the output
mylist = list(dict.fromkeys(mylist))
print(mylist)

mylist = [1, 3, 3, 4, 4, 6, 7, 2]  # it will sort the output
mylist = list(set(mylist))
print(mylist)

# second way to remove duplicates from a list
ints_list = [1, 4, 3, 4, 3, 2]

temp = []

for x in ints_list:
    if x not in temp:
        temp.append(x)

ints_list = temp

print(f'Updated List after removing duplicates = {temp}')
