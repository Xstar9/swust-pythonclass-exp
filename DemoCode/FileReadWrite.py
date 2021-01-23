import os  # 引入读写
# 读写  r w rb wb   只读   只写   读二进制 写二进制  模式
'''
f = open("text.txt", "w")
f.write("hello world!\n")
f.write("hello world!\n")
f.close()
f = open("text.txt", "r")
# content = f.read(10)     # 读一行的10个字符
# contents = f.readline()  只读一行
contents = f.readlines()   # 读所有行 以列表形式打印
print(contents)
i = 1
for j in contents:
    print("%d:%s" % (i, j))
    i += 1
f.close()
os.rename("text.txt", "test1.txt")  # 文件重命名
'''
# 异常捕获 try:   except  IOError  文件找不到属于IO异常（输入输出异常）
# NameError   变量名异常（操作，输出变量未定义）  except(IOError, NameError...)捕获多个异常
# try ...finally   finally：一定会执行   except Exception as result:（跟踪错误）

def Write():
    f = open("gushi.txt", "w")
    f.write("\t春晓\t\n春眠不觉晓，\n处处闻啼鸟。\n夜来风雨声，\n花落知多少。\n")
    f.close()
def ReadAndCopy():
    f = open("gushi.txt", "r")
    ff = open("copy.txt", "w")
    poem = f.readlines()
    for i in poem:
        try:
          ff.write(i)
        except:
            pass
        print(i)
    print("复制完毕!")
    ff = open("copy.txt", "r")
    poemcopy = ff.readlines()
    for k in poemcopy:
        print(k)
    f.close()
    ff.close()
Write()
ReadAndCopy()




