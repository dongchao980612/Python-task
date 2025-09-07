name = "zhanfsan"# 变量
def add(a,b):#a,b是参数
    pass
if __name__ == "__main__":
    s = "hello world"# 下标0开始  最后一个下标-1 
    # 字符列表->字符串 可迭代的对象，可以通过下表索引到元素
    # 列表 容器，存放元素，变量
    # 新建一个空列表
    l1 = []# 空列表
    l2 = [2,3.5 ,'a',"hello",l1,[1,2,3,4]]
    l3= list(s)# list强制类型转换，把可迭代的对象转化为list
    # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    # 把字符串中每一个字符，作为列表中的元素
    """
    int(3.2)# 3
    str(7)# "7"
    """
    #print(l1,l2,l3,s,type(l3))

    #计算长度
    print(len(l2))

    # 添加
    l1.append(2)# 0
    l1.append('hello') # 1
    l1.append('keqkjgrhb')# 2
    l1.append('bveuir')# 3
    # l1.append([2354,5346])


    # 修改
    # l1[0] = 99# 在字符串不允许

    # 删除
    # pop()  默认删除末尾元素
    # l1.pop()
    # pop(index)# 指定删除index位置的元素
    # l1.pop(2)

    # del 删除
    # del l1[2]

    # remove 删除某个值
    # l1.remove(2) # 删除成功
    # l1.remove(3)# 删除一个不存的数，报错

    # 插入
    print(l1)
    l1.insert(1,"world")
    l1.insert(-1,"last value")# 

    # 查找
    print(l1.index(2))# 返回索引
    # l1.index(3)  # 3 不在l1中，所以报错
    
    # 判断元素在不在列表中
    #print(3 in l1)# False
    #print(2 in l1)# True
    #print(3 not in l1)# # True
    print("*"*10)
    print(l1)

    # 遍历列表，使用for循环
    new_l = []
    for i in l1:
        print("元素是：",i)


    # ["zs",'li']

    # 生成序列（列表）[start,stop,step)
    data = list(range(0,10,2))# range对象强制转化为list对象
    print("data=",data)
    print("直接打印：",range(0,3))
    for  i in range(0,3):# 只能通过遍历查看元素
        print(i)
    """
    name =xxx

    """ 
    for n in ["zs",'li']:
        print("name = ",n)


    """
    int arr=[];
    for(int i=0;i<10;i++)
        printf("%d",arr[i]);
    """
    #l1的下标是从0~len(l1)-1
    l1_index = list(range(0,len(l1)))# 生成下标
    for index in l1_index:
        print(f"第{index}元素是：",l1[index])
    print("*"*10)
    # (0,2)  元组
    # enumerate(l1) -> [(0,2),(1,"world").....]# 取决于原来的l1的个数
    # enumerate会将l1变成类似于这样的数据类型，其实是列表，列表中每一项变为(下标,值)的形式
    # [(0,2),(1,"world").....]
    for i in enumerate(l1):
        # print(i[0],i[1])#  
        #        下标，值
        print(f"第{i[0]}元素是：",i[1])
    names = ["zhangsan","lisi","wangwu"]
    # enumerate(names)之后是[(0,"zhangsan"),(1,"lisi"),(2,"wangwu")]
    for name in enumerate(names):
        print(name[1])

    
