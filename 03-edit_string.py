name = 'ada lovelace'
# title()方法 以首写字母为大写显示每个单词
print(name.title())

name = 'Ada Lovelace'
# upper() 方法 将字符串单词全部改为大写
print(name.upper())

name = 'ADA LOVELACE'
# lower() 方法 很有用 很多时候 无法靠用户来提供正确的大小写
# 因此需要将字符串先转换为小写 在储存它们 以后需要显示这些信息的时候
# 再将其转换为合适的大小写
print(name.lower())

# 在字符串中使用变量
first_name = 'ada'
last_name = 'lovelace !!!'
# 在字符串中使用变量的值 要在引号前面加上字母 f (format)
# f (format) 设置格式的简写 在使用{} 来读取变量的值
full_name = f'{first_name} {last_name}'
print(full_name)

# 使用变量创建整条消息
# print(f'hello, {full_name.title()}')
message = f'hello, {full_name.title()}'
print(message)

# 注意点:
# f 字符串是Python 3.6 引入的 如果使用 Python 3.5或者更早的版本
# 需要使用 format() 这个方法 而不是 f 语法
# full_name = '{} {}'.format(first_name,last_name)

