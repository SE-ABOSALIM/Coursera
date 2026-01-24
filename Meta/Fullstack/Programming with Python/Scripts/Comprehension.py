# List comprehension
print(
      '\n\n'
      '###################################\n'
      '#        List Comprehension       #\n'
      '###################################'
)

lst = [1,3,4,6,7,10,14,17,20,22,27,30,35]
print(f'Before Editing: {lst}')

lst = [x+2 for x in lst]
print(f'Add Two (Original List Mutated): {lst}')

multiply_two = [x*2 for x in lst]
print(f'Old lst: {lst}')
print(f'List created from the old: {multiply_two}')

mod_four = [x-1 for x in multiply_two if x%4 == 0]
print(f'New list (Divisible by four minus one): {mod_four}')

nines = [x for x in range(100) if x%7 == 0]
print(f'From 1-100 but the divisible by 9 ones {nines}')

lst2 = ['hello', 'i', 'love', 'rocket', 'league']
upper_case = [word.upper() for word in lst2]
print(f'Rocket League: {upper_case}')

# Dictionary comprehension
print(
      '\n\n'
      '###################################\n'
      '#     Dictionary Comprehension    #\n'
      '###################################'
)

using_range = {x:x*2 for x in range(12)}
print(f'Key -> 1-12, value -> (1-12)*2: {using_range}')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
number = [1,2,3,4,5,6,7,8,9,10,11,12]

months_number = {key:value for (key, value) in zip(months, number)}
print(f'Two lists to dictionary: {months_number}')



# List Comprehension
print(
      '\n\n'
      '###################################\n'
      '#         Set Comprehension       #\n'
      '###################################'
)

'''
The set comprehension deals with the set data type and it's very similar to list comprehension. 
The only key difference is the use of curly brackets for sets instead of square brackets as in lists.
'''
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)



# Generator Comprehension
'''
Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets. 
They are also more memory efficient as compared to list comprehensions.
'''
print(
      '\n\n'
      '###################################\n'
      '#      Generator Comprehension    #\n'
      '###################################'
)

data = [1,3,4,6,7,10,14,17,20,22,27,30,35]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for i in gen_obj:
      print(i, end=' ')