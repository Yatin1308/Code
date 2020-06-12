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
