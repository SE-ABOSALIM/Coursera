print("\nLists")
lst = [1, 2, 3, 4, 5] # Mutable
print(f'The list: {lst}')
print(f'Length: {len(lst)}')
lst.append(6) # Add element
print(f'Add "6": {lst}')
lst.pop(1) # Remove Element from specific index
print(f'Remove index 1: {lst}')
lst.extend([6,7,8,9]) # Concat a new list
print(f'Concat with another list: {lst}')
lst.remove(3) # Remove specific element
print(f'Remove the Element "3": {lst}')



print("\nTuples:")
tpl = (1,2,3,4,5, 'hello', 3, 3) # Immutable
print(f'The Tuple: {tpl}')
print(f'The Element at index 1: {tpl[1]}', end=', ') # Access element from tuple
print(f'The Element at index 4: {tpl[4]}')
print(f"Count of the number 3: {tpl.count(3)}") # The number of 3 in the tuple
print(f'The index of number 5: {tpl.index(5)}') # The index of 5



print("\nSets:")
st = {1,2,3,4,5,1,2,3,1,1,2,10,15}
st2 = {7,8,9,1,2,3,4,5}
print(f'st: {st}')
print(f'st2: {st2}')
print(f'Concat st & st2: {st.union(st2)}') # Concat 2 sets
print(f'Concat st & st2: {st | st2}') # Concat 2 sets
print(f'Common Elements between st & st2: {st.intersection(st2)}') # Common elements (Same as st & st2)
print(f'The Elements only in st & not in st2: {st.difference(st2)}') # The Elements only in one set (Same as st - st2)
print(f'The Unique elements in st & st2: {st.symmetric_difference(st2)}') # Unique values (Same as st ^ st2)
st.add(6) # Add element
print(f'Add the Element "6": {st}')
st.remove(1) # Remove element -> If the element doesn't exist the error will be thrown
print(f'Remove the element "1": {st}')
st.discard(2) # Remove element -> If the element doesn't exist, nothing will happen
print(f'Remove the element "2": {st}')
# print(st[0]) # Error set doesn't have sequence we cannot access by index



print('\nDictionaries:')
dic = {1: 'Java', 2: 'Javascript', 3: 'Python'}
print(f'The dictionary: {dic}')
print(f'The value in key 1: {dic[1]}')
print(f'The value in key 3: {dic[3]}')
print('All values & keys:')
for key, value in dic.items():
    print(f'{key}: {value}')