# # creating file
# my_output_file = open('hello.txt', 'w')

# lines_to_write = ['This is my file.', '\n There are many like it,', '\nbut this one is mine.']

# my_output_file.writelines(lines_to_write)
# my_output_file.close()

# my_output_file = open('hello.txt', 'a')
# next_line = ['\nNON SEQUITUR']

# my_output_file.writelines(next_line)
# my_output_file.close()


# # reading file
# my_input_file = open('hello.txt', 'r')
# print('with comma\n')
# for line in my_input_file.readlines():
#     print(line),
# my_input_file.close()


# my_input_file = open('hello.txt', 'r')
# print('no comma\n')
# for line in my_input_file.readlines():
#     print(line)
# my_input_file.close()


# my_input_file = open('hello.txt', 'r')
# print('end=blank\n')
# for line in my_input_file.readlines():
#     print(line, end='')
# my_input_file.close()


# my_input_file = open('hello.txt', 'r')
# print('\nend=two new lines')
# for line in my_input_file.readlines():
#     print(line, end='\n\n')
# my_input_file.close()

my_input_file = open('hello.txt', 'r')

line = my_input_file.readline()

while line != '':
    print(line)
    line = my_input_file.readline()

my_input_file.close()
