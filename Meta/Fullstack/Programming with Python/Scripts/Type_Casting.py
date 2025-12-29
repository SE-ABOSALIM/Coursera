"""
Explicit convertion: Conversion is done manually by the programmer using built-in functions like int(), float(), str(), etc.
"""
StringToNumber = '123'
print(int(StringToNumber)) # int

CantConvertToNumber = 'Hello'
# print(int(CantConvertToNumber)) # Error
print()


""" 
Implicit convertion: Conversion is done automatically by Python, without the programmer writing any code for it. 
It usually happens to prevent data loss.
"""
num1 = 3
num2 = 2.5
total = num1 + num2

print(total) # float (num1 Converted)