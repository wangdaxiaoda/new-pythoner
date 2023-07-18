# from package1.sub_package1.module2 import mul
import exe_module
from package1 import module1

num = 3
str1 = 'hello'
str2 = 'wdxd'


# print(str1 + str2)
# print(str1 * num)

str3 = '''
hello
wdxd
'''
# print(str3)

# 反转字符串 mystring[start:stop:step_size]
# reverse_str = str1[:4:1]
# print(reverse_str)


# 可以链式调用
# strM = str1.replace('lo', ' world').upper()

# 可以使用 f 来实现模版替换
# strM = f'{str1} world'
# print(strM)
# strA = f'3 + 3 = {3 + 3}'
# print(strA)

# print(f'{str1=} {str2=}')

# 运算符
# bool_a = True
# if bool_a:
#     print('lalal')
# else:
#     print('hahah')

# print(True < 3)

# 循环
# for i in 'string':
#     print(i)

# list = ['1', 2, True]
# for j in list:
#     print(j)

# count = 1
# while count <= 5:
#     print(count)
#     count += 1


# 函数默认值
def add(a, b=1, v=6):
    print(a + b * v)


# add(a=2, b=4)

# input 方法
# name = input('请输入你的名字:')
# print(f'你的名字是{name}')

# 实现的小功能
# is_right_name = False
# while not is_right_name:
#     name = input('请输入你的名字:')
#     if name.startswith('shen'):
#         is_right_name = True
#     else:
#         print('不符合规定，请重新输入')

# if __name__ == '__main__':
#     print('im main')
#     add(10)

print(module1.reduce(5))
