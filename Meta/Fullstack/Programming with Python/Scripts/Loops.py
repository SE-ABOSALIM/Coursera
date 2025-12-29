languages = ['Python', 'Java', 'Javascript', 'C', 'C++']

for index, lang in enumerate(languages):
    print(f'{index+1}. {lang}')

print()
i=0
while i < len(languages):
    print(f'{i+1}. {languages[i]}')
    i += 1

print()
for lang in languages:
    if lang == 'C#':
        print('This is my favourite language')
        break
else:
    print("My favourite language isn't in the list")

print()
for lang in languages:
    if lang == 'Java':
        continue
    print(f'{lang} in the list (Not my favourite)')

# "pass" keyword allowing us to include an empty block of code without causing a syntax error.
# It does nothing and allows the program to continue execution normally.


print()
# Performance Test for nested loop
import time
start = time.time()

for i in range(10000):
    for j in range(100):
        print(j, end=' ')
    print()

end = time.time()
result = end - start

print(format(result, '.2f'))

# instanceOf(Java) -> isinstance(Python)
a = isinstance("aa", str)
print(a)