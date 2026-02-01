try:
    a = 5/0
except Exception as e:
    print('Cannot divide by zero. Error message:', e)



b = 'hello'
try:
    c = int(b)
except Exception as e:
    print(f"Type conversion error: '{b}' cannot be converted to an integer. Details: {e}")



lst = [1,2,3]
try:
    element = lst[6]
except Exception as e:
    print(e)