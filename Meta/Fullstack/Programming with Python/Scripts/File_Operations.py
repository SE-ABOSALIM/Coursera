# # Read from a file
# read_file = open('./Files/Test.txt', mode = 'r')
# firstLine = read_file.readlines()
# print(firstLine)
# read_file.close()
#
# # Write to a file
# write_file = open('./Files/Test.txt', mode= 'a') # mode='w' Clears the file completely and write on it
# write_file.write('\nHello again from the code')
# write_file.close()

# Another way to open the file
try:
    with open('./Files/Test.txt', 'r') as file: # If the file non exist the error will be thrown
        data = file.readlines()
        for line in data:
            print(line, end='')
except Exception as e:
    print(e)



import random
try:
    f_name = input('Type the file name: ')
    f = open(f_name)  # "r" omitted as it's the default
    f_content = f.read()
    f_content_list = f_content.split("\n")
    f.close()
    print(f_content_list)
    print(random.choice(f_content_list))
except Exception as e:
    print(e)
