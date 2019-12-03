#!/usr/bin/env python3
# 当语句以':'结尾时，缩进的语句被视为代码块
# a = input('please enter a number:') # 这样用不行
# a = input() #这样也不行
# a = 100 #只能这样！！！why?
# 以解决，input()只能赋值为String，需要转型为int才能在后面作比较
a = int(input('please enter a number:'))
if a >= 0: #计算符左右两边似乎必须有空格隔开
	print(a)
else:
	print(-a)

