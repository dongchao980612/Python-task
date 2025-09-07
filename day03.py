

if __name__ == "__main__":
    s="hello world,ZHANGSAN"
    print(s.title())
    print(s.upper())
    print(s.lower())

    s1 = "     hello    "
    print(s1.strip())
    print(s1.lstrip())
    print(s1.rstrip(),end="")# right
    print("***")

    print("acdsbsn".isalpha())# 判断是否都是字母
    print("111".isdigit())
    print("11a1".isalnum())
    print("www.baidu.com".startswith("www"))
    print("www.baidu.com".endswith("com"))

    # 判断邮箱是否合理 T/F
    # xxxx@qq.com
    print("xxxx@qq.com".endswith("qq.com"))
    print(len("hello"),"hello"[1])
    msg="hello"# 字符串是常量，不允许修改
    # msg[0]="H"
    new_msg = msg.title()
    print(new_msg)

    s="hello world,ZHANGSAN"
    new_s = s.find("zhagnsan")
    print(new_s) # 找到返回索引坐标，找不到返回-1
    # print(s.index("zhagnsan"))# 找到返回索引坐标，找不到报错 ValueError 
    
    url="www.baidu.com"
    print(url.split("."))# 列表 ['www', 'baidu', 'com']

    # 用户输入姓名,性别,年龄[以空格分隔]，并打印输出
    # data = input().split(" ")
    # print("姓名：",data[0])
    # print("性别：",data[1])
    # print("年龄：",data[2]) 


    name = "lisi"
    s1 = "nihao:" + name
    s2 = "nihao:%s" % name # %s占位符-字符串
    s3 = "nihao:{}".format(name)

    # format
    s4 = f"nihao:{name}" 
    print(s1,s2,s3,s4)
    # 日志  
    # xxx文件,在xxx时间,发生报错,错误行数:xxx,原因xxx
    fiilename = "main.py"
    datatime = "12.34"
    linenum = 5
    cause = "value error"
    log = f"{fiilename}文件,在{datatime}时间,发生报错,错误行数:{linenum},原因{cause}"
    print(log)
    fiilename="demo.py"
    log = f"{fiilename}文件,在{datatime}时间,发生报错,错误行数:{linenum},原因{cause}"
    print(log)
    
    #    0123456789
    #             o:-2 m:-1
    url="wwwbaiducom"# 字符串切片操作,连续的一个子串
    print(url[3:8])# [start:end)左闭右开的区间
    print(url[:8])# 缺省start,默认从0开始
    print(url[3:])# 缺省end,，默认从最后结束
    print(url[:])# 缺省start,缺省end,表示复制

    print(url[3:8:2])# start,end,step,默认step=1, 隔step个取1个
    print(url[-4:-2])

    # 163 126
    email = "myemailname@qq.com" # 用户名是四位，帮我获取用户名和邮箱的类别
    name = email[:4]# 切片
    name = email.split("@")[0]# 分割
    ty = email[5:]
    ty = email[-6:]
    ty=email.split("@")[-1]
    # 10 02 03 1987 03 20 2948
    print(name,ty)

    # 字符串 列表 [data1,data2,data3] 字典 [key键:value值]{name:zs,age:12} 
    # 循环 判断