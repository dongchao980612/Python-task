from test import fun_in_test1,fun_in_test2
def fun1():
    print("fun1 in main",__name__)


"""
此时运行的文件的__name__是__main__
其他的被调用的文件__name__是自身的文件名
"""




if __name__ == "__main__":# 说明执行的是这个函数
    # fun1()# __main__ # 调用
    # fun()# 从test.py导入的, 此时的__name__ = test
    # print()
    # fun_in_test1()
    
    print(10)
    x = 11
    print(x)# print函数有一个默认分隔符， " "
    print(20,39)
    x1 = 12
    print(x1,x)
    print(10,20,sep=".")
    # printf(); c语言 不带回车  \n——newline
    print(10,20,end="*")#end指定用什么形式换行，默认是\n，可以认人为指定
    print("123")
    print("\n")# 此时n不再是字符n，而是换行符newline
    print("\a")# alert
    print("123\t123")# tab  123    123
    print("xingming:","zhangsan",sep="\t")
    print("xingming:\tzhangsan")

    # 字符串 
    s = "hello"
    s1 = 'hello'
    # I say "I am lihua "
    msg='I say "I am lihua "'
    print(msg)
    s = "hello"# 字符数组 有序的集合 
    #  01234
    print(s[0])# 字符串下标索引
    name = "zhangsan"
    ss = "nihao:"+name
    ss = "nihao:%s" % name # %s占位符-字符串
    age = 10
    ss = "今年%d岁了" % age# %d占位符-整数
    ss = "今年"+str(age)+"岁了"
    t = 27.454861 # 写一位小数，默认保持为6位
    """
    m.n  m表示所有位数,n表示小数位占几位
    m,n可以省略，省略后按照默认位数输出

    .2
    """  
    ss = "今天天气%-5.f度"%t # %f 占位符 小数
    """
    - 表示右边补空，缺省在坐标
    """
    print(ss)
