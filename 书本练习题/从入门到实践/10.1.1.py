'''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓读文件块↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())


# with open('C:\\Users\\fallo\PycharmProjects\\falloutDemo\\课本练习\\从入门到实践\\pi_digits.txt') as file_object:
#     content = file_object.read()
#     print(content.rstrip())


# filename = 'C:\\Users\\fallo\PycharmProjects\\falloutDemo\\课本练习\\从入门到实践\\pi_digits.txt'
# # 路径可用'pi_digits.txt'代替
# with open(filename) as file_object:
#     for line in file_object:  # 逐行读取，每行都覆盖赋值给line
#         print(line.rstrip())


# filename = 'C:\\Users\\fallo\PycharmProjects\\falloutDemo\\课本练习\\从入门到实践\\pi_digits.txt'
# # '''路径可用'pi_digits.txt'代替'''
# with open(filename) as file_object:
#     lines = file_object.readlines()  # 从文件读取每一行，并将其存储在列表lines中
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()  # 此处每行中的空格被rstrip删除
# print(pi_string)
# print(len(pi_string))
#
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()  # 删除所有的空格和空行用strip
# print(pi_string)
# print(len(pi_string))


# filename = 'pi_million_digits.txt'  # 大文件读取
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:52] + '...')
# print(len(pi_string))


# 圆周率里包含你的生日吗？
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for each_line in lines:
#     pi_string += each_line.strip()
# birthday = input("Enter your birthday, in the form mmddyy:")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of Pi!")
# else:
#     print("Your birthday does not appear in the first million digits of Pi.")

'''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑读文件块↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''






'''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓写文件块↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")  # 这里注意双引号是个小技巧，便于英文中的单引号的出现


filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I love programming too.\n")
    file_object.write("I love creating new games.\n")  # 结尾处务必带上换行符，上面代码段因为没有所以和第二段连在一起了

'''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑写文件块↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''