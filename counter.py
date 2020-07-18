from collections import Counter

# empty Counter
counter = Counter()
print(counter)  # Counter()

# Counter with initial values
counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})

counter = Counter(a=2, b=3, c=1)
print(counter)  # Counter({'b': 3, 'a': 2, 'c': 1})

# Iterable as argument for Counter
counter = Counter('abc')
print(counter)  # Counter({'a': 1, 'b': 1, 'c': 1})

# List as argument to Counter
words_list = ['Cat', 'Dog', 'Horse', 'Dog']
counter = Counter(words_list)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

# Dictionary as argument to Counter
word_count_dict = {'Dog': 2, 'Cat': 1, 'Horse': 1}
counter = Counter(word_count_dict)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

# Counter works with non-numbers too
special_counter = Counter(name='Pankaj', age=20)
print(special_counter)  # Counter({'name': 'Pankaj', 'age': 20})

# getting count
counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
countDog = counter['Dog']
print(countDog)  # 2

# getting count for non existing key, don't cause KeyError
print(counter['Unicorn'])  # 0

counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
# setting count
counter['Horse'] = 0
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 0})

# setting count for non-existing key, adds to Counter
counter['Unicorn'] = 1
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Unicorn': 1, 'Horse': 0})

# Delete element from Counter
del counter['Unicorn']
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 0})

counter = Counter({'Dog': 2, 'Cat': -1, 'Horse': 0})

# elements()
elements = counter.elements()  # doesn't return elements with count 0 or less
for value in elements:
    print(value)

counter = Counter({'Dog': 2, 'Cat': -1, 'Horse': 0})

# most_common()
most_common_element = counter.most_common(1)
print(most_common_element)  # [('Dog', 2)]

least_common_element = counter.most_common()[:-2:-1]
print(least_common_element)  # [('Cat', -1)]

# subtract() and update()

# Counter subtract() method is used to subtract element counts from another counter.
# update() method is used to add counts from another counter.


counter = Counter('ababab')
print(counter)  # Counter({'a': 3, 'b': 3})
c = Counter('abc')
print(c)  # Counter({'a': 1, 'b': 1, 'c': 1})

# subtract
counter.subtract(c)
print(counter)  # Counter({'a': 2, 'b': 2, 'c': -1})

# update
counter.update(c)
print(counter)  # Counter({'a': 3, 'b': 3, 'c': 0})

# arithmetic operations
c1 = Counter(a=2, b=0, c=-1)
c2 = Counter(a=1, b=-1, c=2)

c = c1 + c2  # return items having +ve count only
print(c)  # Counter({'a': 3, 'c': 1})

c = c1 - c2  # keeps only +ve count elements
print(c)  # Counter({'a': 1, 'b': 1})

c = c1 & c2  # intersection min(c1[x], c2[x])
print(c)  # Counter({'a': 1})

c = c1 | c2  # union max(c1[x], c2[x])
print(c)  # Counter({'a': 2, 'c': 2})

counter = Counter({'a': 3, 'b': 3, 'c': 0})
# miscellaneous examples
print(sum(counter.values()))  # 6

print(list(counter))  # ['a', 'b', 'c']
print(set(counter))  # {'a', 'b', 'c'}
print(dict(counter))  # {'a': 3, 'b': 3, 'c': 0}
print(counter.items())  # dict_items([('a', 3), ('b', 3), ('c', 0)])

# remove 0 or negative count elements
counter = Counter(a=2, b=3, c=-1, d=0)
counter = +counter
print(counter)  # Counter({'b': 3, 'a': 2})

# clear all elements
counter.clear()
print(counter)  # Counter()
