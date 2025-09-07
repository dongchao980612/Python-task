def fun_in_test1():
    print("fun_in_test1",__name__)

def fun_in_test2():
    print("fun_in_test2",__name__)


# fun_in_test1()# 调用
# fun_in_test2()# 调用

if __name__ == "__main__":# test
    fun_in_test1()# 调用
    fun_in_test2()# 调用