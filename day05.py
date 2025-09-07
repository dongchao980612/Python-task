#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/9/7 15:00
# File    : day05.py
# Software: PyCharm

def my_cmp(test_str):
    flag = True
    start = 0
    end = len(test_str) - 1
    for i in range(int(len(test_str) / 2)):
        # 不是
        if test_str[start] != test_str[end]:
            flag = False
            break
        # 是
        start = start + 1
        end = end - 1

    if flag:
        print("是")
    else:
        print("不是")


if __name__ == '__main__':
    # 字典  存储数据的容器，和 list 一样
    dic = {
        # 键:值 对
        "name": "zhang san",
        "age": 10,
        "score": [89, 90]
    }
    print(dic)

    # 字典的遍历
    # 方法1
    print(dic.items())  # [('name', 'zhang san'), ('age', 10)]
    print("遍历方法1：")
    for data in dic.items():
        print("字典的键是：", data[0], "字典的值是：", data[1])

    # 方法2
    print("遍历方法2：")
    for data in dic.items():
        key, value = data  # 解包，('name', 'zhang san')
        print("字典的键是：", key, "字典的值是：", value)

    # 方法3
    print("遍历方法3：")
    for key, value in dic.items():  # [('name', 'zhang san'), ('age', 10)]
        print("字典的键是：", key, "字典的值是：", value)

    names = ["zhangsan", "lisi", "wangwu"]
    # enumerate(names)之后是 [(0,"zhangsan"),(1,"lisi"),(2,"wangwu")]
    # 列表中的元素是元组的形式，可以用方式2、3
    for index, value in enumerate(names):
        print(value)

    mydata = [(0, "zhangsan"), (1, "lisi"), (2, "wangwu")]
    for index, value in mydata:
        print(value)

    l = [2, 356, 6, 6, 7, 3, 6, 4]
    print(sorted(l, reverse=False))  # 函数（变量,参数...）

    l = [2, 356, 6, 6, 7, 3, 6, 4]
    l.sort(reverse=True)  # 变量.方法(参数...)
    print(l)
    # reverse=True，从大向小，默认 reverse=False，即从小向大排序

    # 字典只能通过键，拿到值
    dic_name = dic["name"]
    dic_age = dic["age"]
    dic_score = dic["score"]
    # dic_score = dic["score1"]# 不存在的键会报错
    print(dic_name, dic_age, dic_score)
    all_keys = dic.keys()  # 获取所有的键
    print("all_keys=", all_keys)
    for key in all_keys:
        print(dic[key])  # 等价于 dic["name"]

    for index, key in enumerate(all_keys):
        print(index, dic[key])

    # 添加一项 总成绩
    dic["all_score"] = 99
    print(dic, len(dic))  # 4

    # 元组
    print("*" * 10)
    t = (1, 1, 3)
    print(t, type(t))  # tuple

    t1 = (1)  # 认为这是一个带括号的整数
    print(t1, type(t1))  # int

    t1 = (1,)  # 即使元组里面有一个元素，也要加一个逗号
    print(t1, type(t1))  # tuple

    print(t[1], t[2])

    # 遍历
    for i in enumerate(t):
        print(i)

    s = "hello"
    print(s[-1:-4:1])  # 字符串反转

    # 判断一个字符串是不是回文，字符串反转之后和原来一样
    #   是：abnvnba    abnvvnba
    # 不是：abuivern
    s1 = "abnvnba"
    s2 = "abnvvnba"
    s3 = "abuivern"
    print(s1[::-1] == s1)
    print(s2[::-1] == s2)
    print(s3[::-1] == s3)

    flag = True
    test_str = s3
    start = 0
    end = len(test_str) - 1
    for i in range(int(len(test_str) / 2)):
        # 不是
        if test_str[start] != test_str[end]:
            flag = False
            break
        # 是
        start = start + 1
        end = end - 1

    if flag:
        print("是")
    else:
        print("不是")

    print("="*20)
    my_cmp(s1)
    my_cmp(s2)
    my_cmp(s3)
