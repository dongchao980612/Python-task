

if __name__ == "__main__":# 函数入口
    # 计算两个数的和
    a = 10
    b = 20
    res  = a + b
    print(res)

    # 程序中数据的来源
    # 1、定义好的 i=10
    # 2、用户输入的 i=input()
    # 3、从本地读取 excel pandas
    # 4、从网络上获取 爬虫
    # 计算两个数的和，两个数由用户输入决定
    a1=input()# 返回值是str
    b1=input()

    res1 =int(a1)+int(b1)# 前置类型转换 str -> int  
    print(res1)