def main():
    print("Hello from pyprj!")


"""
python 处理excel
python基础 无 
专业 编程 C 18 
变量 四则 输入输出 判断 循环 函数（**）  文件（*）
gcc  // xxx
int  double float 
"""
if __name__ == "__main__":
    #  变量 
    a = 10  # int
    b = 3.14  # float
    c = "hello"  # char* > String   str(in python)
    d = "10"  # str
    a = 2.9  # 最后一次赋值的类型 float
    # 字母数字下划线，数字不开头 注释
    # + = 10
    # #=10
    # @ = 10
    # 0a= 99
    """
    这些都是注释，不会被执行
    """
    res = type(b)  # 获取变量的类型
    print(res)
    # 用这个命令运行文件 : python xxx.py

    # 四则
    print(2 + 3, 1 - 2, 3 * 4, 12 / 4, 7 % 2, 5 / 2, 5 // 2)  # 数字和数字
    print(2 * 2, 2 ** 100)  # 幂运算，计算2的100次方，python 用于科学计算

    print("hello" + "world")  # 字符串和字符串 -> 拼接
    print("hello" * 3)  # 字符串和数字 重复n此

    # 输入 输出
    ## input() 函数,返回值是str,后续需要其他类型,要类型转换
    # print("请输入一些信息，并按下回车键")
    # inputdata = input() # 输入数据，给出一些提示，让用户知道该干什么
    # print("输入的数据是：")
    # print(inputdata)

    # inputdata = input("请输入一些信息，并按下回车键")
    # print("输入的数据是：")
    # print(inputdata)
    # str"10"  int("10")  -> int10  √
    tmp1 = "999"  # 字符串
    tmp2 = 10  # 数字类型
    tmp3 = int(tmp1)  # 字符串类型转换成数字类型
    print(type(tmp1), type(tmp2), type(tmp3))  # <class 'str'> <class 'int'>

    t = 2  # float
    print(float(t))

    age = 10  # int
    age = str(age)  # str
    msg = "我今年" + age + "岁了"  # str
    print(msg)
    age = int(age) + 1  # int
    age = str(age)  # str
    msg = "我今年" + age + "岁了"  # str
    print(msg)
