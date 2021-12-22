#  Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
import test

# 1.多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
x = 'hello' \
    + 'world'


# 2. Python3 中有六个标准的数据类型：
#
# 判断数据类型 print(type(x))
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）

# 2.1 Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）（数组）、Dictionary（字典）（对象）、Set（集合）。
#

# 2.2 List（列表）————数组
#       list = [ 'abed', 786 , 2.23, 'noob', 70.2 ]
#   print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表
#

# 2.3 Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )

# 2.4 Set（集合）
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# 2.5 Dictionary（字典）键(key) : 值(value) 的集合。————对象
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

def hello():
    print(x)  #
    print(__name__)  # __main__
    print(test.__name__)  # test
    print(type(x))  # <class 'str'>


if __name__ == '__main__':
    hello()
