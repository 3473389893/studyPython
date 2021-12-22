#  Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
import test

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
x = 'hello' \
    + 'world'

# Python3 中有六个标准的数据类型：
#
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
#
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


def hello():
    print(x)
    print(__name__)
    print(test.__name__)


if __name__ == '__main__':
    hello()
