"""
A Pure Function is a function (a block of code) that always returns the same result if the same arguments are passed.
    - Pure functions return consistent results for identical inputs.
    - They do not modify external states or depend on mutable data.
    - Often used with immutable data structures to ensure reliability.
    - Their independence from external states makes them highly reusable.
"""

lst = [1,2,3]

# Not Pure Function
def add_to_list_not_pure(item):
    lst.append(item)
    return lst

result = add_to_list_not_pure(4)
print(lst)
print(result)


lst2 = [4,5,6]
# Pure Function
def add_to_list(item):
    lst_copy = lst2.copy()
    lst_copy.append(item)
    return lst_copy

result2 = add_to_list(7)
print(lst2)
print(result2)